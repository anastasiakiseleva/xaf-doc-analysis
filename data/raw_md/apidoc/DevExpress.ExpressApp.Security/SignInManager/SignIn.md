---
uid: DevExpress.ExpressApp.Security.SignInManager.SignIn(DevExpress.ExpressApp.Security.ISecurityUser)
name: SignIn(ISecurityUser)
type: Method
summary: Signs in the specified user.
syntax:
  content: public AuthenticationResult SignIn(ISecurityUser user)
  parameters:
  - id: user
    type: DevExpress.ExpressApp.Security.ISecurityUser
    description: An [XAF Security System](xref:113366) user.
  return:
    type: DevExpress.ExpressApp.Security.AuthenticationResult
    description: An object of the `AuthenticationResult` type that contains the result of an authentication attempt.
seealso: []
---

Use this method to programmatically sign a user into an XAF application. This method takes an object that contains a user's logon parameters and returns an `AuthenticationResult` object.

[!include[signin-manager-authentication-result-description](~/templates/signin-manager-authentication-result-description.md)]

## Usage Considerations

[!include[signin-manager-signin-method-usage-considerations](~/templates/signin-manager-signin-method-usage-considerations.md)]

## Example

The following code snippet demonstrates how to use the `SignIn` method to sign into a nested scope and execute an action on a service user's behalf (user impersonation):

[!include[signinmanager-impersonation-example](~/templates/signinmanager-impersonation-example.md)]