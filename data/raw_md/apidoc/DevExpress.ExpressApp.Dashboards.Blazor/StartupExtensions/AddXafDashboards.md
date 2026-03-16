---
uid: DevExpress.ExpressApp.Dashboards.Blazor.StartupExtensions.AddXafDashboards(Microsoft.Extensions.DependencyInjection.IServiceCollection,System.Action{DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator,System.IServiceProvider})
name: AddXafDashboards(IServiceCollection, Action<BlazorDashboardConfigurator, IServiceProvider>)
type: Method
summary: Registers the required [Dashboards Module](xref:117449) services in the application's @Microsoft.Extensions.DependencyInjection.IServiceCollection.
syntax:
  content: public static IServiceCollection AddXafDashboards(this IServiceCollection services, Action<BlazorDashboardConfigurator, IServiceProvider> configure = null)
  parameters:
  - id: services
    type: Microsoft.Extensions.DependencyInjection.IServiceCollection
    description: The collection of services registered in your application.
  - id: configure
    type: System.Action{DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator,System.IServiceProvider}
    defaultValue: "null"
    description: A delegate that allows you to customize the **BlazorDashboardConfigurator** settings.
  return:
    type: Microsoft.Extensions.DependencyInjection.IServiceCollection
    description: The collection of services registered in your application. Allows you to chain further service registrations.
seealso: []
---
Call this method in the **Startup.ConfigureServices** method when you [add the Dashboards Module to your ASP.NET Core Blazor application](xref:117449#add-the-dashboards-module-to-your-application). The following example demonstrates how to specify a connection string provider to allow users to create new [SQL data sources](xref:117720#use-the-sql-data-source) based on connection strings from the _MySolution.Blazor.Server\appsettings.json_ file:

# [C# (Startup.cs)](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Dashboards.Blazor;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services){
        //...
        services.AddXafDashboards((dashboardConfigurator, services) => {
            var configuration = services.GetRequiredService<IConfiguration>();
            dashboardConfigurator.SetConnectionStringsProvider(new DashboardConnectionStringsProvider(configuration));
        });
        // ...
    }
    // ...
}
```
***
