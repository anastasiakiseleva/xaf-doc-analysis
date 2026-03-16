---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.MiddleTierAuthenticationBuilderExtensions.UsePasswordAuthentication(DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder,System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierPasswordAuthenticationOptions})
name: UsePasswordAuthentication(IMiddleTierAuthenticationBuilder, Action<MiddleTierPasswordAuthenticationOptions>)
type: Method
summary: Enables standard authentication (with a login and password) in the [Middle Tier](xref:113439) application server.
syntax:
  content: public static IMiddleTierAuthenticationBuilder UsePasswordAuthentication(this IMiddleTierAuthenticationBuilder builder, Action<MiddleTierPasswordAuthenticationOptions> configureOptions = null)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.ApplicationBuilder.MiddleTierPasswordAuthenticationOptions}
    defaultValue: "null"
    description: For internal use. Do not specify these settings in your application.
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IMiddleTierAuthenticationBuilder
    description: Allows you to enable and configure the [Security System](xref:113366) in your application, and chain further configuration.
seealso: []
---
The following code snippet uses this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{13-15}
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
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***