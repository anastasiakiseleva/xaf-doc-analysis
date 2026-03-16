---
uid: DevExpress.ExpressApp.IObjectSpace.IsObjectToSave(System.Object)
name: IsObjectToSave(Object)
type: Method
summary: Indicates whether the specified object has been added, deleted or modified, but not committed in the transaction currently in progress.
syntax:
  content: bool IsObjectToSave(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object for which it has been requested whether it should be saved.
  return:
    type: System.Boolean
    description: '**true**, if the specified object has been added, deleted or modified and should be committed; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.GetObjectsToSave(System.Boolean)
  altText: IObjectSpace.GetObjectsToSave(Boolean)
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsObjectToSave(System.Object)
  altText: EFCoreObjectSpace.IsObjectToSave(Object)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsObjectToSave(System.Object)
  altText: XPObjectSpace.IsObjectToSave(Object)
---
When you create, modify or delete an object, you should then call the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method. This method saves all the changes made to the current Object Space's persistent objects to the database. To get the list of objects to be committed, use the [EFCoreObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ModifiedObjects) property. After calling the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method, this list is empty until creating, modifying or deleting an object. The **IsObjectToSave** property is intended for determining whether a particular object should be committed in the transaction currently in progress.