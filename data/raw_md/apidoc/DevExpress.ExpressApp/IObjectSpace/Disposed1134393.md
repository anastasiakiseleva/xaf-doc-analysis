---
uid: DevExpress.ExpressApp.IObjectSpace.Disposed
name: Disposed
type: Event
summary: Occurs after an Object Space has been disposed of.
syntax:
  content: event EventHandler Disposed
seealso: []
---
If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to raise this event, since it's raised by the [BaseObjectSpace.Dispose](xref:DevExpress.ExpressApp.BaseObjectSpace.Dispose) method. This method releases all resources allocated by the ObjectSpace and speeds up system performance. Handle this event to release custom resources before the current Object Space is disposed of.