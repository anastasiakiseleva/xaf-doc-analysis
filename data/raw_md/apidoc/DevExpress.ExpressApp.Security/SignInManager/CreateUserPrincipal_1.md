---
uid: DevExpress.ExpressApp.Security.SignInManager.CreateUserPrincipal(DevExpress.ExpressApp.Security.ISecurityUser,System.Collections.Generic.IEnumerable{System.Security.Claims.Claim})
name: CreateUserPrincipal(ISecurityUser, IEnumerable<Claim>)
type: Method
summary: Creates a @System.Security.Claims.ClaimsPrincipal object for the specified user.
syntax:
  content: public ClaimsPrincipal CreateUserPrincipal(ISecurityUser user, IEnumerable<Claim> additionalClaims = null)
  parameters:
  - id: user
    type: DevExpress.ExpressApp.Security.ISecurityUser
    description: An XAF Security System user.
  - id: additionalClaims
    type: System.Collections.Generic.IEnumerable{System.Security.Claims.Claim}
    defaultValue: "null"
    description: A list of additional claims to add to the created @System.Security.Claims.ClaimsPrincipal.
  return:
    type: System.Security.Claims.ClaimsPrincipal
    description: A @System.Security.Claims.ClaimsPrincipal object that is a collection of statements (claims) about the specified user within the Security System.
seealso: []
---

The following code snippet demonstrates how to use the `CreateUserPrincipal` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var signInManager = serviceProvider.GetRequiredService<SignInManager>();
var principal = signInManager.CreateUserPrincipal(user);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider