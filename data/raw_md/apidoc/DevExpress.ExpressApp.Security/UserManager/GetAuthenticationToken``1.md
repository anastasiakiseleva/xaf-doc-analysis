---
uid: DevExpress.ExpressApp.Security.UserManager.GetAuthenticationToken``1(``0,System.Int32,System.Collections.Generic.IEnumerable{System.Security.Claims.Claim})
name: GetAuthenticationToken<TUser>(TUser, Int32, IEnumerable<Claim>)
type: Method
summary: Gets an authentication token for the specified user.
syntax:
  content: |-
    public string GetAuthenticationToken<TUser>(TUser user, int expirationSeconds, IEnumerable<Claim> additionalClaims = null)
        where TUser : class, ISecurityUserWithLoginInfo
  parameters:
  - id: user
    type: '{TUser}'
    description: An application user object.
  - id: expirationSeconds
    type: System.Int32
    description: The number of seconds until the authentication token expires.
  - id: additionalClaims
    type: System.Collections.Generic.IEnumerable{System.Security.Claims.Claim}
    defaultValue: "null"
    description: A collection of additional claims to add to the resulting token.
  typeParameters:
  - id: TUser
    description: The user object type.
  return:
    type: System.String
    description: A `System.String`that contains the resulting authentication topic.
seealso: []
---

> [!IMPORTANT]
>
> This method is not supported on the WinForms platform. If called from a WinForms application, it throws the @System.PlatformNotSupportedException.

The following code snippet demonstrates a custom implementation of an `IAuthenticationTokenProvider`that uses the `GetAuthenticationToken` to generate an authentication token for a successfully authenticated user:

# [C#](#tab/tabid-csharp)

```csharp{22}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Core;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Security.Authentication.ClientServer;
using System.Runtime.ExceptionServices;
// ...
public class JwtTokenProviderService : IAuthenticationTokenProvider {
    IServiceProvider serviceProvider;

    public JwtTokenProviderService(IServiceProvider serviceProvider) {
        this.serviceProvider = serviceProvider;
    }
    public string Authenticate(object logonParameters) {
        var signInManager = serviceProvider.GetRequiredService<SignInManager>();
        var userManager = serviceProvider.GetRequiredService<UserManager>();

        var result = signInManager.AuthenticateByLogonParameters(logonParameters);
        if(result.Succeeded) {
            using IObjectSpace nonSecuredObjectSpace = serviceProvider
                .GetRequiredService<INonSecuredObjectSpaceFactory>().CreateNonSecuredObjectSpace<ApplicationUser>();
            var user = userManager.FindUserByPrincipal<ApplicationUser>(nonSecuredObjectSpace, result.Principal);
            var token = userManager.GetAuthenticationToken(user, 6000);
            return token;
        }
        if(result.Error is IUserFriendlyException) {
            ExceptionDispatchInfo.Throw(result.Error);
        }
        throw new AuthenticationException("Internal server error");
    }
}
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider