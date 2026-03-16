---
uid: DevExpress.ExpressApp.BaseObjectSpace.RollingBack
name: RollingBack
type: Event
summary: Occurs before rolling back the changes made to the current Object Space's persistent objects.
syntax:
  content: public event EventHandler<CancelEventArgs> RollingBack
seealso: []
---
The **RollingBack** event is raised before updating persistent objects as a result of calling the [BaseObjectSpace.Rollback](xref:DevExpress.ExpressApp.BaseObjectSpace.Rollback(System.Boolean)) method. Handle this event to prevent objects from rolling back. For this purpose, set the handler's **CancelEventArgs.Cancel** parameter to **true**. By default, this parameter is set to **false**.