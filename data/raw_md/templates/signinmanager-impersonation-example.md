> [!NOTE]
> Note that the user impersonation technique demonstrated below is not supported for WinForms applications.
>
> In Blazor applications, the demonstrated technique is not compatible with the static API exposed by the @DevExpress.ExpressApp.SecuritySystem class. This is because the `SecuritySystem` class's methods always operate on the XAF application instance rather than a _scope_, so these methods are not affected by impersonation. To avoid faulty behavior in application logic that uses impersonation, ensure that this logic never uses the static API exposed by the `SecuritySystem` class.

# [C#](#tab/tabid-csharp)

```csharp{28}
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Security;
using DevExpress.Persistent.Base;
// ...
public partial class MyController : ViewController<ListView> {
    SimpleAction myAction;
    IServiceScopeFactory serviceScopeFactory;

    [ActivatorUtilitiesConstructor]
    public MyController(IServiceProvider serviceProvider) : this() {
        // ...
        myAction.Execute += MyAction_Execute;
        serviceScopeFactory = serviceProvider.GetRequiredService<IServiceScopeFactory>();
    }
    // ...
    private void MyAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        // ...
        // Create a nested service scope whithin which to establish a separate login session. 
        using (IServiceScope impersonationScope = serviceScopeFactory.CreateScope()) {
            // Use the UserManager to obtain the "ServiceUser" user object.
            using IObjectSpace nonSecuredObjectSpace = impersonationScope.ServiceProvider
                .GetRequiredService<INonSecuredObjectSpaceFactory>().CreateNonSecuredObjectSpace<ApplicationUser>();
            ApplicationUser serviceUser = impersonationScope.ServiceProvider
                .GetRequiredService<UserManager>().FindUserByName<ApplicationUser>(nonSecuredObjectSpace, "ServiceUser");

            // Sign in as "ServiceUser" to the nested scope.
            SignInManager signInManager = impersonationScope.ServiceProvider.GetService<SignInManager>();
            signInManager.SignIn(serviceUser);

            // Obtain an Object Space from the nested scope and use this Object Space
            // to manipulate business objects on the "ServiceUser" user's behalf.
            using IObjectSpace objectSpace = impersonationScope.ServiceProvider
                .GetRequiredService<IObjectSpaceFactory>().CreateObjectSpace<MyActionPerMonth>();
            // ...
        }
    }
}
```
***

[`UserManager`]: DevExpress.ExpressApp.Security.UserManager
[`SignInManager`]: DevExpress.ExpressApp.Security.UserManager

