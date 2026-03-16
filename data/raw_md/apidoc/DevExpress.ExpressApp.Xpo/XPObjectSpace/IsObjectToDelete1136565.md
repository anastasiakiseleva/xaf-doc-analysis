---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsObjectToDelete(System.Object)
name: IsObjectToDelete(Object)
type: Method
summary: Indicates whether the specified object has been deleted but not committed in the transaction currently in progress.
syntax:
  content: public override bool IsObjectToDelete(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: The persistent object to test.
  return:
    type: System.Boolean
    description: '**true**, if the specified object is marked as deleted in the transaction currently in progress; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectsToDelete(System.Boolean)
---
This method passes the request to the [Session.IsObjectToDelete](xref:DevExpress.Xpo.Session.IsObjectToDelete*) method and returns its value.

To learn more, see [Deleting Persistent Objects](xref:2026).