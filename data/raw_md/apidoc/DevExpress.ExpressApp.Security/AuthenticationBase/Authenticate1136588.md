---
uid: DevExpress.ExpressApp.Security.AuthenticationBase.Authenticate(DevExpress.ExpressApp.IObjectSpace)
name: Authenticate(IObjectSpace)
type: Method
summary: Authenticates a user trying to find the corresponding user object by comparing logon parameter values with the information stored in the database.
syntax:
  content: public virtual object Authenticate(IObjectSpace objectSpace)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) Object Space used for data manipulation.
  return:
    type: System.Object
    description: An object which is an authenticated user.
seealso: []
---
When implementing a custom authentication, override this method.
