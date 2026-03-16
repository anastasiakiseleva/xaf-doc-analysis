---
uid: DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions.SetupDashboardConfigurator
name: SetupDashboardConfigurator
type: Property
summary: Allows you to customize the [Dashboard Configurator](xref:403544).
syntax:
  content: public Action<BlazorDashboardConfigurator, IServiceProvider> SetupDashboardConfigurator { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator,System.IServiceProvider}
    description: The delegate that allows you to customize the [Dashboard Configurator](xref:403544).
seealso: []
---
The following example demonstrates how to specify this property: 

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp-1)
```csharp{15-18}
using DevExpress.DashboardAspNetCore;
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
            builder.Modules
                // ...
                .AddDashboards(options => {
                    options.SetupDashboardConfigurator = (dashboardConfigurator, services) => {
                        var configuration = services.GetRequiredService<IConfiguration>();
                        dashboardConfigurator.SetConnectionStringsProvider(new DashboardConnectionStringsProvider(configuration));
                    };
                });
            // ...
        });
        // ...
    }
}
```
***