---
uid: DevExpress.ExpressApp.XafApplication.CreateObjectSpace
name: CreateObjectSpace()
type: Method
summary: Creates an [Object Space](xref:113707). Use this method overload if your application registers only one @DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider.
syntax:
  content: |-
    [Browsable(false)]
    public IObjectSpace CreateObjectSpace()
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the created Object Space.
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace
---

We recommend to use the @DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type) overload in most cases.