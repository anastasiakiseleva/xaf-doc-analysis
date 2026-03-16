---
uid: DevExpress.ExpressApp.Frame.Disposing
name: Disposing
type: Event
summary: Occurs when the current [](xref:DevExpress.ExpressApp.Frame) is disposed of.
syntax:
  content: public event EventHandler Disposing
seealso: []
---
This event is raised before calling the [Frame.Dispose](xref:DevExpress.ExpressApp.Frame.Dispose) method. This method releases all resources allocated by the current [](xref:DevExpress.ExpressApp.Frame) and speeds up system performance. Handle this event to release custom resources before disposing of the [](xref:DevExpress.ExpressApp.Frame) .