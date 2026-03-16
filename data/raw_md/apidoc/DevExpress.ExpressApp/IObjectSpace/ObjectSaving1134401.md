---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectSaving
name: ObjectSaving
type: Event
summary: Occurs before saving changes made to a specified persistent object to the database.
syntax:
  content: event EventHandler<ObjectManipulatingEventArgs> ObjectSaving
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.Committed
- linkId: DevExpress.ExpressApp.IObjectSpace.Committing
- linkId: DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaving
---
Raise this event before saving changes made to the object passed as the handler's **ObjectManipulationEventArgs.Object** parameter.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to declare this event. It's declared within the **BaseObjectSpace class**. The **BaseObjectSpace.OnObjectSaving** method raises this event. So, you should only invoke the **OnObjectSaving** method before an object is saved.

> [!NOTE]
> The object changes which are about to be saved to the database are the changes made after the last call of the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method.