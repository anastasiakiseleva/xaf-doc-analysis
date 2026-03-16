---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsDeletedObject(System.Object)
name: IsDeletedObject(Object)
type: Method
summary: Indicates whether the specified persistent object is deleted.
syntax:
  content: public override bool IsDeletedObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The object to test.
  return:
    type: System.Boolean
    description: '**true** if the specified object is marked as deleted; otherwise, **false**.'
seealso: []
---
This method passes the request to the [Session.IsObjectMarkedDeleted](xref:DevExpress.Xpo.Session.IsObjectMarkedDeleted(System.Object)) method and returns its value.

To learn more, see [Deferred and Immediate Object Deletion](xref:2026).