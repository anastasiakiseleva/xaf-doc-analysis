---
uid: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CustomCreateUser
name: CustomCreateUser
type: Event
summary: Occurs when a user is created automatically.
syntax:
  content: public event EventHandler<CustomCreateUserEventArgs> CustomCreateUser
seealso: []
---
When the [AuthenticationActiveDirectory.CreateUserAutomatically](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.CreateUserAutomatically) property is set to **true**, the Security System creates a user for the Windows account used to start the application. To customize this process, handle the **CustomCreateUser** event and assign a user object to the [CustomCreateUserEventArgs.User](xref:DevExpress.ExpressApp.Security.CustomCreateUserEventArgs.User) parameter. Set the **Handled** parameter to **true** to cancel the default user creation.

The following example demonstrates how to handle this event and create a new user associated with a low-privileged _"Default"_ role in the event handler:

**File:** _MySolution.Win\WinApplication.cs_ (_MySolution.Win\WinApplication.vb_)

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.Security.Strategy;
// ...
public partial class MySolutionWindowsFormsApplication : WinApplication {
    public MySolutionWindowsFormsApplication() {
        // ...
        authenticationActiveDirectory1.CustomCreateUser += authenticationActiveDirectory1_CustomCreateUser;
    }
    private void authenticationActiveDirectory1_CustomCreateUser(object sender, CustomCreateUserEventArgs e) {
        ApplicationUser user = e.ObjectSpace.CreateObject<ApplicationUser>();
        user.UserName = e.UserName;
        PermissionPolicyRole defaultRole = 
            e.ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
        if (defaultRole != null) {
            user.Roles.Add(defaultRole);
        }
        e.User = user;
        e.Handled = true;
    }
    // ...
}
```
***

To create this _"Default"_ role, override the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method in the [!include[File_Updater](~/templates/file_updater111114.md)] file (the [Template Kit](xref:405447) adds similar code):

**File:** _MySolution.Module\DatabaseUpdate\Updater.cs_ (_MySolution.Module\DatabaseUpdate\Updater.vb_)

# [C#](#tab/tabid-csharp)

```csharp
public override void UpdateDatabaseAfterUpdateSchema() {
    base.UpdateDatabaseAfterUpdateSchema();
    // ...
    PermissionPolicyRole defaultRole = ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
    if(defaultRole == null) {
        defaultRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
        defaultRole.Name = "Default";
        defaultRole.AddObjectPermissionFromLambda<ApplicationUser>(SecurityOperations.Read, u => u.Oid == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
        defaultRole.AddNavigationPermission(@"Application/NavigationItems/Items/Default/Items/MyDetails", SecurityPermissionState.Allow);
        defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, "ChangePasswordOnFirstLogon", u => u.Oid == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
        defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(SecurityOperations.Write, "StoredPassword", u => u.Oid == (Guid)CurrentUserIdOperator.CurrentUserId(), SecurityPermissionState.Allow);
        defaultRole.AddTypePermissionsRecursively<PermissionPolicyRole>(SecurityOperations.Read, SecurityPermissionState.Deny);
        defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.ReadWriteAccess, SecurityPermissionState.Allow);
        defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.ReadWriteAccess, SecurityPermissionState.Allow);
        defaultRole.AddTypePermissionsRecursively<ModelDifference>(SecurityOperations.Create, SecurityPermissionState.Allow);
        defaultRole.AddTypePermissionsRecursively<ModelDifferenceAspect>(SecurityOperations.Create, SecurityPermissionState.Allow);                
    }
    ObjectSpace.CommitChanges();
}
```
***