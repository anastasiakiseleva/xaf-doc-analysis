---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectEndEdit
name: ObjectEndEdit
type: Event
summary: Occurs after ending an edit operation taking place on the specified object.
syntax:
  content: event EventHandler<ObjectManipulatingEventArgs> ObjectEndEdit
seealso: []
---
If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to declare this event. It's declared within the **BaseObjectSpace class**. The **BaseObjectSpace.OnObjectEndEdit** method raises this event. So, you should only invoke the **OnObjectEndEdit** method in your descendant.