# Archived Tools

This folder contains tools that have been superseded by improved versions or consolidated into other scripts.

## Why Archive Instead of Delete?

- **Historical reference** - Understand evolution of analysis approaches
- **Rollback option** - Can restore if new approach has issues
- **Code reuse** - May contain useful techniques for future work
- **Documentation** - Shows what was tried and why it changed

## Archived Scripts

### 1. find_missing_deployment_apis.py.bak
**Archived:** February 11, 2026  
**Replaced by:** `tools/find_deployment_apis.py`

**Reason:** Consolidated with `list_all_deployment_apis.py` into single script with `--format` flag for different output modes.

**Old functionality:** Showed top 20 APIs needing Deployment tags with rationale.

**New equivalent:**
```bash
python tools/find_deployment_apis.py --format summary
```

### 2. list_all_deployment_apis.py.bak
**Archived:** February 11, 2026  
**Replaced by:** `tools/find_deployment_apis.py`

**Reason:** Consolidated with `find_missing_deployment_apis.py` into single script.

**Old functionality:** Exported complete list of deployment API candidates to CSV/JSON with categorization.

**New equivalent:**
```bash
python tools/find_deployment_apis.py --format complete  # CSV export
python tools/find_deployment_apis.py --format categorized  # Grouped by keyword
```

### 3. generate_crosslink_report.py.bak
**Archived:** February 11, 2026  
**Replaced by:** `tools/generate_crosslink_filtered.py`

**Reason:** Basic version superseded by advanced version with:
- Text presence validation (prevents false positives)
- Support ticket volume weighting (prioritizes pain points)
- Confidence scoring
- Multiple filter presets
- Realistic caps based on article types

**Old functionality:** Basic cross-linking recommendations without filtering.

**New equivalent:**
```bash
python tools/generate_crosslink_filtered.py
```

**Note:** Filtered version is significantly more sophisticated (955 lines vs basic version). Produces actionable, high-confidence recommendations instead of discovery dumps.

---

## Recovery Instructions

If you need to restore an archived script:

1. Copy from archive and remove `.bak` extension
2. Check if any dependencies have changed
3. Test before using in production
4. Consider why newer version was preferred

## Permanent Deletion Policy

Scripts remain in archive for:
- Minimum 6 months after archiving
- Until at least one full project cycle with replacement
- Until team confirms no need for reference

After this period, may be permanently deleted with team approval.

---

**Last Updated:** February 11, 2026
