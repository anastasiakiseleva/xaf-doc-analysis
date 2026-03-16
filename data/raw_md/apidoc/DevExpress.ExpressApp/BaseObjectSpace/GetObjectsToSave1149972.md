---
uid: DevExpress.ExpressApp.BaseObjectSpace.GetObjectsToSave(System.Boolean)
name: GetObjectsToSave(Boolean)
type: Method
summary: Returns a collection of persistent objects that will be saved when the current transaction is committed, including objects that will be saved in the parent transaction(s), optionally.
syntax:
  content: public virtual ICollection GetObjectsToSave(bool includeParent)
  parameters:
  - id: includeParent
    type: System.Boolean
    description: '**true**, to include persistent objects that will be saved in the parent transaction(s); otherwise, **false**.'
  return:
    type: System.Collections.ICollection
    description: The collection of persistent objects that will be saved when the current transaction is committed.
seealso: []
---
