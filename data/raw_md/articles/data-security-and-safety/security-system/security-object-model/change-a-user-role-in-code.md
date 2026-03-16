---
uid: "403826"
title: Change the Current User Role in Code
owner: Yekaterina Kiseleva
seealso:
  - linkId: '113152'
  - linkId: '403824'
---
# Change the Current User Role in Code

This topic describes how to access and edit a user's role collection in applications with [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core).

Follow the steps below to replace the "Default" role with "Extended".

1. Create a new @DevExpress.ExpressApp.ViewController with @DevExpress.ExpressApp.Actions.SimpleAction and handle the Action's @DevExpress.ExpressApp.Actions.SimpleAction.Execute event.
2. In the event handler, call the **CreateNonsecuredObjectSpace** ([XPO](xref:DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.CreateNonsecuredObjectSpace)/[EF Core](xref:DevExpress.EntityFrameworkCore.Security.SecuredEFCoreObjectSpaceProvider`1.CreateNonsecuredObjectSpace)) method to create a non-secured @DevExpress.ExpressApp.IObjectSpace instance. The non-secured Object Space ignores security permissions and provides access to all data.
3. Use the @DevExpress.ExpressApp.Security.XafApplicationExtensions.GetSecurityStrategy(DevExpress.ExpressApp.XafApplication) method and @DevExpress.ExpressApp.Security.SecurityStrategyBase.User property to access the current user. Call the @DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object) method to copy the user object to the non-secured Object Space.
4. Remove the "Default" role from the @DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.Roles collection and add the "Extended" role to this collection.
6. Call the @DevExpress.ExpressApp.IObjectSpace.CommitChanges method of the unsecured Object Space to save these changes.
7. Call the @DevExpress.ExpressApp.IObjectSpace.Refresh method of the main Object Space to display the new changes in the UI. 

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
using System.Linq;
// ...
public class SetExtendedRoleController : ViewController {
    SimpleAction setExtendedRoleAction; 
    public SetExtendedRoleController() {
        setExtendedRoleAction = new SimpleAction(this, "SetExtendedRole", PredefinedCategory.Edit);
        setExtendedRoleAction.Execute += SetExtendedRoleAction_Execute;
    }

    private void SetExtendedRoleAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        using (IObjectSpace nonSecuredObjectSpace =
            ((INonsecuredObjectSpaceProvider)Application.ObjectSpaceProvider).CreateNonsecuredObjectSpace()) {
            SecurityStrategy security = Application.GetSecurityStrategy();
            ApplicationUser user = (ApplicationUser)nonSecuredObjectSpace.GetObject(security.User);
            PermissionPolicyRole oldRole = user.Roles.FirstOrDefault(r => r.Name == "Default");
            if (oldRole != null) {
                PermissionPolicyRole newRole =
                    nonSecuredObjectSpace.FirstOrDefault<PermissionPolicyRole>(r => r.Name == "Extended");
                user.Roles.Remove(oldRole);
                user.Roles.Add(newRole);
                nonSecuredObjectSpace.CommitChanges();
                ObjectSpace.Refresh();
            }
        }
    }
}
```

***

[`ViewController`]: xref:DevExpress.ExpressApp.ViewController
[`Application`]: xref:DevExpress.ExpressApp.Controller.Application
[`SimpleAction`]: xref:DevExpress.ExpressApp.Actions.SimpleAction
[`/\.(Execute)/`]: xref:DevExpress.ExpressApp.Actions.SimpleAction.Execute
[`SecurityStrategy`]: xref:DevExpress.ExpressApp.Security.SecurityStrategy
[`GetSecurityStrategy`]: xref:DevExpress.ExpressApp.Security.XafApplicationExtensions.GetSecurityStrategy(DevExpress.ExpressApp.XafApplication)
[`PermissionPolicyRole`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole
[`Roles`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.Roles
[`User`]: xref:DevExpress.ExpressApp.Security.SecurityStrategyBase.User
[`CreateNonsecuredObjectSpace`]: xref:DevExpress.ExpressApp.Security.ClientServer.SecuredObjectSpaceProvider.CreateNonsecuredObjectSpace
[`GetObject`]: xref:DevExpress.ExpressApp.IObjectSpace.GetObject(System.Object)
[`CommitChanges`]: xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges
[`Refresh`]: xref:DevExpress.ExpressApp.IObjectSpace.Refresh
[`INonsecuredObjectSpaceProvider`]: xref:DevExpress.ExpressApp.Security.INonsecuredObjectSpaceProvider