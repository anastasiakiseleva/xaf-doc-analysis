---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.Security
name: Security
type: Property
summary: Provides access to `IBlazorSecurityBuilder` that allows you to configure the [Security System](xref:113366).
syntax:
  content: IBlazorSecurityBuilder Security { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: 'Allows you to configure the [Security System](xref:113366). '
seealso: []
---
The following example demonstrates how to use this property:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-20}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
using DevExpress.Persistent.BaseImpl;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.Security
                .UseIntegratedMode(options => {
                    options.RoleType = typeof(PermissionPolicyRole);
                    options.UserType = typeof(CustomApplicationUser);
                    options.UserLoginInfoType = typeof(CustomApplicationUserLoginInfo);
                    options.UseXpoPermissionsCaching();
                })
                .AddPasswordAuthentication(options => {
                    options.IsSupportChangePassword = true;
                });
            // ...
        });
        // ...
    }
}
```
***