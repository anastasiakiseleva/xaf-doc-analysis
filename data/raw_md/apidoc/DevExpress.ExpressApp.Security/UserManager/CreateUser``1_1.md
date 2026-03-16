---
uid: DevExpress.ExpressApp.Security.UserManager.CreateUser``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String,System.String,System.Action{``0},System.Boolean)
name: CreateUser<TUser>(IObjectSpace, String, String, String, Action<TUser>, Boolean)
type: Method
summary: Creates a new user with the specified settings.
syntax:
  content: |-
    public UserResult<TUser> CreateUser<TUser>(IObjectSpace objectSpace, string userName, string loginProviderName, string providerUserKey, Action<TUser> customizeUser = null, bool autoCommit = true)
        where TUser : class, ISecurityUserWithLoginInfo
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to create the user.
  - id: userName
    type: System.String
    description: A user name for the new user.
  - id: loginProviderName
    type: System.String
    description: The name of the login provider for which to create a user.
  - id: providerUserKey
    type: System.String
    description: The user login for the specified login provider.
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
seealso: []
---

Use this overload of the `CreateUser` method to create a user for a specific authentication provider.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var userManager = serviceProvider.GetRequiredService<UserManager>();
string providerUserKey = Guid.NewGuid().ToString();
var userResult = userManager.CreateUser<ApplicationUser>(os, "User", "ProviderName", providerUserKey);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider

[!include[usermanager-user-result](~/templates/usermanager-user-result.md)]