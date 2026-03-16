---
uid: DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions.Events
name: Events
type: Property
summary: Provides access to Windows Authentication events.
syntax:
  content: public WindowsActiveDirectoryAuthenticationProviderEvents Events { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Security.Authentication.WindowsActiveDirectoryAuthenticationProviderEvents
    description: Windows Authentication events.
seealso: []
---
The following example demonstrates how to use this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{14-16}
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
                options.Events.CustomCreateUser = (args) => {
                    // ...
                };
            });
        // ...
    }
    // ...
}
```
***