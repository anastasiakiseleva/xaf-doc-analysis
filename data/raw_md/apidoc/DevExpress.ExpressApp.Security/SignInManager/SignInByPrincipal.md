---
uid: DevExpress.ExpressApp.Security.SignInManager.SignInByPrincipal(System.Security.Claims.ClaimsPrincipal)
name: SignInByPrincipal(ClaimsPrincipal)
type: Method
summary: Signs in a user based on the specified claims principal.
syntax:
  content: public AuthenticationResult SignInByPrincipal(ClaimsPrincipal claimsPrincipal)
  parameters:
  - id: claimsPrincipal
    type: System.Security.Claims.ClaimsPrincipal
    description: A @System.Security.Claims.ClaimsPrincipal object.
  return:
    type: DevExpress.ExpressApp.Security.AuthenticationResult
    description: An object of the `AuthenticationResult` type that contains the result of an authentication attempt.
seealso: []
---

Use this method to programmatically sign a user into an XAF application. This method takes an object that contains a user's logon parameters and returns an `AuthenticationResult` object.

[!include[signin-manager-authentication-result-description](~/templates/signin-manager-authentication-result-description.md)]

The following code snippet demonstrates how to use the `SignInByPrincipal` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var signInManager = serviceProvider.GetRequiredService<SignInManager>();
var principal = signInManager.CreateUserPrincipal(user);
var authResult = signInManager.SignInByPrincipal(principal);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider


## Usage Considerations

[!include[signin-manager-signin-method-usage-considerations](~/templates/signin-manager-signin-method-usage-considerations.md)]