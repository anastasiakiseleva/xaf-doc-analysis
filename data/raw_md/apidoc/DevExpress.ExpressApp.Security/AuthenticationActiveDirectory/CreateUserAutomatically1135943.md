---
uid: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically
name: CreateUserAutomatically
type: Property
summary: Specifies whether a user is created automatically for the Windows account used to run the application.
syntax:
  content: public bool CreateUserAutomatically { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, to create a user for the current Windows account automatically; otherwise, `false`.'
seealso: []
---
If your XAF application is created through the standard wizard, call the @DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions.CreateUserAutomatically* method in the application builder code to create a user for the current Windows account automatically. If you create an application with the [Template Kit](xref:405447) and enables the Windows authentication (the **Active Directory (uses Windows account)** option), the kit adds the @DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions.CreateUserAutomatically* method call in the _Startup.cs_ file.