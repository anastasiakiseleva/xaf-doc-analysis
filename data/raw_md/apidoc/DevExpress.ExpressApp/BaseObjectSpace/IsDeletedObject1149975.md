---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsDeletedObject(System.Object)
name: IsDeletedObject(Object)
type: Method
summary: Indicates whether the specified persistent object is deleted from the database.
syntax:
  content: public virtual bool IsDeletedObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The object to test.
  return:
    type: System.Boolean
    description: '**true** if the specified object is marked as deleted; otherwise, **false**.'
seealso: []
---
When an object is deleted, it's not deleted immediately from the database. It's marked as an object to delete and removed from the database the next time the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method is called.

Use the **IsDeletedObject** method to determine whether a particular object is deleted and this is committed to the database.