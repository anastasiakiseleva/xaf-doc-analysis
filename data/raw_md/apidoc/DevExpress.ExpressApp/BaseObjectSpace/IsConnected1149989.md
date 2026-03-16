---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsConnected
name: IsConnected
type: Property
summary: Indicates whether the [](xref:DevExpress.ExpressApp.BaseObjectSpace) is connected to the database.
syntax:
  content: public virtual bool IsConnected { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the [](xref:DevExpress.ExpressApp.BaseObjectSpace) is connected to the database; otherwise, **false**.'
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns true, but this behavior is overridden in descendants (see [EFCoreObjectSpace.IsConnected](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.IsConnected) and [XPObjectSpace.IsConnected](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsConnected)).