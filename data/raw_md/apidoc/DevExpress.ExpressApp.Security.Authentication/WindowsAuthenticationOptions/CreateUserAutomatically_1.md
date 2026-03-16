---
uid: DevExpress.ExpressApp.Security.Authentication.WindowsAuthenticationOptions.CreateUserAutomatically(DevExpress.ExpressApp.Security.ICanInitializeNewUser)
name: CreateUserAutomatically(ICanInitializeNewUser)
type: Method
summary: Specifies whether a user is created automatically for the Windows account used to run the application.
syntax:
  content: public void CreateUserAutomatically(ICanInitializeNewUser newUserInitializer)
  parameters:
  - id: newUserInitializer
    type: DevExpress.ExpressApp.Security.ICanInitializeNewUser
    description: 'A custom `ICanInitializeNewUser` object that initializes a new user. '
seealso: []
---
The following example demonstrates how to use this method:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{14}
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
                options.CreateUserAutomatically(new MyCustomUserInitializer());
            });
        // ...
    }
    // ...
}
```
***