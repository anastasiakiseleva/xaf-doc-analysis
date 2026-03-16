---
uid: DevExpress.ExpressApp.Security.ISecurityUserWithLoginInfo.CreateUserLoginInfo(System.String,System.String)
name: CreateUserLoginInfo(String, String)
type: Method
summary: Allows the XAF framework to create a `UserLoginInfo` instance.
syntax:
  content: ISecurityUserLoginInfo CreateUserLoginInfo(string loginProviderName, string providerUserKey)
  parameters:
  - id: loginProviderName
    type: System.String
    description: The authentication type name.
  - id: providerUserKey
    type: System.String
    description: The user ID.
  return:
    type: DevExpress.ExpressApp.Security.ISecurityUserLoginInfo
    description: Login information.
seealso: []
---
[!include[<ISecurityUserWithLoginInfo>](~/templates/isecurity-example.md)]
