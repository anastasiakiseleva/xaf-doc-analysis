---
uid: DevExpress.ExpressApp.IObjectSpace.IsObjectToDelete(System.Object)
name: IsObjectToDelete(Object)
type: Method
summary: Indicates whether the specified object has been deleted but not committed in the transaction currently in progress.
syntax:
  content: bool IsObjectToDelete(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The persistent object to test.
  return:
    type: System.Boolean
    description: '**true**, if the specified object is marked as deleted in the transaction currently in progress; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.GetObjectsToDelete(System.Boolean)
---
When an object is deleted, it's not deleted immediately from the database. It's marked as an object to delete and removed from the database the next time the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method is called.

The **IsObjectToDelete** method is intended to determine whether a particular object is marked as deleted in the current transaction.