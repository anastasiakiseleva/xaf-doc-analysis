---
uid: DevExpress.ExpressApp.Security.UserManager.FindUserByName``1(DevExpress.ExpressApp.IObjectSpace,System.String)
name: FindUserByName<TUser>(IObjectSpace, String)
type: Method
summary: Finds an application user based on the specified user name.
syntax:
  content: |-
    public TUser FindUserByName<TUser>(IObjectSpace objectSpace, string name)
        where TUser : class, ISecurityUser
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An Object Space used to search for a user.
  - id: name
    type: System.String
    description: A `System.String` value that contains the user name.
  typeParameters:
  - id: TUser
    description: The user object type.
  return:
    type: '{TUser}'
    description: The resulting user object.
seealso:
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByKey``1(DevExpress.ExpressApp.IObjectSpace,System.String)
  altText: FindUserByKey
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByLogin``1(DevExpress.ExpressApp.IObjectSpace,System.String,System.String)
  altText: FindUserByLogin
- linkId: DevExpress.ExpressApp.Security.UserManager.FindUserByPrincipal``1(DevExpress.ExpressApp.IObjectSpace,System.Security.Principal.IPrincipal)
  altText: FindUserByPrincipal
---

Use this method to search for a user object based on a user name as the following code snippet demonstrates:

**File:** _MySolution.Module/DatabaseUpdate/Updater.cs_

# [C#](#tab/tabid-csharp)
```csharp{9}
using DevExpress.ExpressApp.Security;
// ...
public class Updater : ModuleUpdater {
    // ...
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
        UserManager userManager = ObjectSpace.ServiceProvider.GetRequiredService<UserManager>();
        // If a user named 'User' doesn't exist in the database, create this user
        if(userManager.FindUserByName<ApplicationUser>(ObjectSpace, "User") == null) {
            // Set a password if the standard authentication type is used
            string EmptyPassword = "";
            var userCreationResult = userManager.CreateUser<ApplicationUser>(ObjectSpace, "User", EmptyPassword, (user) => {
                // Add the Users role to the user
                user.Roles.Add(defaultRole);
            });
            // ...
        }
        // ...
        ObjectSpace.CommitChanges(); // This line persists created object(s).
    }
}
```
***