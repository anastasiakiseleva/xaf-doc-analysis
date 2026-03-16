---
uid: DevExpress.ExpressApp.Security.UserManager.FindUserByPrincipal``1(DevExpress.ExpressApp.IObjectSpace,System.Security.Principal.IPrincipal)
name: FindUserByPrincipal<TUser>(IObjectSpace, IPrincipal)
type: Method
summary: Finds an application user based on the specified claims principal.
syntax:
  content: |-
    public TUser FindUserByPrincipal<TUser>(IObjectSpace objectSpace, IPrincipal principal)
        where TUser : class, ISecurityUserWithLoginInfo
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to search for a user.
  - id: principal
    type: System.Security.Principal.IPrincipal
    description: A claims principal object.
  typeParameters:
  - id: TUser
    description: The user object type.
  return:
    type: '{TUser}'
    description: The resulting user object.
seealso:
- linkId: "404462"
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByKey``1(DevExpress.ExpressApp.IObjectSpace,System.String)
  altText: FindUserByKey
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByLogin``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)
  altText: FindUserByLogin
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByName``1(DevExpress.ExpressApp.IObjectSpace,System.String)
  altText: FindUserByName
---

The following code snippet demonstrates a [custom authentication provider](xref:402197) implementation that uses the `FindUserByPrincipal` method to search for a user object based on a `ClaimsPrincipal` object returned by a third-party authentication service ([Template Kit](xref:405447) generates equivalent code for applications configured to use OAuth2).

# [C#](#tab/tabid-csharp)

```csharp{11}
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