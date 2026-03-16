---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.MiddleTierSecurityExtensions.UseMiddleTierMode(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinSecurityBuilder,System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityOptions},System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions})
name: UseMiddleTierMode(IWinSecurityBuilder, Action<MiddleTierSecurityOptions>, Action<SecurityModuleOptions>)
type: Method
summary: Enables and configures [XPO Middle Tier Security](xref:113439).
syntax:
  content: public static IMiddleTierAuthenticationBuilder UseMiddleTierMode(this IWinSecurityBuilder securityBuilder, Action<MiddleTierSecurityOptions> configureOptions, Action<SecurityModuleOptions> configureSecurityModule = null)
  parameters:
  - id: securityBuilder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityOptions}
    description: Options that allow you to configure the Security System.
  - id: configureSecurityModule
    type: System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions}
    defaultValue: "null"
    description: Options that allow you to configure the Security Module.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

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