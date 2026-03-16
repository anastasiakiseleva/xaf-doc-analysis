---
uid: DevExpress.ExpressApp.Security.Authentication.WindowsActiveDirectoryAuthenticationProviderEvents.OnCustomizeClaims
name: OnCustomizeClaims
type: Property
summary: Specifies a delegate method that allows you to customize the set of claims added to the authentication cookie.
syntax:
  content: public Action<WindowsPrincipalCustomizeClaimContext> OnCustomizeClaims { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Security.WindowsPrincipalCustomizeClaimContext}
    description: A delegate method that takes a context object as an argument.
seealso:
- linkId: "404462"
---

Use this property in an ASP.NET Core Blazor application to customize claims added to the authentication cookie when Active Directory authentication is used as an optional authentication method.

> [!NOTE]
> When Active Directory authentication is used as the default authentication method, the client passes user identity information to the server with each request. In this instance, an authentication cookie is not used, so the `OnCustomizeClaims` delegate method is never called.

The specified delegate method is called after the user authentication succeeds and before the authentication cookie is issued. In the delegate method, you can customize the list of claims added to the cookie. You can also access the principal object and copy the required claims from it.

To keep the cookie small, only the claims of the following types are copied from the principal object (the default setting):

- `ClaimTypes.Name`
- `ClaimTypes.NameIdentifier`

The code sample below demonstrates how to add a claim of the `ClaimTypes.PrimaryGroupSid` type to the authentication cookie.

**File:** _MySolution.WebApi\startup.cs_ (_MySolution.Blazor.Server\startup.cs_)

# [C#](#tab/tabid-csharp-1)

```csharp{8-11}
using System.Security.Claims;
// ...
services.AddXaf(Configuration, builder => {
    // ...
    builder.Security
        .AddWindowsAuthentication(options => {
            options.CreateUserAutomatically();
            options.Events.OnCustomizeClaims = context => {
                Claim primaryGroupSid = context.Principal.Claims.First(claim => claim.Type == ClaimTypes.PrimaryGroupSid);
                context.Claims.Add(primaryGroupSid);
            };
        });
        // ...
});
```
***

## Access Claims

[!include[](~/templates/authentication-access-claims.md)]
