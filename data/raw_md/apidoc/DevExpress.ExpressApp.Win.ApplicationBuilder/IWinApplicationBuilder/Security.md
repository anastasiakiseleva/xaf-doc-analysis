---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder.Security
name: Security
type: Property
summary: Provides access to `IWinSecurityBuilder` that allows you to configure the [Security System](xref:113366).
syntax:
  content: IWinSecurityBuilder Security { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinSecurityBuilder
    description: 'Allows you to configure the [Security System](xref:113366). '
seealso: []
---
The following example demonstrates how to use this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{8-15}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.Security
            .UseIntegratedMode(options => {
                options.RoleType = typeof(PermissionPolicyRole);
                options.UserType = typeof(CustomApplicationUser);
                options.UserLoginInfoType = typeof(CustomApplicationUserLoginInfo);
                options.UseXpoPermissionsCaching();
            })
            .UsePasswordAuthentication();
        // ...
    }
    // ...
}
```
***