---
uid: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder`1.UseTokenAuthentication(System.String,System.Func{System.String})
name: UseTokenAuthentication(String, Func<String>)
type: Method
summary: Configures the client to use a custom authentication based on the specified authentication scheme name and a JSON web token (JWT) identified through a delegate.
syntax:
  content: public MiddleTierClientBuilder<TDbContext> UseTokenAuthentication(string schemeName, Func<string> accessTokenProvider)
  parameters:
  - id: schemeName
    type: System.String
    description: The name of the [authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication#authentication-scheme).
  - id: accessTokenProvider
    type: System.Func{System.String}
    description: A delegate that should return JSON web token (JWT).
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.MiddleTierClientBuilder{{TDbContext}}
    description: The builder that allows you to further configure the Middle Tier client.
seealso:
- linkId: "404389"
- linkId: "404398"
---
You can use this method for OAuth, Microsoft Entra ID (Azure AD), and other types of authentication.
