---
uid: DevExpress.ExpressApp.Security.UserManager.FindUserByLogin``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)
name: FindUserByLogin<TUser>(IObjectSpace, String, String)
type: Method
summary: Finds an application user based on the specified user login information.
syntax:
  content: |-
    public TUser FindUserByLogin<TUser>(IObjectSpace objectSpace, string loginProviderName, string providerUserKey)
        where TUser : class, ISecurityUserWithLoginInfo
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to search for a user.
  - id: loginProviderName
    type: System.String
    description: The name of the login provider for which to find a user.
  - id: providerUserKey
    type: System.String
    description: The user key for the specified login provider.
  typeParameters:
  - id: TUser
    description: The user object type.
  return:
    type: '{TUser}'
    description: The resulting user object.
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByKey``1(DevExpress.ExpressApp.IObjectSpace,System.String)
  altText: FindUserByKey
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByName``1(DevExpress.ExpressApp.IObjectSpace,System.String)
  altText: FindUserByName
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByPrincipal``1(DevExpress.ExpressApp.IObjectSpace,System.Security.Principal.IPrincipal)
  altText: FindUserByPrincipal
---

The following code snippet demonstrates how to use the `FindUserByLogin` method to find a user based on their login information for the specified login provider:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var userManager = serviceProvider.GetRequiredService<UserManager>();
ApplicationUser user = userManager.FindUserByLogin<ApplicationUser>(os, "MyCustomLoginProvider", providerUserKey);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider