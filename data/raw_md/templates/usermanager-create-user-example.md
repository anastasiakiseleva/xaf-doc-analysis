**File:** _MySolution.Module/DatabaseUpdate/Updater.cs_

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Security;
// ...
public class Updater : ModuleUpdater {
    // ...
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
        UserManager userManager = ObjectSpace.ServiceProvider.GetRequiredService<UserManager>();
        // If a user named 'User' doesn't exist in the database, create this user.
        if(userManager.FindUserByName<ApplicationUser>(ObjectSpace, "User") == null) {
            // Set a password if the standard authentication type is used.
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
