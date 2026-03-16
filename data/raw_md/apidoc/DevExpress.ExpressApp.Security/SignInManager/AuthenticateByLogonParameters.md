---
uid: DevExpress.ExpressApp.Security.SignInManager.AuthenticateByLogonParameters(System.Object)
name: AuthenticateByLogonParameters(Object)
type: Method
summary: Authenticates a user based on the specified logon parameters.
syntax:
  content: public AuthenticationResult AuthenticateByLogonParameters(object logonParameters)
  parameters:
  - id: logonParameters
    type: System.Object
    description: An object that contains a user's logon parameters.
  return:
    type: DevExpress.ExpressApp.Security.AuthenticationResult
    description: An object of the `AuthenticationResult` type that contains the result of an authentication attempt.
seealso: []
---

Use this method to programmatically authenticate a user in an XAF application. This method takes an object that contains a user's logon parameters and returns an `AuthenticationResult` object. 

[!include[signin-manager-authentication-result-description](~/templates/signin-manager-authentication-result-description.md)]

## Example

The code sample below demonstrates how you can use the `AuthenticateByLogonParameters` method to implement a [Backend Web API Service](xref:403394) controller for JSON Web Token (JWT)-based authentication. The [Template Kit](xref:405447) generates equivalent code for Blazor projects with integrated Web API.

[!include[sign-in-manager-example](~/templates/sign-in-manager-example.md)]

## Usage Considerations

- The `AuthenticateByLogonParameters` method differs from the [SignInByLogonParameters](xref:DevExpress.ExpressApp.Security.SignInManager.SignInByLogonParameters(System.Object)) method in the following ways:
  * The `AuthenticateByLogonParameters` method only uses the passed logon parameters to find a user. This method does not affect the currently logged in user.
  * The `SignInByLogonParameters` method implicitly calls the `AuthenticateByLogonParameters` method to find a user. If the user is found, `SignInByLogonParameters` signs in this user.