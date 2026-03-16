---
uid: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.Authenticate(DevExpress.ExpressApp.IObjectSpace)
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
The [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication uses the [WindowsIdentity.Name](https://learn.microsoft.com/en-us/dotnet/api/system.security.principal.windowsidentity.name#System_Security_Principal_WindowsIdentity_Name) property of an object obtained via the static [WindowsIdentity.GetCurrent](https://learn.microsoft.com/en-us/dotnet/api/system.security.principal.windowsidentity.getcurrent#System_Security_Principal_WindowsIdentity_GetCurrent) method to get a user name in the _DOMAIN\USERNAME_ format. This string is used to find a persisted object of the [AuthenticationActiveDirectory.UserType](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.UserType) with the matching [ISecurityUser.UserName](xref:DevExpress.ExpressApp.Security.ISecurityUser.UserName) value (the [IObjectSpace.FindObject](xref:DevExpress.ExpressApp.IObjectSpace.FindObject*) method is used internally). If a matching user object is not found and the [AuthenticationActiveDirectory.CreateUserAutomatically](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically) property is set to true, a new use object is created. Additionally, the [AuthenticationActiveDirectory.CustomCreateUser](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CustomCreateUser) event is raised. If this event is not handled or its **Handled** parameter is _false_, the new user of the [AuthenticationActiveDirectory.UserType](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.UserType) type is created via the [IObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) method. The created object should support the [](xref:DevExpress.Persistent.Base.Security.IAuthenticationActiveDirectoryUser) interface. The [IAuthenticationActiveDirectoryUser.UserName](xref:DevExpress.Persistent.Base.Security.IAuthenticationActiveDirectoryUser.UserName) property is used to pass a user name. These changes are immediately committed via the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges).
