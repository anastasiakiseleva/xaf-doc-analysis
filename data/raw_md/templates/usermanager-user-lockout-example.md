See the @DevExpress.ExpressApp.Security.ISecurityUserLockout topic for information on the user lockout ("Brute Force" attack protection) feature in XAF. 

## Example

This example demonstrates how to use `UserManager` API to allow administrators to view the lockout status of application users and how to implement a controller action that administrators can use to reset the lockout for a specific user account.

To display the user lockout status in the List View and Detail View for the `ApplicationUser` persistent class, add a non-persistent `IsLockedOut` property to this class. In the property getter, use the `UserManager.IsLockedOut` method to obtain the lockout status for the current user object:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using Microsoft.Extensions.DependencyInjection;
using DevExpress.ExpressApp.Security;
// ...
public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo, ISecurityUserLockout {
    // ...
    [NotMapped]
    public virtual bool IsLockedOut {
        get {
            var userManager = ObjectSpace.ServiceProvider.GetRequiredService<UserManager>();
            return userManager.IsLockedOut(this);
        }    
    }
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using Microsoft.Extensions.DependencyInjection;
using DevExpress.ExpressApp.Security;
// ...
public class ApplicationUser : PermissionPolicyUser, ISecurityUserWithLoginInfo, ISecurityUserLockout {
    // ...
    public bool IsLockedOut {
        get {
            var userManager = Session.ServiceProvider.GetRequiredService<UserManager>();
            return userManager.IsLockedOut(this);
        }
    }
}
```
***

Next, add a new View Controller and implement a controller action that calls the `UserManager.ResetLockout` method to reset the lockout for the currently viewed user account:

# [C#](#tab/tabid-csharp)

```csharp{28-29}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
using Microsoft.Extensions.DependencyInjection;
using MySolution.Module.BusinessObjects;
// ...
public class ResetUserLockoutController : ViewController {
    IServiceProvider serviceProvider;
    SimpleAction resetUserLockoutAction;

    public ResetUserLockoutController() { }

    [ActivatorUtilitiesConstructor]
    public ResetUserLockoutController(IServiceProvider serviceProvider) : this() {
        this.serviceProvider = serviceProvider;
        TargetViewType = ViewType.DetailView;
        TargetObjectType = typeof(ApplicationUser);

        resetUserLockoutAction = new SimpleAction(this, "ResetLockout", PredefinedCategory.View) {
            Caption = "Reset Lockout",
        };

        resetUserLockoutAction.Execute += ResetUserLockoutAction_Execute;
    }

    private void ResetUserLockoutAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        var userManager = serviceProvider.GetRequiredService<UserManager>();
        userManager.ResetLockout(View.CurrentObject);
        View.Refresh();
    }

    protected override void OnActivated() {
        base.OnActivated();
        // Hide the action from non-admin users.
        ISecurityStrategyBase securityStrategy = serviceProvider.GetRequiredService<ISecurityProvider>().GetSecurity();
        ApplicationUser currentUser = (ApplicationUser)securityStrategy.User;
        resetUserLockoutAction.Active["AdminOnlyAction"] = currentUser.Roles.Any(r => r.IsAdministrative);
    }
}

```
***

The image below demonstrates the result:

![Result](~/images/usermanager-user-lockout-example.png)
