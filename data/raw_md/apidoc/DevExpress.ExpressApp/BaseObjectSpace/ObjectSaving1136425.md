---
uid: DevExpress.ExpressApp.BaseObjectSpace.ObjectSaving
name: ObjectSaving
type: Event
summary: Raised before saving changes made to a specified persistent object to the database.
syntax:
  content: public event EventHandler<ObjectManipulatingEventArgs> ObjectSaving
seealso: []
---
The **ObjectSaving** event is supposed to be raised by the **BaseObjectSpace** class' descendants before saving changes made to the object passed as the handler's **ObjectManipulationEventArgs.Object** parameter. The object changes are the ones made after the last call of the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method.