---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.WinSecurityBuilderExtensions.UseWindowsAuthentication(DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder,System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions})
name: UseWindowsAuthentication(IWinAuthenticationBuilder, Action<WindowsAuthenticationOptions>)
type: Method
summary: Enables Windows Authentication in the application with the [Security System](xref:113366) in [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core).
syntax:
  content: public static IWinAuthenticationBuilder UseWindowsAuthentication(this IWinAuthenticationBuilder builder, Action<WindowsAuthenticationOptions> configureOptions)
  parameters:
  - id: builder
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder
    description: '[!include[ISecurityBuilder_Parameter_Description](~/templates/ISecurityBuilder_Parameter_Description.md)]'
  - id: configureOptions
    type: System.Action{DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions}
    description: Options that allow you to configure the [Security System](xref:113366) in [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core).
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinAuthenticationBuilder
    description: ''
seealso: []
---
The following example demonstrates how to use this method:

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
            .UseIntegratedMode(options => {
                // ...
            })
            .UseWindowsAuthentication(options => {
                options.CreateUserAutomatically();
            });
        // ...
    }
    // ...
}
```
***