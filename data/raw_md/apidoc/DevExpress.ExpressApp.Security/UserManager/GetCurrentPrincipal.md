---
uid: DevExpress.ExpressApp.Security.UserManager.GetCurrentPrincipal
name: GetCurrentPrincipal()
type: Method
summary: Gets the current user's `ClaimsPrincipal` object.
syntax:
  content: public IPrincipal GetCurrentPrincipal()
  return:
    type: System.Security.Principal.IPrincipal
    description: An object that implements the `IPrincipal` interface.
seealso:
- linkId: "404462"
---

The following code snippet demonstrates a [custom authentication provider](xref:402197) implementation that uses the `GetCurrentPrincipal` method to access the `ClaimsPrincipal` object returned by a third-party authentication service ([Template Kit](xref:405447) generates equivalent code for applications configured to use OAuth2).

# [C#](#tab/tabid-csharp)

```csharp{9}
public class CustomAuthenticationProvider : IAuthenticationProviderV2 {
    private readonly UserManager userManager;

    public CustomAuthenticationProvider(UserManager userManager) {
        this.userManager = userManager;
    }

    public object Authenticate(IObjectSpace objectSpace) {
        var currentPrincipal = userManager.GetCurrentPrincipal();
        if(currentPrincipal?.Identity?.IsAuthenticated ?? false) {
            var user = userManager.FindUserByPrincipal<ApplicationUser>(objectSpace, currentPrincipal);
            if(user != null) {
                return new UserResult<ApplicationUser>(user);
            }

        // The code below creates users for testing purposes only.
#if !RELEASE
            bool autoCreateUser = true;
            if(autoCreateUser) {
                var userResult = userManager.CreateUser<ApplicationUser>(objectSpace, currentPrincipal, user => {
                    user.Roles.Add(objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default"));
                });
                if(!userResult.Succeeded) {
                    //throw userResult.Error;
                }
                return userResult;
            }
#endif
        }
        return null;
    }
}
```
***