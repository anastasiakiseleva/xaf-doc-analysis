---
uid: DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)
name: Rollback(Boolean)
type: Method
summary: Discards all unsaved changes made by users and invalidates previously loaded objects in the current Object Space.
syntax:
  content: public bool Rollback(bool askConfirmation = true)
  parameters:
  - id: askConfirmation
    type: System.Boolean
    defaultValue: "True"
    description: '`true`, if the confirmation dialog is required, otherwise, `false`.'
  return:
    type: System.Boolean
    description: '`true`, if changes made to persistent objects were canceled; otherwise, `false`.'
seealso: []
---
Use this method to cancel changes to persistent objects in the current Object Space. The built-in [ModificationsController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.CancelAction) uses this method.

The `Rollback` method discards changes made by users to objects loaded by the current Object Space. If there are unsaved changes and the `askConfirmation` parameter is `true` (default), it raises the @DevExpress.ExpressApp.BaseObjectSpace.ConfirmationRequired event, and the handler's @DevExpress.ExpressApp.ConfirmationResult determines what happens next:
* `Yes` -- The changes are discarded and objects reloaded
* `No` -- Rollback operation is aborted

Internally, the `Rollback` method behaves similarly to the [Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method, with the key difference being that `Rollback` only offers Yes/No confirmation options (no Cancel option), and includes the `askConfirmation` parameter to control whether confirmation is requested.

If you call the `Rollback` method without parameters, the method prompts the following dialog:

![RefreshAskConfirmation](~/images/RefreshAskConfirmation.png)

To roll back an [Object Space](xref:113707) without a confirmation dialog, set the `askConfirmation` parameter to `false`.

The following events related to the `Rollback` method are available:

* [BaseObjectSpace.RollingBack](xref:DevExpress.ExpressApp.BaseObjectSpace.RollingBack)
    
    Handle this event to stop the `Rollback` method from rolling back. Set the handler's `CancelEventArgs.Cancel` parameter to `true`.
* [BaseObjectSpace.CustomRollBack](xref:DevExpress.ExpressApp.BaseObjectSpace.CustomRollBack)
    
    Handle this event to perform a custom rollback instead of the default one. Set the handler’s `CompletedEventArgs.Handled` parameter to `true` to show that you already performed the rollback operation. Set the handler’s `CompletedEventArgs.IsCompleted` parameter to the value that the `Rollback` method returns.

