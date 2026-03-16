---
uid: DevExpress.ExpressApp.SystemModule.ModificationsController
name: ModificationsController
type: Class
summary: An [](xref:DevExpress.ExpressApp.ObjectViewController) descendant that contains **Cancel**, **Save**, **Save And Close**, and **Save And New** [Actions](xref:112622).
syntax:
  content: 'public class ModificationsController : ObjectViewController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ModificationsController._members
  altText: ModificationsController Members
---
`ModificationsController` displays **Cancel**, **Save**, **SaveAndClose** and **SaveAndNew** Actions in Object Views.

ASP.NET Core Blazor
:   ![|Modifications Controller in ASP.NET Core Blazor, DevExpress|](~/images/blazor-modificationscontroller-detailview.png)

Windows Forms
:   ![|Modifications Controller in Windows Forms, DevExpress|](~/images/detailviewcontroller115929.png)

For detailed information about **Cancel**, **Save**, **Save and Close**, and **Save and New** Actions, refer to the following property descriptions:
* [ModificationsController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.CancelAction)
* [ModificationsController.SaveAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAction)
* [ModificationsController.SaveAndCloseAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndCloseAction)
* [ModificationsController.SaveAndNewAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndNewAction)

To customize the default behavior of these Actions, inherit from a platform-specific Controller or subscribe to its events. In addition, you can access Actions to modify their behavior.

| Platform | Descendant |
| -------- | ---------- |
| ASP.NET Core Blazor | [](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorModificationsController) |
| Windows Forms | [](xref:DevExpress.ExpressApp.Win.SystemModule.WinModificationsController) |

If you need to override one the following protected virtual methods, inherit from the platform-specific controller:

| Method | Trigger Action | Description |
|---|---|---|
| `Save` | The **Save** Action. | The **Save** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Does nothing. Overridden in the Controller's descendants. |
| `SaveAndClose` | The **Save and Close** Action. | The **Save and Close** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Does nothing. Overridden in the Controller's descendants. |
| `SaveAndNew` | The **Save and New** Action. | The  **Save and New** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Commits changes made to the current View's object and executes the **New** Action, if it is available (see [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)). |
| `Cancel` | The **Cancel** Action. | The **Cancel** Action's [SimpleAction.Execute](xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute) event handler. Does nothing. Overridden in the Controller's descendants. |
| `UpdateActionState` | A change in environment (for example, the current object was changed). | Checks whether the active or enabled state of the **Save**, **Save and Close**, **Save and New** and **Cancel** Actions should be changed after changes in the environment. |

This Controller is activated for Object Views only. To check whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property. If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information about `ModificationsController` and its **Cancel**, **Save**, **SaveAndClose**, and **SaveAndNew** Actions is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).
