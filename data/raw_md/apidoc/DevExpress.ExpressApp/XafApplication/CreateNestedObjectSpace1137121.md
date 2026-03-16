---
uid: DevExpress.ExpressApp.XafApplication.CreateNestedObjectSpace(DevExpress.ExpressApp.IObjectSpace)
name: CreateNestedObjectSpace(IObjectSpace)
type: Method
summary: Creates nested Object Space.
syntax:
  content: public IObjectSpace CreateNestedObjectSpace(IObjectSpace parentObjectSpace)
  parameters:
  - id: parentObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that is a parent Object Space.
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that is a created nested Object Space.
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CreateObjectSpace*
---
This method is intended for creating a nested Object Space - an Object Space that implements the **INestedObjectSpace** interface. For details, refer to the [XPObjectSpace.CreateNestedObjectSpace](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.CreateNestedObjectSpace) method description.