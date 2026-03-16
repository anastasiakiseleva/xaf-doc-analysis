---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpaceProvider.CreateObjectSpace
name: CreateObjectSpace()
type: Method
summary: Instantiates an Object Space.
syntax:
  content: public IObjectSpace CreateObjectSpace()
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object that is the instantiated Object Space.
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CreateObjectSpace*
---
If you implement a custom @DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider with the `CreateObjectSpace` method overridden, make sure this method returns an object of the @DevExpress.ExpressApp.Security.SecuredXPObjectSpace type instead of @DevExpress.ExpressApp.Xpo.XPObjectSpace.