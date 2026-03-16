---
uid: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnCustomizeLoginToken
name: OnCustomizeLoginToken
type: Property
summary: Specifies a delegate method that allows you to add additional claims to the user login token.
syntax:
  content: public Action<CustomizeLoginTokenContext> OnCustomizeLoginToken { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Security.CustomizeLoginTokenContext}
    description: A delegate method that takes a context object as an argument.
seealso:
- linkId: DevExpress.ExpressApp.Security.AuthenticationStandardEvents.OnCustomizeClaims
- linkId: "404462"
---

Use this property in an ASP.NET Core Blazor application to add additional claims to the login token. The specified delegate method is called before the token is issued and can use the authentication data available at this stage through the `context` argument to modify the claims collection.

For example, you can use this property to implement custom logic that adds logon parameter values to the claims. Consider a usage scenario where your login form has a custom "Company" field. You can use the code below to add the selected company's `Id` value to the claims collection:

**File:** _MySolution.WebApi\startup.cs_ (_MySolution.Blazor.Server\startup.cs_)

# [C#](#tab/tabid-csharp-1)

```csharp{6-12}
services.AddXaf(Configuration, builder => {
    // ...
    builder.Security
        .AddPasswordAuthentication(options => {
            options.IsSupportChangePassword = true;
            options.Events.OnCustomizeLoginToken = context => {
                var logonParameters = (CustomLogonParameters)context.LogonParameters;
                context.Claims.Add(new Claim("CompanyId", logonParameters.Company.Id));
                // If your login form allows a user to select a database,
                // you can also add a "DatabaseId" claim:
                // context.Claims.Add(new Claim("DatabaseId", logonParameters.Database.Id));
            };
        });
        // ...
});
```
***

Refer to the following section for information on how to implement custom logon parameters: [](xref:404264).

## Access Claims

[!include[](~/templates/authentication-access-claims.md)]
