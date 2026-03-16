---
uid: DevExpress.ExpressApp.IObjectSpace.IsDeletedObject(System.Object)
name: IsDeletedObject(Object)
type: Method
summary: Indicates whether the specified persistent object is deleted and committed.
syntax:
  content: bool IsDeletedObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The object to test.
  return:
    type: System.Boolean
    description: '**true** if the specified object is deleted; otherwise, **false**.'
seealso: []
---
When an object is deleted, it's not deleted immediately from the database. It's marked as an object to delete and removed from the database the next time the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method is called.

The **IsDeletedObject** method is intended to determine whether a particular object is deleted and this is committed.