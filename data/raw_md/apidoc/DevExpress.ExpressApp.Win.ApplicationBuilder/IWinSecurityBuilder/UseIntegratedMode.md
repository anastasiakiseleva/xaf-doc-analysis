---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinSecurityBuilder.UseIntegratedMode(System.Action{DevExpress.ExpressApp.Security.SecurityOptions},System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions})
name: UseIntegratedMode(Action<SecurityOptions>, Action<SecurityModuleOptions>)
type: Method
summary: Enables and configures the [Security System](xref:113366) in [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core).
syntax:
  content: IWinAuthenticationBuilder UseIntegratedMode(Action<SecurityOptions> configureOptions, Action<SecurityModuleOptions> configureSecurityModule = null)
  parameters:
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.SecurityOptions}
    description: Options that allow you to configure the Security System.
  - id: configureSecurityModule
    type: System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions}
    defaultValue: "null"
    description: Options that allow you to configure the Security Module.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{10-17}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        // ...
        builder.Security
            .UseIntegratedMode(options => {
                options.RoleType = typeof(PermissionPolicyRole);
                options.UserType = typeof(ApplicationUser);
                options.UserLoginInfoType = typeof(ApplicationUserLoginInfo);
            },
            moduleOptions => {
                // ...
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***