---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsObjectToSave(System.Object)
name: IsObjectToSave(Object)
type: Method
summary: Indicates whether the specified object has been added, deleted or modified, but not committed in the current object context or the transaction currently in progress.
syntax:
  content: public virtual bool IsObjectToSave(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object for which it is requested whether it should be saved.
  return:
    type: System.Boolean
    description: '**true**, if the specified object has been added, deleted or modified, but not committed; otherwise, **false**.'
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns false, but this behavior is overridden in descendants (see [EFCoreObjectSpace.IsObjectToSave](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsObjectToSave(System.Object)) and [XPObjectSpace.IsObjectToSave](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsObjectToSave(System.Object))).