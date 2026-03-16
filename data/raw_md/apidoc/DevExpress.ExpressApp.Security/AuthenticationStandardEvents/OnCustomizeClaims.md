---
uid: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnCustomizeClaims
name: OnCustomizeClaims
type: Property
summary: Specifies a delegate method that allows you to customize the set of claims added to the authentication cookie.
syntax:
  content: public Action<CustomizeClaimContext> OnCustomizeClaims { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Security.CustomizeClaimContext}
    description: A delegate method that takes a context object as an argument.
seealso:
- linkId: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnCustomizeLoginToken
- linkId: "404462"
---

Use this property in an ASP.NET Core Blazor application to customize a logged-in user's claims. The specified delegate method is called after the user authentication succeeds and before the authentication cookie is issued. 

Normally, claims are copied from the login token to the user's authentication cookie. The `OnCustomizeClaims` property allows you to intercept this process and change the existing claims or add additional ones. The list of claims is available through the `conext.Claims` object. 

**Example:**

**File:** _MySolution.WebApi\startup.cs_ (_MySolution.Blazor.Server\startup.cs_)

# [C#](#tab/tabid-csharp-1)

```csharp{6-8}
services.AddXaf(Configuration, builder => {
    // ...
    builder.Security
        .AddPasswordAuthentication(options => {
            options.IsSupportChangePassword = true;
            options.Events.OnCustomizeClaims = context => {
                context.Claims.Add(new Claim("CustomClaim", "ClaimValue"));
            };
        });
        // ...
});
```
***

## Access Claims

[!include[](~/templates/authentication-access-claims.md)]