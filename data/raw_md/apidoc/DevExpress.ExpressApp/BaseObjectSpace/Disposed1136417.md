---
uid: DevExpress.ExpressApp.BaseObjectSpace.Disposed
name: Disposed
type: Event
summary: Occurs before an Object Space is disposed of.
syntax:
  content: public event EventHandler Disposed
seealso: []
---
This event is raised as a result of calling the [BaseObjectSpace.Dispose](xref:DevExpress.ExpressApp.BaseObjectSpace.Dispose) method. This method releases all resources allocated by the ObjectSpace and speeds up system performance. Handle this event to release custom resources before the current Object Space is disposed of.