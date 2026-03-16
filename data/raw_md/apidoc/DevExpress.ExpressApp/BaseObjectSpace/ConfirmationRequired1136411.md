---
uid: DevExpress.ExpressApp.BaseObjectSpace.ConfirmationRequired
name: ConfirmationRequired
type: Event
summary: Occurs when performing **Refresh** or **Rollback** operations with the current Object Space's persistent objects.
syntax:
  content: public event EventHandler<ConfirmationEventArgs> ConfirmationRequired
seealso: []
---

`BaseObjectSpace` raises the `ConfirmationRequired` event from the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) or [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) methods.

Windows Forms applications use this event to show confirmation messages. The following topics describe how to change this behavior:
* @DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode
* [](xref:403181)

When you create an Object Space and use it internally, handle the `ConfirmationRequired` event to show a confirmation message for the **Refresh** and **Rollback** operations. The confirmation type comes from the handler's `ConfirmationEventArgs.ConfirmationType` parameter. Set the handler's `ConfirmationEventArgs.ConfirmationResult` parameter to specify what operation the calling method should execute.
