---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.MiddleTierSecurityExtensions.UseMiddleTierMode(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder,System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityOptions},System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions})
name: UseMiddleTierMode(IBlazorSecurityBuilder, Action<MiddleTierSecurityOptions>, Action<SecurityModuleOptions>)
type: Method
summary: Enables and configures [XPO Middle Tier Security](xref:113439).
syntax:
  content: public static IMiddleTierAuthenticationBuilder UseMiddleTierMode(this IBlazorSecurityBuilder securityBuilder, Action<MiddleTierSecurityOptions> configureOptions, Action<SecurityModuleOptions> configureSecurityModule = null)
  parameters:
  - id: securityBuilder
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: Allows you to configure the [security system](xref:113366) in your application.
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierSecurityOptions}
    description: Allows you to configure the security options.
  - id: configureSecurityModule
    type: System.Action{DevExpress.ExpressApp.Security.SecurityModuleOptions}
    defaultValue: "null"
    description: Allows you to configure the security module.
  return:
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: Allows you to chain further [security system](xref:113366) configuration.
seealso: []
---
# [MySolution.Blazor.Server\Startup.cs](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
// ...
public class Startup {
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<BlazorApplication>();
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