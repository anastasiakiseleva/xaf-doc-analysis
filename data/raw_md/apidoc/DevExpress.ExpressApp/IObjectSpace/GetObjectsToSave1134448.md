---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectsToSave(System.Boolean)
name: GetObjectsToSave(Boolean)
type: Method
summary: Returns a collection of persistent objects that will be saved when the current transaction is committed, including objects that will be saved in the parent transaction(s), optionally.
syntax:
  content: ICollection GetObjectsToSave(bool includeParent)
  parameters:
  - id: includeParent
    type: System.Boolean
    description: '**true**, to include persistent objects that will be saved in the parent transaction(s); otherwise, **false**.'
  return:
    type: System.Collections.ICollection
    description: The collection of persistent objects that will be saved when the current transaction is committed.
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.GetObjectsToSave(System.Boolean)
  altText: EFCoreObjectSpace.GetObjectsToSave(Boolean)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectsToSave(System.Boolean)
  altText: XPObjectSpace.GetObjectsToSave(Boolean)
---
When you create, modify or delete an object, you should then call the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method. This method saves all the changes made to the current Object Space's persistent objects to the database. To get the list of objects to be committed, use the [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) property. After calling the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method, this list is empty until creating, modifying or deleting an object.