---
uid: DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder.ObjectSpaceProviders
name: ObjectSpaceProviders
type: Property
summary: Provides access to `IObjectSpaceProviderBuilder` that allows you to configure [Object Spaces](xref:113707) used in your application.
syntax:
  content: IObjectSpaceProviderBuilder<IWinApplicationBuilder> ObjectSpaceProviders { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder}
    description: 'Allows you to configure [Object Spaces](xref:113707) used in your application. '
seealso: []
---
The following example demonstrates how to use this property:

**File**: _MySolution.Win\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{8-12}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Win.ApplicationBuilder;
// ...
public class ApplicationBuilder : IDesignTimeApplicationFactory {
    public static WinApplication BuildApplication(string connectionString) {
        var builder = WinApplication.CreateBuilder();
        builder.UseApplication<MySolutionWindowsFormsApplication>();
        builder.ObjectSpaceProviders
            .AddSecuredXpo((application, options) => {
                options.ConnectionString = connectionString;
            })
            .AddNonPersistent();
        // ...
    }
    // ...
}
```
***