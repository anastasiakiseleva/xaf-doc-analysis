"""Apply approved doc_intents to xaf-taxonomy.json."""
import json
from pathlib import Path

TAXONOMY_PATH = Path(__file__).parent.parent / "config" / "xaf-taxonomy.json"

# All 148 approved doc_intents mapped by concept ID
DOC_INTENTS = {
    "xaf.architecture.core.web-api-service": ["concept", "how_to", "configuration", "reference"],
    "xaf.data.orm.entity-framework-core": ["concept", "how_to", "configuration", "reference", "troubleshooting"],
    "xaf.data.orm.xpo": ["concept", "how_to", "configuration", "reference", "troubleshooting"],
    "xaf.data.business-model.non-persistent-object": ["concept", "how_to", "configuration", "reference"],
    "xaf.data.business-model.business-object": ["concept", "how_to", "tutorial", "reference"],
    "xaf.data.object-space.business-logic": ["concept", "how_to", "reference"],
    "xaf.security.core.security-system": ["concept", "how_to", "tutorial", "configuration", "reference"],
    "xaf.security.authentication.authentication": ["concept", "how_to", "configuration", "reference", "troubleshooting"],
    "xaf.security.authorization.authorization": ["concept", "how_to", "configuration", "reference"],
    "xaf.architecture.application-model.application-model": ["concept", "how_to", "tutorial", "configuration", "reference"],
    "xaf.ui.views.views": ["concept", "how_to", "tutorial", "configuration", "reference"],
    "xaf.ui.editors.property-editors": ["concept", "how_to", "reference", "configuration"],
    "xaf.ui.list-editors.list-editors": ["concept", "how_to", "reference", "configuration"],
    "xaf.ui.controllers.controllers-and-actions": ["concept", "how_to", "tutorial", "reference"],
    "xaf.ui.windows-frames.frames": ["concept", "how_to", "reference"],
    "xaf.ui.windows-frames.windows": ["concept", "how_to", "reference"],
    "xaf.ui.templates.application-templates": ["concept", "how_to", "reference", "configuration"],
    "xaf.ui.layout.layout": ["concept", "how_to", "reference", "configuration"],
    "xaf.architecture.core.xaf-application": ["concept", "how_to", "tutorial", "configuration", "reference"],
    "xaf.architecture.modules.modules": ["concept", "how_to", "reference"],
    "xaf.architecture.application-model.model-nodes": ["concept", "reference"],
    "xaf.tooling.model-editor.model-editor": ["concept", "how_to", "tutorial"],
    "xaf.architecture.application-model.model-differences": ["concept", "how_to", "configuration"],
    "xaf.architecture.application-model.model-extension": ["concept", "how_to", "reference"],
    "xaf.architecture.application-model.model-cache": ["concept", "how_to", "configuration"],
    "xaf.architecture.core.applicationbuilder": ["concept", "how_to", "reference", "configuration"],
    "xaf.architecture.dependency-injection.dependency-injection": ["concept", "how_to", "reference"],
    "xaf.security.core.middle-tier": ["concept", "how_to", "configuration"],
    "xaf.data.object-space.async-operations": ["concept", "how_to", "reference"],
    "xaf.data.object-space.object-space": ["concept", "how_to", "tutorial", "reference"],
    "xaf.data.object-space.object-space-provider": ["concept", "how_to", "reference"],
    "xaf.data.database.database-connection": ["concept", "how_to", "configuration"],
    "xaf.data.relationships.object-relationships": ["concept", "how_to", "reference"],
    "xaf.data.business-model.business-object-lifecycle": ["concept", "how_to", "reference"],
    "xaf.data.properties.collection-property": ["concept", "how_to", "reference"],
    "xaf.data.properties.reference-property": ["concept", "how_to", "reference"],
    "xaf.data.properties.calculated-property": ["concept", "how_to", "reference"],
    "xaf.data.properties.property-metadata": ["concept", "how_to", "reference", "configuration"],
    "xaf.data.criteria.criteria": ["concept", "how_to", "reference"],
    "xaf.data.criteria.built-in-criteria-operators": ["reference"],
    "xaf.data.criteria.custom-criteria-functions": ["concept", "how_to", "reference"],
    "xaf.data.database.multiple-databases": ["concept", "how_to", "configuration"],
    "xaf.data.database.direct-sql": ["concept", "how_to", "reference"],
    "xaf.data.properties.auto-increment-fields": ["concept", "how_to"],
    "xaf.data.concurrency.optimistic-locking": ["concept", "how_to", "configuration", "reference"],
    "xaf.data.business-model.tree-node-interface": ["concept", "how_to", "reference"],
    "xaf.data.updates.database-update": ["concept", "how_to", "reference"],
    "xaf.ui.views.view-types": ["concept", "reference"],
    "xaf.ui.views.list-view": ["concept", "how_to", "configuration", "reference"],
    "xaf.ui.views.list-view-data-access-modes": ["concept", "how_to", "configuration"],
    "xaf.ui.views.detail-view": ["concept", "how_to", "configuration", "reference"],
    "xaf.ui.views.dashboard-view": ["concept", "how_to", "configuration", "reference"],
    "xaf.ui.views.lookup-view": ["concept", "how_to", "configuration"],
    "xaf.ui.views.view-items": ["concept", "how_to", "reference"],
    "xaf.ui.views.static-view-items": ["concept", "how_to"],
    "xaf.ui.views.dashboard-view-items": ["concept", "how_to"],
    "xaf.ui.actions.action-container-view-items": ["concept", "how_to"],
    "xaf.ui.views.view-customization": ["concept", "how_to", "configuration"],
    "xaf.ui.views.master-detail-views": ["concept", "how_to", "configuration"],
    "xaf.ui.views.nested-views": ["concept", "how_to"],
    "xaf.ui.views.view-variants": ["concept", "how_to", "configuration"],
    "xaf.ui.views.view-lifecycle": ["concept", "reference"],
    "xaf.ui.layout.layout-generation": ["concept", "how_to"],
    "xaf.ui.layout.layout-runtime-customization": ["concept", "how_to", "configuration"],
    "xaf.ui.windows-frames.popup-windows": ["concept", "how_to", "reference"],
    "xaf.ui.ux.inline-editing": ["concept", "how_to", "configuration"],
    "xaf.ui.list-editors.tree-list": ["concept", "how_to", "configuration"],
    "xaf.ui.editors.property-editor-types": ["concept", "reference"],
    "xaf.ui.editors.standard-property-editors": ["reference", "configuration"],
    "xaf.ui.editors.lookup-property-editors": ["concept", "how_to", "configuration", "reference"],
    "xaf.ui.editors.collection-property-editors": ["concept", "how_to", "configuration"],
    "xaf.ui.editors.specialized-property-editors": ["concept", "how_to", "reference"],
    "xaf.ui.editors.property-editor-customization": ["concept", "how_to", "reference"],
    "xaf.ui.editors.property-editor-features": ["concept", "how_to", "configuration"],
    "xaf.ui.controllers.controller-types": ["concept", "reference"],
    "xaf.ui.controllers.view-controller": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.generic-view-controllers": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.object-view-controllers": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.window-controller": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.dialog-controller": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.controller-activation": ["concept", "how_to"],
    "xaf.ui.controllers.target-properties": ["concept", "reference"],
    "xaf.ui.controllers.controller-lifecycle": ["concept", "reference"],
    "xaf.ui.controllers.built-in-controllers": ["reference"],
    "xaf.ui.controllers.crud-controllers": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.list-view-controllers": ["concept", "how_to", "reference"],
    "xaf.ui.controllers.controller-customization": ["concept", "how_to", "reference"],
    "xaf.ui.navigation.tabbed-mdi-interface": ["concept", "how_to", "configuration"],
    "xaf.ui.ux.context-menus": ["concept", "how_to", "configuration"],
    "xaf.ui.ux.loading-indicators": ["concept", "how_to", "configuration"],
    "xaf.ui.ux.filtering-ui": ["concept", "how_to", "configuration"],
    "xaf.ui.editors.spreadsheet-control": ["concept", "how_to", "configuration"],
    "xaf.ui.theming.svg-graphics": ["concept", "how_to"],
    "xaf.ui.layout.accordion-control": ["concept", "how_to", "configuration"],
    "xaf.ui.theming.theming": ["concept", "how_to", "configuration"],
    "xaf.ui.navigation.navigation": ["concept", "how_to", "configuration", "reference"],
    "xaf.ui.actions.actions": ["concept", "how_to", "tutorial", "reference"],
    "xaf.ui.actions.action-types": ["concept", "reference"],
    "xaf.ui.actions.simple-action": ["concept", "how_to", "reference"],
    "xaf.ui.actions.parametrized-action": ["concept", "how_to", "reference"],
    "xaf.ui.actions.popup-window-show-action": ["concept", "how_to", "reference"],
    "xaf.ui.actions.single-choice-action": ["concept", "how_to", "reference"],
    "xaf.ui.actions.action-containers": ["concept", "how_to", "configuration"],
    "xaf.ui.actions.action-state-management": ["concept", "how_to", "reference"],
    "xaf.ui.actions.action-customization": ["concept", "how_to", "configuration"],
    "xaf.ui.actions.built-in-actions": ["reference"],
    "xaf.security.users.custom-user-management": ["concept", "how_to", "reference"],
    "xaf.security.authorization.permission-policies": ["concept", "how_to", "configuration", "reference"],
    "xaf.security.auditing.audit-trail": ["concept", "how_to", "configuration"],
    "xaf.data.business-model.validation": ["concept", "how_to", "configuration", "reference"],
    "xaf.data.business-model.custom-validation-rules": ["concept", "how_to", "reference"],
    "xaf.ui.ux.error-styling": ["concept", "how_to", "configuration"],
    "xaf.ui.theming.conditional-appearance": ["concept", "how_to", "configuration"],
    "xaf.ui.views.reports": ["concept", "how_to", "configuration"],
    "xaf.ui.views.report-parameters": ["concept", "how_to"],
    "xaf.ui.views.reports-v2": ["concept", "how_to", "configuration"],
    "xaf.ui.editors.mail-merge": ["concept", "how_to", "configuration"],
    "xaf.ui.views.dashboards": ["concept", "how_to", "configuration"],
    "xaf.ui.views.scheduler": ["concept", "how_to", "configuration"],
    "xaf.ui.views.recurring-events": ["concept", "how_to"],
    "xaf.ui.ux.notifications": ["concept", "how_to", "configuration"],
    "xaf.data.business-model.state-machine": ["concept", "how_to", "configuration"],
    "xaf.data.properties.file-attachments": ["concept", "how_to", "configuration"],
    "xaf.ui.views.charts": ["concept", "how_to", "configuration"],
    "xaf.ui.views.pivotgrid": ["concept", "how_to", "configuration"],
    "xaf.data.business-model.clone-object": ["concept", "how_to", "configuration"],
    "xaf.ui.editors.office-module": ["concept", "how_to", "configuration"],
    "xaf.localization.localization.programmatic-localization": ["concept", "how_to", "reference"],
    "xaf.localization.localization.localization-basics": ["concept", "how_to", "configuration"],
    "xaf.localization.localization.localization-tool": ["concept", "how_to", "tutorial"],
    "xaf.localization.localization.satellite-assemblies": ["concept", "how_to"],
    "xaf.localization.localization.runtime-language-switcher": ["concept", "how_to", "configuration"],
    "xaf.localization.localization.culture-specific-formatting": ["concept", "how_to", "configuration"],
    "xaf.architecture.multi-tenancy.multi-tenancy": ["concept", "how_to", "configuration", "reference"],
    "xaf.architecture.multi-tenancy.tenant": ["concept", "reference"],
    "xaf.ops.deployment.deployment": ["concept", "how_to", "configuration"],
    "xaf.quality.testing.testing": ["concept", "how_to", "reference"],
    "xaf.ops.logging.logging": ["concept", "how_to", "configuration"],
    "xaf.ops.diagnostics.diagnostic-tools": ["concept", "how_to"],
    "xaf.quality.performance.performance-optimization": ["concept", "how_to", "troubleshooting"],
    "xaf.quality.performance.memory-management": ["concept", "how_to", "troubleshooting"],
    "xaf.ops.deployment.scaling-architecture": ["concept", "how_to", "configuration"],
    "xaf.tooling.project-creation.package-management": ["concept", "how_to"],
    "xaf.tooling.project-creation.assembly-references": ["concept", "how_to", "troubleshooting"],
    "xaf.tooling.project-creation.template-kit": ["concept", "how_to", "tutorial"],
    "xaf.migration.legacy.legacy-net-framework": ["concept"],
    "xaf.migration.migration.migration": ["concept", "how_to"],
    "xaf.tooling.project-creation.project-wizards": ["concept", "how_to"],
}


def main():
    with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
        taxonomy = json.load(f)

    concepts = taxonomy["taxonomy"]["concepts"]
    updated = 0
    missing = []

    for concept in concepts:
        cid = concept["id"]
        if cid in DOC_INTENTS:
            if "documentation" not in concept:
                concept["documentation"] = {}
            concept["documentation"]["doc_intents"] = DOC_INTENTS[cid]
            updated += 1
        else:
            missing.append(cid)

    with open(TAXONOMY_PATH, "w", encoding="utf-8") as f:
        json.dump(taxonomy, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Updated {updated}/{len(concepts)} concepts with doc_intents.")
    if missing:
        print(f"WARNING: {len(missing)} concepts had no mapping:")
        for m in missing:
            print(f"  - {m}")
    
    # Verify count matches
    mapped_ids = set(DOC_INTENTS.keys())
    concept_ids = {c["id"] for c in concepts}
    extra = mapped_ids - concept_ids
    if extra:
        print(f"WARNING: {len(extra)} mapped IDs not found in taxonomy:")
        for e in extra:
            print(f"  - {e}")


if __name__ == "__main__":
    main()
