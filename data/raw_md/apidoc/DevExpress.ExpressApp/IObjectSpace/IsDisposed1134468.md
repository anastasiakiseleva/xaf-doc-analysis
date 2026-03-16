---
uid: DevExpress.ExpressApp.IObjectSpace.IsDisposed
name: IsDisposed
type: Property
summary: Gets a value indicating whether an Object Space has been disposed of.
syntax:
  content: bool IsDisposed { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the current Object Space has been disposed of; otherwise, **false**.'
seealso: []
---
If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, the **IsDisposed** property is already implemented (see [BaseObjectSpace.IsDisposed](xref:DevExpress.ExpressApp.BaseObjectSpace.IsDisposed)). However, you should override the [BaseObjectSpace.Dispose](xref:DevExpress.ExpressApp.BaseObjectSpace.Dispose) method to set the **IsDisposed** property to **true** and release the resources allocated by the current Object Space. For instance, the container for in-memory objects ([XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) in the case of an [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) or [EFCoreObjectSpace.DbContext](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.DbContext) in the case of the [](xref:DevExpress.ExpressApp.EFCore.EFCoreObjectSpace)), [Types Info](xref:113669) and Type Info Source must be disposed of.