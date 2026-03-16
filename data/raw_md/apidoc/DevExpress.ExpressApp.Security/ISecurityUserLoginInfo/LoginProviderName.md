---
uid: DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.LoginProviderName
name: LoginProviderName
type: Property
summary: Specifies the authentication type name.
syntax:
  content: string LoginProviderName { get; }
  parameters: []
  return:
    type: System.String
    description: The type name.
seealso: []
---
Use the following values for different authentication types:

Windows Active Directory
:   'Windows'
OAuth
:   The System.Security.Principal.IIdentity.AuthenticationType property value
Standard Authentication
:   'Password'

The `LoginProviderName` and @DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.ProviderUserKey form a unique combination. The @DevExpress.ExpressApp.Security.ISecurityUserLoginInfo.ProviderUserKey is not necessarily unique among all providers but is always unique for a specific provider.
