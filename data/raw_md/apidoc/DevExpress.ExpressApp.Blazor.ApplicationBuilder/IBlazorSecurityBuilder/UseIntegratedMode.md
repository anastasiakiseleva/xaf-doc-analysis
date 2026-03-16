---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder.UseIntegratedMode(System.Action{DevExpress.ExpressApp.Security.SecurityOptions},System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions})
name: UseIntegratedMode(Action<SecurityOptions>, Action<SecurityModuleOptions>)
type: Method
summary: Enables and configures the [Security System](xref:113366) in [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core).
syntax:
  content: IBlazorSecurityBuilder UseIntegratedMode(Action<SecurityOptions> configureOptions, Action<SecurityModuleOptions> configureSecurityModule = null)
  parameters:
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.SecurityOptions}
    description: Options that allow you to configure the Security System.
  - id: configureSecurityModule
    type: System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions}
    defaultValue: "null"
    description: Options that allow you to configure the Security Module.
  return:
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{12-19}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    options.RoleType = typeof(PermissionPolicyRole);
                    options.UserType = typeof(ApplicationUser);
                    options.UserLoginInfoType = typeof(ApplicationUserLoginInfo);
                    options.UseXpoPermissionsCaching();
                }, moduleOptions => {
                    // ...
                })
                // ...
        });
        // ...
    }
}
```
***