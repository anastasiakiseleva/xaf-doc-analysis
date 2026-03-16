---
uid: DevExpress.ExpressApp.SystemModule.RefreshController.RefreshAction
name: RefreshAction
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.SystemModule.RefreshController)'s **Refresh** Action.
syntax:
  content: public SimpleAction RefreshAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the **Refresh** Action.
seealso: []
---
The **Refresh** Action is intended to refresh the object(s) represented by the current View.

This Action's **Execute** event is handled by the **RefreshController**'s **Refresh** protected method (see the class' description). If you need to modify the way this Action is executed, inherit from this Controller and override the **Refresh** method.

By default, the **Refresh** Action is activated for root Views only (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)).

The **Refresh** Action is disabled when the object in the current Detail View is new, i.e. the object has not been committed to the database.

To ascertain why the **Refresh** Action is currently deactivated or disabled, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property, respectively.

Information on the **Refresh** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).