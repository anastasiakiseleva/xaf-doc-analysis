---
uid: DevExpress.ExpressApp.SystemModule.DialogController.CancelAction
name: CancelAction
type: Property
summary: Provides access to the current Dialog Controller's **Cancel** Action.
syntax:
  content: public SimpleAction CancelAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) object representing the Dialog Controller's Cancel Action.
seealso: []
---
The Dialog Controller contains the **Cancel** Action. This Action is available if it has a caption. To execute this Action, press the current pop-up Window's cancel button. When executing this Action, the pop-up Window is closed.

The Cancel Action's [ActionBase.ActionMeaning](xref:DevExpress.ExpressApp.Actions.ActionBase.ActionMeaning) property is set to [ActionMeaning.Cancel](xref:DevExpress.ExpressApp.Actions.ActionMeaning.Cancel), by default.

To change any of the Cancel Action's settings ([ActionBase.Caption](xref:DevExpress.ExpressApp.Actions.ActionBase.Caption), [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active)), use the **CancelAction** property. To perform custom code before executing this Action, handle the Dialog Controller's [DialogController.Cancelling](xref:DevExpress.ExpressApp.SystemModule.DialogController.Cancelling) event. To change the default behavior of this Action, use the Dialog Controller's [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) property

By default, the Cancel Action is displayed by the "PopupActions" [Action Container](xref:112610). To change this behavior, use the [DialogController.DialogActionContainerName](xref:DevExpress.ExpressApp.SystemModule.DialogController.DialogActionContainerName) field. If you set another Action Container for this field, be sure that it is contained in the [Template](xref:112609) that displays your pop-up Window.