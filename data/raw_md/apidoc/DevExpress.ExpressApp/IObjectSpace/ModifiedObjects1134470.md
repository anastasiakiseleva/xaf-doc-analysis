---
uid: DevExpress.ExpressApp.IObjectSpace.ModifiedObjects
name: ModifiedObjects
type: Property
summary: Returns a collection of objects that have been created, modified or deleted after they were retrieved or committed.
syntax:
  content: IList ModifiedObjects { get; }
  parameters: []
  return:
    type: System.Collections.IList
    description: An IList collection that contains the modified objects belonging to the current Object Space.
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.ModifiedChanged
  altText: IObjectSpace.ModifiedChanged
- linkId: DevExpress.ExpressApp.IObjectSpace.IsModified
  altText: IObjectSpace.IsModified
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.ModifiedObjects
  altText: EFCoreObjectSpace.ModifiedObjects
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.ModifiedObjects
  altText: XPObjectSpace.ModifiedObjects
---
When you create, modify or delete an object, you should then call the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method. This method saves all the changes made to the current Object Space's persistent objects to the database. The **ModifiedObjects** method is intended  to get the list of objects to be committed. After calling the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method, this list is empty until creating, modifying or deleting an object.

[!include[<32-33><40-41>](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]