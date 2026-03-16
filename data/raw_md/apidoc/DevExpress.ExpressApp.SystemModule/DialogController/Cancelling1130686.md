---
uid: DevExpress.ExpressApp.SystemModule.DialogController.Cancelling
name: Cancelling
type: Event
summary: Occurs when executing the current Dialog Controller's [DialogController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.CancelAction).
syntax:
  content: public event EventHandler Cancelling
seealso: []
---
When executing the Action specified by the Dialog Controller's [DialogController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.CancelAction) property, the current pop-up Window is closed. Handle the **Cancelling** event to perform custom actions before closing the Window.

If you need to cancel closing the current pop-up Window, set the [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) property to **false**. By default, this property is set to **true**.