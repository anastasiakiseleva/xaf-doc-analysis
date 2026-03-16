---
uid: DevExpress.ExpressApp.BaseObjectSpace.ObjectReloaded
name: ObjectReloaded
type: Event
summary: Occurs after an object has been reloaded from the database.
syntax:
  content: public event EventHandler<ObjectManipulatingEventArgs> ObjectReloaded
seealso: []
---
This event is supposed to be raised by the **BaseObjectSpace** class' descendants. Generally, you do not need to handle this event, since it is intended for internal use.