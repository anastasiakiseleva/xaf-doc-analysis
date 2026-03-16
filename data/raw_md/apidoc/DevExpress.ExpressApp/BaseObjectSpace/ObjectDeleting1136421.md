---
uid: DevExpress.ExpressApp.BaseObjectSpace.ObjectDeleting
name: ObjectDeleting
type: Event
summary: Occurs when the specified objects are about to be deleted.
syntax:
  content: public event EventHandler<ObjectsManipulatingEventArgs> ObjectDeleting
seealso: []
---
The **ObjectDeleting** event is supposed to be raised by the **BaseObjectSpace** class' descendants before marking objects as deleted from a dataset (see [BaseObjectSpace.Delete](xref:DevExpress.ExpressApp.BaseObjectSpace.Delete*)). Use the handler's **ObjectsManipulatingEventArgs.Objects** parameter to get the object(s) to be deleted.