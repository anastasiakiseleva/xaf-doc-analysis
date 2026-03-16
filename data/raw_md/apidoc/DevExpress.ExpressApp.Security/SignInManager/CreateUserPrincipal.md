---
uid: DevExpress.ExpressApp.Security.SignInManager.CreateUserPrincipal(System.String)
name: CreateUserPrincipal(String)
type: Method
summary: Creates a @System.Security.Claims.ClaimsPrincipal object based on a user's authentication token.
syntax:
  content: public AuthenticationResult CreateUserPrincipal(string userToken)
  parameters:
  - id: userToken
    type: System.String
    description: A `string` value that contains a user login token.
  return:
    type: DevExpress.ExpressApp.Security.AuthenticationResult
    description: An object of the `AuthenticationResult` type that contains the result.
seealso: []
---

> [!IMPORTANT]
>
> This overload of the `CreateUserPrincipal` method is not supported on the WinForms platform. If called from a WinForms application, it throws the @System.PlatformNotSupportedException.

Use this method overload to create a @System.Security.Claims.ClaimsPrincipal object for a user based on the user's login token. It returns an `AuthenticationResult` object that exposes the following properties:

`Succeeded`
:   A `boolean` property that indicates whether or not the user was successfully resolved based on the token.
`Principal`
:   If the operation succeeds, this property contains the @System.Security.Claims.ClaimsPrincipal object (a collection of statements about the authenticated user) returned by the Security System.
`Error`
:   If the operation fails, this property contains the resulting @System.Exception.

The following code snippet demonstrates how to use the `CreateUserPrincipal` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var signInManager = serviceProvider.GetRequiredService<SignInManager>();
var principal = signInManager.CreateUserPrincipal(userAuthenticationToken);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider