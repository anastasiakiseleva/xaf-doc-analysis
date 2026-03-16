---
uid: DevExpress.ExpressApp.BaseObjectSpace.Committing
name: Committing
type: Event
summary: Occurs before saving the persistent objects belonging to the current Object Space to the database.
syntax:
  content: public event EventHandler<CancelEventArgs> Committing
seealso: []
---
The **Committing** event is raised before committing persistent objects as a result of calling the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method. Handle this event to prevent saving object changes to the database. For this purpose, set the handler's **CancelEventArgs.Cancel** parameter to **true**. By default, this parameter is set to **false**.