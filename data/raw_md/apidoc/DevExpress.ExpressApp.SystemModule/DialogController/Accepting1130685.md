---
uid: DevExpress.ExpressApp.SystemModule.DialogController.Accepting
name: Accepting
type: Event
summary: Occurs when executing the current Dialog Controller's [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction).
syntax:
  content: public event EventHandler<DialogControllerAcceptingEventArgs> Accepting
seealso: []
---
Executing the Action specified by the Dialog Controller's [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) property results in the following, by default:

* The current Window contains a [Detail View](xref:112611):
    
    The **Save** Action of the current Window's **ModificationsController** is executed, and the Window is closed.
* The current Window contains a [List View](xref:112611):
    
    The current Window is closed.

Handle the **Accepting** event to perform custom actions before the default actions defined above are executed. To cancel executing the default actions, set the handler's **DialogControllerAcceptingEventArgs.Cancel** parameter to **true** (by default, it is set to **false**).

If you need to cancel execution of either  the **Save** Action or closing the current pop-up Window (see above), use the [DialogController.SaveOnAccept](xref:DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept) and [DialogController.CanCloseWindow](xref:DevExpress.ExpressApp.SystemModule.DialogController.CanCloseWindow) properties.

> [!NOTE]
> The Action specified by the [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) property is executed both when pressing the pop-up Window's accept button and when double-clicking an object selected in the Window's List View.