---
uid: DevExpress.ExpressApp.Frame.Disposed
name: Disposed
type: Event
summary: Occures after the current [](xref:DevExpress.ExpressApp.Frame) has been disposed of.
syntax:
  content: public event EventHandler Disposed
seealso: []
---
This event is raised as a result of calling the [Frame.Dispose](xref:DevExpress.ExpressApp.Frame.Dispose) method. This method releases all resources allocated by the current [](xref:DevExpress.ExpressApp.Frame) and speeds up system performance. Handle this event to release custom resources after the [](xref:DevExpress.ExpressApp.Frame) has been disposed of.