---
uid: DevExpress.ExpressApp.ApplicationBuilder.BlazorSecurityBuilderExtensions.AddWindowsAuthentication(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder,System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions})
name: AddWindowsAuthentication(IBlazorSecurityBuilder, Action<WindowsAuthenticationOptions>)
type: Method
summary: Enables [Windows Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth) in your application.
syntax:
  content: public static IBlazorSecurityBuilder AddWindowsAuthentication(this IBlazorSecurityBuilder builder, Action<WindowsAuthenticationOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions}
    defaultValue: "null"
    description: Options that you can use to configure Windows Authentication.
  return:
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _YourSolutionName.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{16-18}
using DevExpress.ExpressApp.ApplicationBuilder;

namespace YourSolutionName.Blazor.Server;

public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<YourSolutionNameBlazorApplication>();
            // ...
            builder.Security
                .UseIntegratedMode(options => {
                    // ...
                })
                .AddWindowsAuthentication(options => {
                    options.CreateUserAutomatically();
                });
        });
        // ...
    }
}
```
***