---
uid: DevExpress.ExpressApp.BaseObjectSpace.ObjectSaved
name: ObjectSaved
type: Event
summary: Occurs after saving changes made to a specified persistent object to the database.
syntax:
  content: public event EventHandler<ObjectManipulatingEventArgs> ObjectSaved
seealso: []
---
The **ObjectSaved** event is supposed to be raised by the **BaseObjectSpace** class' descendants after saving changes made to the object passed as the handler's **ObjectManipulationEventArgs.Object** parameter. The object changes are the ones made after the previous call of the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method.