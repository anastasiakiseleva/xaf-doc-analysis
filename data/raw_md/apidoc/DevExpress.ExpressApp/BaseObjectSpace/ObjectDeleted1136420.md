---
uid: DevExpress.ExpressApp.BaseObjectSpace.ObjectDeleted
name: ObjectDeleted
type: Event
summary: Occurs after the specified objects have been deleted.
syntax:
  content: public event EventHandler<ObjectsManipulatingEventArgs> ObjectDeleted
seealso: []
---
The **ObjectDeleted** event is supposed to be raised by the **BaseObjectSpace** class' descendants after marking objects as deleted (see [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*)). Use the handler's **ObjectsManipulatingEventArgs.Objects** parameter to get the deleted object(s).