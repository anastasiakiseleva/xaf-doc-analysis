# XAF Concepts vs SC Features – Gap Report

**Total concepts:** 148  
**Matched:** 63  
**Unmatched (flagged):** 85

## Flagged – not found in `xaf-sc-features-by-category.json`

| Concept name | ID |
|---|---|
| Model Differences | `xaf.architecture.application-model.model-differences` |
| Model Extension | `xaf.architecture.application-model.model-extension` |
| Model Nodes | `xaf.architecture.application-model.model-nodes` |
| ApplicationBuilder | `xaf.architecture.core.applicationbuilder` |
| Web API Service | `xaf.architecture.core.web-api-service` |
| Business Object Lifecycle | `xaf.data.business-model.business-object-lifecycle` |
| Custom Validation Rules | `xaf.data.business-model.custom-validation-rules` |
| Tree Node Interface | `xaf.data.business-model.tree-node-interface` |
| Optimistic Locking | `xaf.data.concurrency.optimistic-locking` |
| Database Connection | `xaf.data.database.database-connection` |
| Async Operations | `xaf.data.object-space.async-operations` |
| Object Space Provider | `xaf.data.object-space.object-space-provider` |
| Entity Framework Core | `xaf.data.orm.entity-framework-core` |
| Auto-Increment Fields | `xaf.data.properties.auto-increment-fields` |
| Calculated Property | `xaf.data.properties.calculated-property` |
| Collection Property | `xaf.data.properties.collection-property` |
| Property Metadata | `xaf.data.properties.property-metadata` |
| Reference Property | `xaf.data.properties.reference-property` |
| Object Relationships | `xaf.data.relationships.object-relationships` |
| Database Update | `xaf.data.updates.database-update` |
| Culture-Specific Formatting | `xaf.localization.localization.culture-specific-formatting` |
| Localization Basics | `xaf.localization.localization.localization-basics` |
| Localization Tool | `xaf.localization.localization.localization-tool` |
| Programmatic Localization | `xaf.localization.localization.programmatic-localization` |
| Runtime Language Switcher | `xaf.localization.localization.runtime-language-switcher` |
| Satellite Assemblies | `xaf.localization.localization.satellite-assemblies` |
| Legacy .NET Framework | `xaf.migration.legacy.legacy-net-framework` |
| Scaling Architecture | `xaf.ops.deployment.scaling-architecture` |
| Diagnostic Tools | `xaf.ops.diagnostics.diagnostic-tools` |
| Logging | `xaf.ops.logging.logging` |
| Memory Management | `xaf.quality.performance.memory-management` |
| Authorization | `xaf.security.authorization.authorization` |
| Permission Policies | `xaf.security.authorization.permission-policies` |
| Security System | `xaf.security.core.security-system` |
| Custom User Management | `xaf.security.users.custom-user-management` |
| Assembly References | `xaf.tooling.project-creation.assembly-references` |
| Package Management | `xaf.tooling.project-creation.package-management` |
| Project Wizards | `xaf.tooling.project-creation.project-wizards` |
| Action Container View Items | `xaf.ui.actions.action-container-view-items` |
| Action Containers | `xaf.ui.actions.action-containers` |
| Action Customization | `xaf.ui.actions.action-customization` |
| Action State Management | `xaf.ui.actions.action-state-management` |
| Built-in Actions | `xaf.ui.actions.built-in-actions` |
| Parametrized Action | `xaf.ui.actions.parametrized-action` |
| Popup Window Show Action | `xaf.ui.actions.popup-window-show-action` |
| Simple Action | `xaf.ui.actions.simple-action` |
| Single Choice Action | `xaf.ui.actions.single-choice-action` |
| CRUD Controllers | `xaf.ui.controllers.crud-controllers` |
| Controller Activation | `xaf.ui.controllers.controller-activation` |
| Controller Lifecycle | `xaf.ui.controllers.controller-lifecycle` |
| Controller Types | `xaf.ui.controllers.controller-types` |
| Dialog Controller | `xaf.ui.controllers.dialog-controller` |
| Generic View Controllers | `xaf.ui.controllers.generic-view-controllers` |
| List View Controllers | `xaf.ui.controllers.list-view-controllers` |
| Object View Controllers | `xaf.ui.controllers.object-view-controllers` |
| Target Properties | `xaf.ui.controllers.target-properties` |
| Window Controller | `xaf.ui.controllers.window-controller` |
| Mail Merge | `xaf.ui.editors.mail-merge` |
| Property Editor Customization | `xaf.ui.editors.property-editor-customization` |
| Property Editor Features | `xaf.ui.editors.property-editor-features` |
| Property Editor Types | `xaf.ui.editors.property-editor-types` |
| Layout Runtime Customization | `xaf.ui.layout.layout-runtime-customization` |
| Tabbed MDI Interface | `xaf.ui.navigation.tabbed-mdi-interface` |
| Application Templates | `xaf.ui.templates.application-templates` |
| SVG Graphics | `xaf.ui.theming.svg-graphics` |
| Theming | `xaf.ui.theming.theming` |
| Context Menus | `xaf.ui.ux.context-menus` |
| Error Styling | `xaf.ui.ux.error-styling` |
| Filtering UI | `xaf.ui.ux.filtering-ui` |
| Inline Editing | `xaf.ui.ux.inline-editing` |
| Loading Indicators | `xaf.ui.ux.loading-indicators` |
| Charts | `xaf.ui.views.charts` |
| Dashboard View Items | `xaf.ui.views.dashboard-view-items` |
| List View Data Access Modes | `xaf.ui.views.list-view-data-access-modes` |
| Lookup View | `xaf.ui.views.lookup-view` |
| Master-Detail Views | `xaf.ui.views.master-detail-views` |
| Nested Views | `xaf.ui.views.nested-views` |
| Reports V2 | `xaf.ui.views.reports-v2` |
| Static View Items | `xaf.ui.views.static-view-items` |
| View Customization | `xaf.ui.views.view-customization` |
| View Lifecycle | `xaf.ui.views.view-lifecycle` |
| View Types | `xaf.ui.views.view-types` |
| Frames | `xaf.ui.windows-frames.frames` |
| Popup Windows | `xaf.ui.windows-frames.popup-windows` |
| Windows | `xaf.ui.windows-frames.windows` |

