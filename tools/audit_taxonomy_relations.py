#!/usr/bin/env python3
"""
D1/D2: Taxonomy Audit — Convert implied related_to edges to directed relations.

Two types of changes:
  1. REMOVE redundant related_to entries where a part_of or is_a relation already
     exists in the reverse direction (parent lists child as related_to, but child
     already declares part_of/is_a pointing back to parent). These are noisy
     bidirectional echoes of a hierarchy that already exists.

  2. CONVERT select related_to pairs to `requires` where XAF documentation
     confirms a clear dependency relationship.

Rationale: `related_to` signals in taxonomy context bias the LLM classifier toward
outputting `related_to` even when a directional type would be appropriate. Removing
false related_to signals reduces that bias.

Usage:
    python tools/audit_taxonomy_relations.py              # dry-run (show changes)
    python tools/audit_taxonomy_relations.py --apply      # write changes
    python tools/audit_taxonomy_relations.py --apply --backup  # backup first
"""

import argparse
import json
import shutil
from pathlib import Path
from datetime import datetime


TAXONOMY_PATH = Path("config/xaf-taxonomy.json")

# Explicit requires relationships to ADD, sourced from XAF documentation:
#   "all data-aware manipulations and custom business logic are performed via
#    the Object Space" (docs.devexpress.com/eXpressAppFramework/113707)
#   "Deployment requires database update steps" (standard XAF deployment flow)
REQUIRES_TO_ADD = [
    (
        "xaf.data.business-model.business-object",
        "xaf.data.object-space.object-space",
        "All CRUD on business objects is performed via Object Space (docs.devexpress.com/eXpressAppFramework/113707)"
    ),
]


def load_taxonomy(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_taxonomy(path: Path, tax: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tax, f, indent=2, ensure_ascii=False)
    print(f"  Saved -> {path}")


def find_redundant_related_to(concepts: list) -> list[tuple[str, str, str]]:
    """
    Find related_to(A, B) pairs that are redundant because part_of(B, A) or is_a(B, A)
    already exists — i.e., B declares itself as part of / a kind of A, so A's related_to
    entry for B is just a noisy echo of that hierarchy edge.

    Returns list of (source_id, target_id, reason).
    """
    # Index: for each concept, collect what it declares as part_of or is_a
    child_to_parents: dict[str, set[str]] = {}  # child_id -> set of parent_ids
    for c in concepts:
        cid = c["id"]
        child_to_parents.setdefault(cid, set())
        for rtype in ("part_of", "is_a"):
            for parent_id in c.get("relations", {}).get(rtype, []):
                child_to_parents[cid].add(parent_id)

    redundant = []
    for c in concepts:
        src_id = c["id"]
        for tgt_id in c.get("relations", {}).get("related_to", []):
            # Check if tgt has declared itself part_of/is_a src
            if src_id in child_to_parents.get(tgt_id, set()):
                reason = f"{tgt_id} already has part_of/is_a -> {src_id}"
                redundant.append((src_id, tgt_id, reason))

    return redundant


def find_explicit_requires_to_add(concepts: list) -> list[tuple[str, str, str]]:
    """
    Returns the REQUIRES_TO_ADD entries that are not yet in the taxonomy as `requires`.
    """
    id_to_concept = {c["id"]: c for c in concepts}
    to_add = []
    for src_id, tgt_id, rationale in REQUIRES_TO_ADD:
        src = id_to_concept.get(src_id)
        if not src:
            print(f"  WARNING: concept {src_id} not found in taxonomy")
            continue
        existing_requires = src.get("relations", {}).get("requires", [])
        if tgt_id in existing_requires:
            continue  # already there
        to_add.append((src_id, tgt_id, rationale))
    return to_add


def apply_changes(
    concepts: list,
    redundant: list[tuple[str, str, str]],
    requires_to_add: list[tuple[str, str, str]],
) -> int:
    id_to_concept = {c["id"]: c for c in concepts}
    total = 0

    # Remove redundant related_to entries
    for src_id, tgt_id, reason in redundant:
        src = id_to_concept[src_id]
        rt_list = src.get("relations", {}).get("related_to", [])
        if tgt_id in rt_list:
            rt_list.remove(tgt_id)
            if not rt_list:
                del src["relations"]["related_to"]
            total += 1

    # Add requires relationships
    for src_id, tgt_id, _ in requires_to_add:
        src = id_to_concept[src_id]
        if "relations" not in src:
            src["relations"] = {}
        if "requires" not in src["relations"]:
            src["relations"]["requires"] = []
        if tgt_id not in src["relations"]["requires"]:
            src["relations"]["requires"].append(tgt_id)
            total += 1
        # Also remove from related_to if present
        rt_list = src.get("relations", {}).get("related_to", [])
        if tgt_id in rt_list:
            rt_list.remove(tgt_id)
            if not rt_list:
                del src["relations"]["related_to"]

    return total


def main():
    parser = argparse.ArgumentParser(description="Audit and clean taxonomy related_to relationships")
    parser.add_argument("--apply", action="store_true", help="Apply changes (default: dry-run)")
    parser.add_argument("--backup", action="store_true", help="Backup taxonomy before writing")
    args = parser.parse_args()

    dry_run = not args.apply

    print("=" * 70)
    print("D1/D2: Taxonomy Relation Audit")
    print("=" * 70)
    print(f"Mode: {'DRY RUN' if dry_run else 'APPLY'}")
    print()

    tax = load_taxonomy(TAXONOMY_PATH)
    concepts = tax["taxonomy"]["concepts"]
    id_to_name = {c["id"]: c["name"] for c in concepts}

    # --- D1: Find redundant related_to ---
    redundant = find_redundant_related_to(concepts)
    print(f"Redundant related_to entries (covered by part_of/is_a in reverse): {len(redundant)}")
    for src_id, tgt_id, reason in sorted(redundant, key=lambda x: x[0]):
        src_name = id_to_name.get(src_id, src_id)
        tgt_name = id_to_name.get(tgt_id, tgt_id)
        print(f"  REMOVE related_to: {src_name} -> {tgt_name}")
        print(f"    reason: {reason}")

    print()

    # --- D2: Find requires to add ---
    requires_to_add = find_explicit_requires_to_add(concepts)
    print(f"Requires relationships to add: {len(requires_to_add)}")
    for src_id, tgt_id, rationale in requires_to_add:
        src_name = id_to_name.get(src_id, src_id)
        tgt_name = id_to_name.get(tgt_id, tgt_id)
        print(f"  ADD requires: {src_name} -> {tgt_name}")
        print(f"    rationale: {rationale}")

    print()
    total_changes = len(redundant) + len(requires_to_add)
    print(f"Total changes: {total_changes}")

    if dry_run:
        print()
        print("[DRY RUN] No changes written. Run with --apply to commit.")
        return

    if total_changes == 0:
        print("Nothing to do.")
        return

    # Backup
    if args.backup:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = TAXONOMY_PATH.parent / f"xaf-taxonomy_backup_{ts}.json"
        shutil.copy2(TAXONOMY_PATH, backup_path)
        print(f"Backup written to {backup_path}")

    # Apply
    n = apply_changes(concepts, redundant, requires_to_add)
    print(f"\nApplied {n} changes.")

    save_taxonomy(TAXONOMY_PATH, tax)

    # Summary of relation counts after
    from collections import Counter
    counts = Counter()
    for c in concepts:
        for k, vs in c.get("relations", {}).items():
            counts[k] += len(vs)
    print("\nRelation counts after changes:")
    for k, cnt in counts.most_common():
        print(f"  {k}: {cnt}")


if __name__ == "__main__":
    main()
