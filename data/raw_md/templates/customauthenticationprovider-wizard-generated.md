# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// In Entity Framework Core solutions
using DevExpress.Persistent.BaseImpl.EF.PermissionPolicy;
// In XPO solutions
using DevExpress.Persistent.BaseImpl.PermissionPolicy
using MySolution.Module.BusinessObjects;

public class CustomAuthenticationProvider : IAuthenticationProviderV2 {
    private readonly UserManager userManager;

    public CustomAuthenticationProvider(UserManager userManager) {
        this.userManager = userManager;
    }

    public object Authenticate(IObjectSpace objectSpace) {
        // When a user successfully logs in with an OAuth provider, you can get their unique user key.
        // The following code snippet finds an ApplicationUser object associated with this key.
        // This code also creates a new ApplicationUser object for this key automatically.
        var currentPrincipal = userManager.GetCurrentPrincipal();
        if(currentPrincipal?.Identity?.IsAuthenticated ?? false) {
            var user = userManager.FindUserByPrincipal<ApplicationUser>(objectSpace, currentPrincipal);
            if(user != null) {
                return new UserResult(user);
            }
        // The following code sample creates users for testing purposes only.
#if !RELEASE
            bool autoCreateUser = true;
            if(autoCreateUser) {
                var userResult = userManager.CreateUser<ApplicationUser>(objectSpace, currentPrincipal, user => {
                    user.Roles.Add(objectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default"));
                });
                if(!userResult.Succeeded) {
                    // throw userResult.Error;
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