```csharp
static IServiceCollection ConfigureSecurity(this IServiceCollection services) {
    services.PostConfigure<SecurityOptions>(options => {
        options.Lockout.Enabled = true;
        options.Lockout.MaxFailedAccessAttempts = 3;
        options.RoleType = typeof(PermissionPolicyRole);
        options.UserType = typeof(ApplicationUser);
        options.UserTokenType = typeof(UserToken);
        options.UserLoginInfoType = typeof(ApplicationUserLoginInfo);
        options.SupportNavigationPermissionsForTypes = false;
        options.Events.OnSecurityStrategyCreated += securityStrategy => {
            ((SecurityStrategy)securityStrategy).PermissionsReloadMode = PermissionsReloadMode.CacheOnFirstAccess;
        };
    });
```

Refer to the [MainDemo.NET.EFCore](xref:113577#employee-management-demo-xpoef-core) demo application for the full code example.