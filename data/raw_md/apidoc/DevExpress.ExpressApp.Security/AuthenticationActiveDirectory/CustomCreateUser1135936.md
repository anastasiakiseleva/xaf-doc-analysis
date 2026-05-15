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

**File:** _MySolution.Win\WinApplication.cs_

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

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Data.Filtering
Imports DevExpress.ExpressApp.Security
Imports DevExpress.ExpressApp.Security.Strategy
' ...
Partial Public Class MySolutionWindowsFormsApplication
    Inherits WinApplication
    Public Sub New()
        ' ...
        AddHandler authenticationActiveDirectory1.CustomCreateUser,
            AddressOf authenticationActiveDirectory1_CustomCreateUser
    End Sub
    Private Sub authenticationActiveDirectory1_CustomCreateUser(ByVal sender As Object, 
        ByVal e As CustomCreateUserEventArgs)
        Dim user As ApplicationUser = e.ObjectSpace.CreateObject(Of ApplicationUser)()
        user.UserName = e.UserName
        Dim defaultRole As PermissionPolicyRole = 
            e.ObjectSpace.FirstOrDefault(Function(role as PermissionPolicyRole) role.Name = "Default")
        If defaultRole IsNot Nothing Then
            user.Roles.Add(defaultRole)
        End If
        e.User = user
        e.Handled = True
    End Sub
    ' ...
End Class
```

***

To create this _"Default"_ role, override the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method in the [!include[File_Updater](~/templates/file_updater111114.md)] file (the [Template Kit](xref:405447) adds similar code):

**File:** _MySolution.Module\DatabaseUpdate\Updater.cs_

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

# [VB.NET](#tab/tabid-vb)

```vb
Public Overrides Sub UpdateDatabaseAfterUpdateSchema()
    MyBase.UpdateDatabaseAfterUpdateSchema()
    ' ...
    Dim defaultRole As PermissionPolicyRole = ObjectSpace.FirstOrDefault(Function(role as PermissionPolicyRole) role.Name = "Default")
    If defaultRole Is Nothing Then
        defaultRole = ObjectSpace.CreateObject(Of PermissionPolicyRole)()
        defaultRole.Name = "Default"
        defaultRole.AddObjectPermissionFromLambda(Of ApplicationUser)(SecurityOperations.Read, Function(u As ApplicationUser) u.Oid = CType(CurrentUserIdOperator.CurrentUserId(), Guid), SecurityPermissionState.Allow)
        defaultRole.AddNavigationPermission("Application/NavigationItems/Items/Default/Items/MyDetails", SecurityPermissionState.Allow)
        defaultRole.AddMemberPermissionFromLambda(Of ApplicationUser)(SecurityOperations.Write, "ChangePasswordOnFirstLogon", Function(u As ApplicationUser) u.Oid = CType(CurrentUserIdOperator.CurrentUserId(), Guid), SecurityPermissionState.Allow)
        defaultRole.AddMemberPermissionFromLambda(Of ApplicationUser)(SecurityOperations.Write, "StoredPassword", Function(u As ApplicationUser) u.Oid = CType(CurrentUserIdOperator.CurrentUserId(), Guid), SecurityPermissionState.Allow)
        defaultRole.AddTypePermissionsRecursively(Of PermissionPolicyRole)(SecurityOperations.Read, SecurityPermissionState.Deny)
        defaultRole.AddTypePermissionsRecursively(Of ModelDifference)(SecurityOperations.ReadWriteAccess, SecurityPermissionState.Allow)
        defaultRole.AddTypePermissionsRecursively(Of ModelDifferenceAspect)(SecurityOperations.ReadWriteAccess, SecurityPermissionState.Allow)
        defaultRole.AddTypePermissionsRecursively(Of ModelDifference)(SecurityOperations.Create, SecurityPermissionState.Allow)
        defaultRole.AddTypePermissionsRecursively(Of ModelDifferenceAspect)(SecurityOperations.Create, SecurityPermissionState.Allow)
    End If
    ObjectSpace.CommitChanges()
End Sub
```

***