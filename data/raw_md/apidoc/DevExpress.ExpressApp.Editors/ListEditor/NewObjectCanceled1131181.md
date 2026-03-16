---
uid: DevExpress.ExpressApp.Editors.ListEditor.NewObjectCanceled
name: NewObjectCanceled
type: Event
summary: Occurs after creation of a new object is cancelled in a [List Editor](xref:113189).
syntax:
  content: public event EventHandler NewObjectCanceled
seealso: []
---
Handle this event to perform specific actions when creation of a new object is cancelled.

This event occurs only in those List Editors whose controls support creation of new objects and supply the required event notification. For instance, the built-in **GridListEditor** supports this event because its **XtraGrid** control can display the [new item row](xref:752).

When deriving from the **ListEditor** class, raise this event when creation of a new object is cancelled.
In addition, the [ListEditor.NewObjectAdding](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectAdding) and [ListEditor.NewObjectCreated](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectCreated) events should be raised where appropriate.
In this instance, the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) will correctly create and manage a business object of the required type.