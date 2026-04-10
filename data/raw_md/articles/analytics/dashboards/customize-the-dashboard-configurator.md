---
uid: "403544"
title: Customize the Dashboard Configurator (ASP.NET Core Blazor)
seealso:
  - linkId: '404466'
  - linkId: 117680
  - linkId: 119823
  - linkId: 118651
---
# Customize the Dashboard Configurator (ASP.NET Core Blazor)

This topic describes how to access the [DashboardConfigurator](xref:DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator) object that allows you to manage global dashboard options. For example, you can customize the dashboard storage or specify a connection string provider for [SQL data sources](xref:404405). 

## Customize the Default Configurator

To access the dashboard configurator, define the [DashboardsOptions.SetupDashboardConfigurator](xref:DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions.SetupDashboardConfigurator) delegate in the `IBlazorApplicationBuilder.Modules.AddDashboards` method.

The following example demonstrates how to specify a connection string provider that allows users to create new [SQL data sources](xref:117720#use-the-sql-data-source) based on connection strings listed in  _MySolution.Blazor.Server\appsettings.json_. Open _MySolution.Blazor.Server\Startup.cs_ and adjust the code to match the snippet below:

```csharp
using DevExpress.ExpressApp.Dashboards.Blazor;
using DevExpress.DashboardAspNetCore;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            builder.UseApplication<YourSolutionNameBlazorApplication>();
            builder.Modules
                // ...
                .AddDashboards(options => {
                    options.DashboardDataType = typeof(DevExpress.Persistent.BaseImpl.DashboardData);
                    options.SetupDashboardConfigurator = (configurator, services) => {
                        var configuration = services.GetRequiredService<IConfiguration>();
                        configurator.SetConnectionStringsProvider(new DashboardConnectionStringsProvider(configuration));
                    };
                });
            // ...
        })
    }
    // ...
}
```

[`SetConnectionStringsProvider`]: xref:DevExpress.DashboardWeb.DashboardConfigurator.SetConnectionStringsProvider(DevExpress.DataAccess.Web.IDataSourceWizardConnectionStringsProvider)
[`DashboardConnectionStringsProvider`]: xref:DevExpress.DashboardAspNetCore.DashboardConnectionStringsProvider
[`dashboardConfigurator`]: xref:DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator
[`AddXafDashboards`]: xref:DevExpress.ExpressApp.Dashboards.Blazor.StartupExtensions.AddXafDashboards(Microsoft.Extensions.DependencyInjection.IServiceCollection,System.Action{DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator,System.IServiceProvider})

## Create a Custom Configurator

1. In the _MySolution.Blazor.Server\Services_ folder, create a @DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator descendant.
2. In the constructor of the newly created class, request the required services.
3. Declare a public method (for example, `Setup`) that initializes the configurator. Do not initialize your configurator in a constructor. After a dashboard configurator instance is created, the service provider initializes it, which can potentially overwrite the logic declared in a constructor.

    ```csharp
    using DevExpress.DashboardAspNetCore;
    using DevExpress.ExpressApp.Dashboards.Blazor.Services;
    using Microsoft.Extensions.Configuration;
    
    public class CustomDashboardConfigurator : BlazorDashboardConfigurator {
        private readonly IConfiguration configuration;
        public CustomDashboardConfigurator(IConfiguration configuration) {
            this.configuration = configuration;
        }
        public void Setup() {
            SetConnectionStringsProvider(new DashboardConnectionStringsProvider(configuration));
        }
    }
    ```
    [`BlazorDashboardConfigurator`]: xref:DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator

4. Register your custom configurator as a scoped service in the _MySolution.Blazor.Server\Startup.cs_ file. In the delegate passed to the `AddDashboards` method, call the method that initializes this configurator (`Setup` in this example):

    ```csharp{9,17}
    using DevExpress.ExpressApp.Dashboards.Blazor;
    using DevExpress.ExpressApp.Dashboards.Blazor.Services;
    using DevExpress.DashboardAspNetCore;
    // ...
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services) {
            // ...
            services.AddScoped<BlazorDashboardConfigurator, CustomDashboardConfigurator>();
            services.AddXaf(Configuration, builder => {
                builder.UseApplication<YourSolutionNameBlazorApplication>();
                builder.Modules
                    // ...
                    .AddDashboards(options => {
                        options.DashboardDataType = typeof(DevExpress.Persistent.BaseImpl.DashboardData);
                        options.SetupDashboardConfigurator = (configurator, services) => {
                            ((CustomDashboardConfigurator)configurator).Setup();
                        };
                    });
                // ...
            })
        }
        // ...
    }
    ```
