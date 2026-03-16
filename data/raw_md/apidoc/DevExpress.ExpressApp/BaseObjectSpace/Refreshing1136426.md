---
uid: DevExpress.ExpressApp.BaseObjectSpace.Refreshing
name: Refreshing
type: Event
summary: Occurs before refreshing the current Object Space's persistent objects.
syntax:
  content: public event EventHandler<CancelEventArgs> Refreshing
seealso: []
---
The **Refreshing** event is raised before updating persistent objects as a result of calling the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method. Handle this event to prevent objects from refreshing. For this purpose, set the handler's **CancelEventArgs.Cancel** parameter to **true**. By default, this parameter is set to **false**.