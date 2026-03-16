---
uid: DevExpress.ExpressApp.Security.AuthenticationStandard.Authenticate(DevExpress.ExpressApp.IObjectSpace)
name: Authenticate(IObjectSpace)
type: Method
summary: Returns an authenticated user.
syntax:
  content: public override object Authenticate(IObjectSpace objectSpace)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object which is an object space used to find a user by logon parameters.
  return:
    type: System.Object
    description: An object which is the authenticated user.
seealso: []
---
This method attempts to find a user object by the [AuthenticationStandard.LogonParameters](xref:DevExpress.ExpressApp.Security.AuthenticationStandard.LogonParameters) value and to compare the  user's stored password with a password specified in logon parameters. On success, returns the found user object; otherwise - throws an authentication exception.