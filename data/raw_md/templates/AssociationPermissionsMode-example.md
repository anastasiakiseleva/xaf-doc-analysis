```csharp
builder.Security
    .UseIntegratedMode(options => {
        options.RoleType = typeof(PermissionPolicyRole);
        options.UserType = typeof(YourSolutionName.Module.BusinessObjects.ApplicationUser);
        options.UserLoginInfoType = typeof(YourSolutionName.Module.BusinessObjects.ApplicationUserLoginInfo);
        //...
        options.Events.OnSecurityStrategyCreated += (securityStrategy) => {
            //...
            ((SecurityStrategy)securityStrategy).AssociationPermissionsMode = AssociationPermissionsMode.Manual;
        })
```
