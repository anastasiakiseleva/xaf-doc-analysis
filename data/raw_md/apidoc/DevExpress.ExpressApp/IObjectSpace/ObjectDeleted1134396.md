---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectDeleted
name: ObjectDeleted
type: Event
summary: Occurs after the specified objects have been deleted from the dataset.
syntax:
  content: event EventHandler<ObjectsManipulatingEventArgs> ObjectDeleted
seealso: []
---
Raise this event after the specified objects are deleted from a dataset (see [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*)). Use the handler's **ObjectsManipulatingEventArgs.Objects** parameter to get the object(s) to be deleted.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you don't have to declare this event. It's declared within the **BaseObjectSpace class**. In addition, the **BaseObjectSpace.OnObjectDeleted** method raises this event. So, you should only invoke the **OnObjectDeleted** method after objects are deleted.