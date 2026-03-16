---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.ModifiedObjects
name: ModifiedObjects
type: Property
summary: Returns a collection of objects that have been created, modified or deleted after they were retrieved or committed.
syntax:
  content: public override IList ModifiedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: An **IList** collection that contains the modified objects belonging to the current Object Space.
seealso: []
---
When you create, modify or delete an object, you should then call the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method. This method saves all the changes made to the current Object Space's persistent objects to the database. To get the list of objects to be committed, use the **ModifiedObjects** property. After calling the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method this list is empty until creating, modifying or deleting an object.