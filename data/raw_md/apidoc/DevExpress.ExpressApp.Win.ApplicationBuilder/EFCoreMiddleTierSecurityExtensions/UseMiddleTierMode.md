---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.EFCoreMiddleTierSecurityExtensions.UseMiddleTierMode(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinSecurityBuilder,System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityOptions},System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions})
name: UseMiddleTierMode(IWinSecurityBuilder, Action<EFCoreMiddleTierSecurityOptions>, Action<SecurityModuleOptions>)
type: Method
summary: Enables and configures [EF Core Middle Tier Security](xref:404389).
syntax:
  content: public static IMiddleTierAuthenticationBuilder UseMiddleTierMode(this IWinSecurityBuilder securityBuilder, Action<EFCoreMiddleTierSecurityOptions> configureOptions, Action<SecurityModuleOptions> configureSecurityModule = null)
  parameters:
  - id: securityBuilder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.EFCoreMiddleTierSecurityOptions}
    description: Options that allow you to configure the Security System.
  - id: configureSecurityModule
    type: System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions}
    defaultValue: "null"
    description: Options that allow you to configure the Security System.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: Allows you to enable and configure the [Security System](xref:113366) in your application, and chain further configuration.
seealso: []
---
The following code snippet uses this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{9-14}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        // ...
        builder.Security
            .UseMiddleTierMode(options => {
                // ...
            }, moduleOptions => {
                // ...
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***
