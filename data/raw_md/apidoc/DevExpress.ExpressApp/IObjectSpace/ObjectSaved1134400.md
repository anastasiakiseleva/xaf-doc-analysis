---
uid: DevExpress.ExpressApp.IObjectSpace.ObjectSaved
name: ObjectSaved
type: Event
summary: Occurs after saving changes made to a specified persistent object to the database.
syntax:
  content: event EventHandler<ObjectManipulatingEventArgs> ObjectSaved
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.Committed
- linkId: DevExpress.ExpressApp.IObjectSpace.Committing
- linkId: DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaving
---
Raise this event after saving changes made to the object passed as the handler's **ObjectManipulationEventArgs.Object** parameter.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to declare this event. It's declared within the **BaseObjectSpace class**. The **BaseObjectSpace.OnObjectSaved** method raises this event. So, you should only invoke the **OnObjectSaved** method after an object is saved.

> [!NOTE]
> The object changes which have been saved to the database are the changes made after the previous call of the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method.