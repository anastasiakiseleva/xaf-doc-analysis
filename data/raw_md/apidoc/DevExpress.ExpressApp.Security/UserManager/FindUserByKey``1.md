---
uid: DevExpress.ExpressApp.Security.UserManager.FindUserByKey``1(DevExpress.ExpressApp.IObjectSpace,System.String)
name: FindUserByKey<TUser>(IObjectSpace, String)
type: Method
summary: Finds an application user based on the specified user object ID.
syntax:
  content: |-
    public TUser FindUserByKey<TUser>(IObjectSpace objectSpace, string userKey)
        where TUser : class, ISecurityUserWithLoginInfo
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to search for a user.
  - id: userKey
    type: System.String
    description: A `System.String` that contains the user ID.
  typeParameters:
  - id: TUser
    description: The user object type.
  return:
    type: '{TUser}'
    description: The resulting user object.
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByLogin``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)
  altText: FindUserByLogin
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByName``1(DevExpress.ExpressApp.IObjectSpace,System.String)
  altText: FindUserByName
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByPrincipal``1(DevExpress.ExpressApp.IObjectSpace,System.Security.Principal.IPrincipal)
  altText: FindUserByPrincipal
---

The following code snippet demonstrates how to use the `FindUserByKey` method to find a user based on the user object's key value:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Security;
using Microsoft.Extensions.DependencyInjection;
// ...
// Use Dependency Injection to access the IServiceProvider.
var userManager = serviceProvider.GetRequiredService<UserManager>();
ApplicationUser user = userManager.FindUserByKey<ApplicationUser>(os, userKeyValue);
```
***
[`Dependency Injection`]: xref:404364
[`IServiceProvider`]: xref:System.IServiceProvider

