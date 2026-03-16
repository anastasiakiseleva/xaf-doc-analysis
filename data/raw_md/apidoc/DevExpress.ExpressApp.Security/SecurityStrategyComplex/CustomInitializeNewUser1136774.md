---
uid: DevExpress.ExpressApp.Security.SecurityStrategyComplex.CustomInitializeNewUser
name: CustomInitializeNewUser
type: Event
summary: Occurs when a user is automatically created.
syntax:
  content: public event EventHandler<CustomInitializeNewUserEventArgs> CustomInitializeNewUser
seealso: []
---
Use this event to setup an automatically created user and link it to necessary roles. Set the **Handled** parameter to **true** to disable the default initialization. 

When the default initialization is enabled, the Security System does the following:

1. Tries to find an object of the [SecurityStrategyComplex.RoleType](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.RoleType) with a **Name** property value equal to a [SecurityStrategyComplex.NewUserRoleName](xref:DevExpress.ExpressApp.Security.SecurityStrategyComplex.NewUserRoleName)'s value. If this role was not found, creates a new role with the name specified in the **NewUserRoleName** property and sets the role's **IsAdministrative** property to **true**.
2. Adds a newly created user to the **Users** collection of the role found or created at the previous step.

The following example handles the `CustomInitializeNewUser` event and sets a value to a custom property of a new user:

# [Startup.cs](#tab/tabid-csharp)
```csharp
public void ConfigureServices(IServiceCollection services) {
    // ...
    services.AddXaf(Configuration, builder => {
        //...
        builder.Security
            .UseIntegratedMode(options => {
              // ...
              options.Events.OnSecurityStrategyCreated = (e) => 
              { ((SecurityStrategyComplex)e).CustomInitializeNewUser += Startup_CustomInitializeNewUser; };
            })
    });
}

private void Startup_CustomInitializeNewUser(object sender, CustomInitializeNewUserEventArgs e) {
    ((ApplicationUser)e.User).CustomProperty = "newproperty";
}
```
***
