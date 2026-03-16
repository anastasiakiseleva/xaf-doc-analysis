---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectDeleting
name: ObjectDeleting
type: Event
summary: Occurs when the specified objects are about to be deleted.
syntax:
  content: event EventHandler<ObjectsManipulatingEventArgs> ObjectDeleting
seealso: []
---
Raise this event before objects are marked as deleted from a dataset (see [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*)). Use the handler's **ObjectsManipulatingEventArgs.Objects** parameter to get the object(s) to be deleted.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to declare this event. It's declared within the **BaseObjectSpace class**. In addition, the **BaseObjectSpace.OnObjectDeleting** method raises this event. So, you should only invoke the **OnObjectDeleting** method before objects are marked as deleted.