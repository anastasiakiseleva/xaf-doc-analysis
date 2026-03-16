---
uid: DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction
name: AcceptAction
type: Property
summary: Provides access to the current Dialog Controller's **DialogOK**Action.
syntax:
  content: public SimpleAction AcceptAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the Dialog Controller's **DialogOK** Action.
seealso: []
---
The Dialog Controller contains the Accept Action. This Action is available if it has a caption. To execute this Action, press the current pop-up Window's accept button or double-click an object in the pop-up Window's List View. Executing this Actions results in the following:

* The current Window contains a [Detail View](xref:112611):
    
    The **Save** Action of the current Window's **ModificationsController** is executed (by the Execute event handler), and the Window is closed (by the ExecuteCompleted event handler).
* The current Window contains a [List View](xref:112611):
    
    The current Window is closed (by the ExecuteCompleted event handler).

The Accept Action's [ActionBase.ActionMeaning](xref:DevExpress.ExpressApp.Actions.ActionBase.ActionMeaning) property is set to [ActionMeaning.Accept](xref:DevExpress.ExpressApp.Actions.ActionMeaning.Accept), by default.

To change any of the Accept Action's settings ([ActionBase.Caption](xref:DevExpress.ExpressApp.Actions.ActionBase.Caption), [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active)), use the **AcceptAction** property. To perform custom code before executing this Action, handle the Dialog Controller's [DialogController.Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) event. To change the default behavior of this Action, use the Dialog Controller's [DialogController.SaveOnAccept](xref:DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept) and [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) properties.

By default, the Accept Action is displayed by the "PopupActions" [Action Container](xref:112610). To change this behavior, use the [DialogController.DialogActionContainerName](xref:DevExpress.ExpressApp.SystemModule.DialogController.DialogActionContainerName) field. If you set another Action Container for this field, be sure that it is contained in the [Template](xref:112609) that displays your pop-up Window.