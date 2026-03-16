---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace.IsObjectToSave(System.Object)
name: IsObjectToSave(Object)
type: Method
summary: Indicates whether the specified object has been added, deleted or modified, but not committed in the transaction currently in progress.
syntax:
  content: public override bool IsObjectToSave(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object for which it is requested whether it should be saved.
  return:
    type: System.Boolean
    description: '**true**, if the specified object has been added, deleted or modified, but not committed; otherwise, **false**.'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.GetObjectsToSave(System.Boolean)
---
Generally, you do not need to use this method, since it is intended for internal use.