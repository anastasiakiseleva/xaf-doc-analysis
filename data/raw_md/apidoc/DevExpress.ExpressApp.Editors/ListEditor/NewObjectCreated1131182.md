---
uid: DevExpress.ExpressApp.Editors.ListEditor.NewObjectCreated
name: NewObjectCreated
type: Event
summary: Occurs after a new object has been created in a [List Editor](xref:113189).
syntax:
  content: public event EventHandler NewObjectCreated
seealso: []
---
This event occurs only in those List Editors whose controls support creation of new objects and supply the required event notification. For instance, the built-in **GridListEditor** supports this event because its **XtraGrid** control can display the [new item row](xref:752).

When deriving from the **ListEditor** class, raise this event after a new object is created in a List Editor's control.
In addition, the [ListEditor.NewObjectAdding](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectAdding) and [ListEditor.NewObjectCanceled](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectCanceled) events should be raised where appropriate.
In this instance, the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) will correctly create and manage a business object of the required type.