## Matched concepts

| Concept name | Matched SC feature(s) |
|---|---|
| Application Model | Application Model, Application Model |
| Model Cache | Cache (ModelAssembly, EnableModelCache) |
| XAF Application | Application Model, Application Model |
| Dependency Injection | Dependency Injection in Controllers, Business Objects |
| Modules | Limit Tenant Features (SKU, Modules, User Count), Dynamically Loaded Modules and Types |
| Multi-Tenancy | Multi-Tenancy (SaaS-ready/multiple tenants), Multi-Tenancy (SaaS-ready/multiple tenants) |
| Tenant | Multi-Tenancy (SaaS-ready/multiple tenants), Multi-Tenancy (SaaS-ready/multiple tenants) |
| Business Object | Dependency Injection in Controllers, Business Objects |
| Clone Object | Clone Object Module, Clone Object Module |
| Non-persistent Object | Non-Persistent Objects, Validate Persistent Objects in Non-XAF Apps |
| State Machine | State Machine Module, State Machine Module |
| Validation | Validation Module, Validation Module |Multi-Tenancy (SaaS-ready/multiple tenants)
| Built-in Criteria Operators | Built-In Criteria Operators |
| Criteria | Built-In Criteria Operators, Custom Criteria Functions |
| Custom Criteria Functions | Custom Criteria Functions |
| Direct SQL | Direct SQL |
| Multiple Databases | Security inMultiple Databases |
| Business Logic | Data Manipulation and Business Logic, Data Manipulation and Business Logic |
| Object Space | Error: Object belongs to a different Session/Space, Error: using CreateObjectSpace() |
| XPO | XPO IList Associations (ManyToManyAliasAttribute), XPO OData, Web API Services, JSON Serialization |
| File Attachments | File Attachments Module, File Attachments Module |
| Migration | ORM Database Schema Migrations |
| Deployment | Deployment, Deployment |
| Performance Optimization | Performance, Performance |
| Testing | Debugging, Testing, and Error Handling, Debugging, Testing, and Error Handling |
| Audit Trail | Audit Trail Module, Audit Trail Module |
| Authentication | Custom Authentication/Logon Parameters Form, OAuth Identity Providers |
| Middle Tier | Middle-Tier Application Server |
| Model Editor | Model Editor, Localization in Model Editor |
| Template Kit | Template Kit |
| Action Types | Built-in Action Types |
| Actions | Controllers, Actions, Frame Templates (Form Templates), InPlace Actions in Grid Cells |
| Built-in Controllers | Built-in Controllers |
| Controller Customization | ShowNavigationItemController Customization |
| Controllers and Actions | Controllers, Actions, Frame Templates (Form Templates) |
| View Controller | Custom Logic Withing View or Controller |
| Collection Property Editors | Custom Property Editors |
| Lookup Property Editors | Custom Property Editors, Lookup Property Editors |
| Office Module | Office Module (Rich Text, Spreadsheets, PDF, Office Module (Rich Text, Spreadsheets, PDF |
| Property Editors | Custom Property Editors, Views and View Items and Property Editors |
| Specialized Property Editors | Custom Property Editors |
| Spreadsheet Control | Spreadsheet |
| Standard Property Editors | Custom Property Editors |
| Accordion Control | Accordion Control |
| Layout | Custom Detail View Layouts, Custom List View Layouts |
| Layout Generation | Layout Generation and Customization API |
| List Editors | Custom List Editors, TreeList Editors Module |
| Tree List | TreeList Editors Module, TreeList Editors Module |
| Navigation | Navigation System, Navigation System |
| Conditional Appearance | Conditional Appearance Module, Conditional Appearance Module |
| Notifications | Notifications Module, Notifications Module |
| Dashboard View | Custom Views (Dashboard, Report, etc.), DashboardViews |
| Dashboards | Dashboards Module, Dashboards Module |
| Detail View | Custom Detail View Layouts, ListViewAndDetailView (Master-Detail |
| List View | Custom List View Layouts, ListViewAndDetailView (Master-Detail |
| PivotGrid | Pivot Grid Module, Pivot Grid Module |
| Recurring Events | Recurring Events |
| Report Parameters | XAF Report Object Parameters, XtraReport Parameters |
| Reports | XPObjectSource for Reports and Dashboards, Reports Module |
| Scheduler | Scheduler Module, Scheduler Module |
| View Items | Views and View Items and Property Editors, Views and View Items and Property Editors |
| View Variants | View Variants Module, View Variants Module |
| Views | Custom Views (Dashboard, Report, etc.), Views and View Items and Property Editors |
