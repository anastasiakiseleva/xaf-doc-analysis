---
uid: DevExpress.ExpressApp.SystemModule.RefreshController
name: RefreshController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.ViewController) descendant that contains the **Refresh** [Action](xref:112622).
syntax:
  content: 'public class RefreshController : ViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.RefreshController._members
  altText: RefreshController Members
---
The **RefreshController** is intended for presenting the **Refresh** Action.

For details on the **Refresh** Action, refer to the description of the [RefreshController.RefreshAction](xref:DevExpress.ExpressApp.SystemModule.RefreshController.RefreshAction) property that provides access to this Action.

To customize the default behavior of the **Refresh** Action, you can inherit from this Controller or access the Action in another Controller.

If you need to inherit from the **RefreshController**, the following protected virtual methods are availabe for overriding:

| Method | When is it called? | Description |
|---|---|---|
| Refresh | Invoked as a result of executing the **Refresh** Action. | Represents the **Refresh** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Refreshes object(s) from the current Object Space (see [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh)). |
| UpdateActionState | Invoked as a result of changes made to the current View's Object Space: | Checks whether the **Refresh** Action's active or enabled state should be changed, after the environment has been changed. |

Public members are described individually in the documentation.

This Controller is activated for all [Views](xref:112611). To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information on the **RefreshController** and its **Refresh** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).