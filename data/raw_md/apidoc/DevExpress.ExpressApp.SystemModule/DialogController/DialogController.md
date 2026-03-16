---
uid: DevExpress.ExpressApp.SystemModule.DialogController
name: DialogController
type: Class
summary: Represents a [](xref:DevExpress.ExpressApp.WindowController) descendant that contains Actions for pop-up [Windows](xref:112608).
syntax:
  content: 'public class DialogController : WindowController'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.DialogController._members
  altText: DialogController Members
---
The **DialogController** class is a descendant of the [](xref:DevExpress.ExpressApp.WindowController) class. It is intended to present the **Accept** and **Cancel** buttons in pop-up Windows. You can inherit from this Controller to modify its behavior.

The Dialog Controller has a peculiarity. It is not added to a Frame's [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection automatically. You should add it yourself.

Basically, the Dialog Controller is required in pop-up Windows only. There are two approaches to add a Dialog Controller to a pop-up Window:

* Use the [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction)
    
    The **DialogController** class instance is, by default, contained in the pop-up Window invoked from a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction). Use the [CustomizePopupWindowParamsEventArgs.DialogController](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.DialogController) parameter of your PopupWindowShowAction's [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event handler, to access the Dialog Controller set by default, or to replace it with a custom one.
* Use [](xref:DevExpress.ExpressApp.ShowViewParameters)
    
    Add a Dialog Controller in a pop-up Window via the [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) parameter of your Action's**Execute** event handler.

For details, refer to the [Dialog Controller](xref:112805) topic.

Use the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) and [DialogController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.CancelAction) properties to access the Dialog Controller's **Accept** and **Cancel** Actions. To change their behavior, use the [DialogController.SaveOnAccept](xref:DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept) and [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) properties, and handle the [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) and [DialogController.Cancelling](xref:DevExpress.ExpressApp.SystemModule.DialogController.Cancelling) events.

Information on the DialogController and its Actions is available in the [Application Model](xref:112580). To access it, use the [Model Editor](xref:112582).