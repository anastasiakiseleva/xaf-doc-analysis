---
uid: DevExpress.ExpressApp.ApplicationBuilder.BlazorSecurityBuilderExtensions.AddPasswordAuthentication(DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder,System.Action{DevExpress.ExpressApp.Security.AuthenticationStandardProviderOptions})
name: AddPasswordAuthentication(IBlazorSecurityBuilder, Action<AuthenticationStandardProviderOptions>)
type: Method
summary: Enables standard authentication (with a login and password) in your application.
syntax:
  content: public static IBlazorSecurityBuilder AddPasswordAuthentication(this IBlazorSecurityBuilder builder, Action<AuthenticationStandardProviderOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.AuthenticationStandardProviderOptions}
    defaultValue: "null"
    description: Options that you can use to configure standard authentication (with a login and password).
  return:
    type: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorSecurityBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
seealso: []
---
The following example demonstrates how to use this method:

**File**: _YourSolution.Blazor.Server\Startup.cs_.

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
                .AddPasswordAuthentication(options => {
                    options.IsSupportChangePassword = true;
                })
        });
        // ...
    }
}
```
***