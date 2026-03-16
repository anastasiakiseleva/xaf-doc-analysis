---
uid: DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder.ObjectSpaceProviders
name: ObjectSpaceProviders
type: Property
summary: Provides access to `IObjectSpaceProviderServiceBasedBuilder` that allows you to configure [Object Spaces](xref:113707) used in your application.
syntax:
  content: IObjectSpaceProviderServiceBasedBuilder<IBlazorApplicationBuilder> ObjectSpaceProviders { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.ApplicationBuilder.IObjectSpaceProviderServiceBasedBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder}
    description: 'Allows you to configure [Object Spaces](xref:113707) used in your application. '
seealso: []
---
The following example demonstrates how to use this property:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{11-22}
using DevExpress.ExpressApp.ApplicationBuilder;
using DevExpress.ExpressApp.Blazor.ApplicationBuilder;
using DevExpress.Persistent.BaseImpl;
// ...
public class Startup {
   // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<MySolutionBlazorApplication>();
            builder.ObjectSpaceProviders
                .AddSecuredXpo((serviceProvider, options) => {
                    string connectionString = null;
                    if(Configuration.GetConnectionString("ConnectionString") != null) {
                        connectionString = Configuration.GetConnectionString("ConnectionString");
                    }
                    ArgumentNullException.ThrowIfNull(connectionString);
                    options.ConnectionString = connectionString;
                    options.ThreadSafe = true;
                    options.UseSharedDataStoreProvider = true;
                })
                .AddNonPersistent();
            // ...
        });
        // ...
    }
}
```
***