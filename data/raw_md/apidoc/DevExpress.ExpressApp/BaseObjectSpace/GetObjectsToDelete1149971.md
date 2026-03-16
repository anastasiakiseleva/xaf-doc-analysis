---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectsToDelete(System.Boolean)
name: GetObjectsToDelete(Boolean)
type: Method
summary: Returns a collection of persistent objects that will be deleted when the current transaction is committed, including objects that will be deleted in the parent transaction(s), optionally.
syntax:
  content: public virtual ICollection GetObjectsToDelete(bool includeParent)
  parameters:
  - id: includeParent
    type: System.Boolean
    description: '**true**, to include persistent objects that will be deleted in the parent transaction(s); otherwise, **false**.'
  return:
    type: System.Collections.ICollection
    description: The collection of persistent objects that will be deleted when the current transaction is committed.
seealso: []
---
Generally, you do not need to use this method, since it is intended for internal use.