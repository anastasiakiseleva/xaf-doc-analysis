---
uid: DevExpress.ExpressApp.Security.UserManager.CreateUser``1(DevExpress.ExpressApp.IObjectSpace,System.Security.Principal.IPrincipal,System.Action{``0},System.Boolean)
name: CreateUser<TUser>(IObjectSpace, IPrincipal, Action<TUser>, Boolean)
type: Method
summary: Creates a new user with the specified settings.
syntax:
  content: |-
    public UserResult<TUser> CreateUser<TUser>(IObjectSpace objectSpace, IPrincipal principal, Action<TUser> customizeUser = null, bool autoCommit = true)
        where TUser : class, ISecurityUserWithLoginInfo
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to create the user.
  - id: principal
    type: System.Security.Principal.IPrincipal
    description: A claims principal object that contains info about the user to create.
  - id: customizeUser
    type: System.Action{{TUser}}
    defaultValue: "null"
    description: A delegate method used to additionally customize the created user object.
  - id: autoCommit
    type: System.Boolean
    defaultValue: "True"
    description: A boolean value that specifies whether or not to automatically commit the changes to the Object Space.
  typeParameters:
  - id: TUser
    description: A user object type.
  return:
    type: DevExpress.ExpressApp.Security.UserResult{{TUser}}
    description: An object that contains the result of the user creation operation.
seealso:
- linkId: "404462"
---

The following code snippet demonstrates a [custom authentication provider](xref:402197) implementation that uses the `CreateUser` method to automatically create users for third-party OAuth2 authentication providers for testing purposes ([Template Kit](xref:405447) generates equivalent code for applications configured to use OAuth2).

# [C#](#tab/tabid-csharp)

```csharp{20-22}
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


[!include[usermanager-user-result](~/templates/usermanager-user-result.md)]