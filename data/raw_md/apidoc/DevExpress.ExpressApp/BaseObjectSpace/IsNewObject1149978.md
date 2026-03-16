---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsNewObject(System.Object)
name: IsNewObject(Object)
type: Method
summary: Indicates whether a specified object has been created but has not been saved to the database.
syntax:
  content: public virtual bool IsNewObject(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: A object to be tested.
  return:
    type: System.Boolean
    description: '**true** if the specified object has not been yet saved to the database; otherwise, **false**.'
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns false, but this behavior is overridden in descendants (see [EFCoreObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsNewObject(System.Object)) and [XPObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsNewObject(System.Object))).