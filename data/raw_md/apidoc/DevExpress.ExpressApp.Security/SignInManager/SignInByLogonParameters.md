---
uid: DevExpress.ExpressApp.Security.SignInManager.SignInByLogonParameters(System.Object)
name: SignInByLogonParameters(Object)
type: Method
summary: Signs in a user based on the specified user logon parameters.
syntax:
  content: public AuthenticationResult SignInByLogonParameters(object logonParameters)
  parameters:
  - id: logonParameters
    type: System.Object
    description: An object that contains a user's logon parameters.
  return:
    type: DevExpress.ExpressApp.Security.AuthenticationResult
    description: An object of the `AuthenticationResult` type that contains the result of an authentication attempt.
seealso: []
---

Use this method to programmatically sign a user into an XAF application. This method takes an object that contains a user's logon parameters and returns an `AuthenticationResult` object.

[!include[signin-manager-authentication-result-description](~/templates/signin-manager-authentication-result-description.md)]

The following code snippet demonstrates how to use the `SignInByLogonParameters` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var signInManager = serviceProvider.GetRequiredService<SignInManager>();
var authResult = signInManager.SignInByLogonParameters(new AuthenticationStandardLogonParameters("User", "Password"));
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider

## Usage Considerations

- The `SignInByLogonParameters` method differs from the [AuthenticateByLogonParameters](xref:DevExpress.ExpressApp.Security.SignInManager.AuthenticateByLogonParameters(System.Object)) method in the following ways:
  * The `AuthenticateByLogonParameters` method only uses the passed logon parameters to find a user. This method does not affect the currently logged in user.
  * The `SignInByLogonParameters` method implicitly calls the `AuthenticateByLogonParameters` method to find a user. If the user is found, `SignInByLogonParameters` signs in this user.

[!include[signin-manager-signin-method-usage-considerations](~/templates/signin-manager-signin-method-usage-considerations.md)]