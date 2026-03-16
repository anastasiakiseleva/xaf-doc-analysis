---
uid: "404405"
title: Use SQL Data Sources (ASP.NET Core Blazor)
owner: Anastasiya Kisialeva
---
# Use SQL Data Sources (ASP.NET Core Blazor)

This topic explains how use an SQL data source with Dashboards. The data source content is based on the application's Business Model.

## Enable SQL Data Sources

To enable SQL data sources in your application, supply the dashboard configurator with a [connection strings provider](xref:DevExpress.DataAccess.Web.IDataSourceWizardConnectionStringsProvider) in the _MySolution.Blazor.Server\Startup.cs_ file. Review the following code sample:

```csharp{2,14-16}
// ...
using DevExpress.DashboardAspNetCore;
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
                    options.DashboardDataType = typeof(DashboardData);
                    options.SetupDashboardConfigurator = (dashboardConfigurator, serviceProvider) => {
                        dashboardConfigurator.SetConnectionStringsProvider(new DashboardConnectionStringsProvider(Configuration));
                    };
                });
            // ...
        });
        // ...
    }
}
```
[`SetConnectionStringsProvider`]: xref:DevExpress.DashboardWeb.DashboardConfigurator.SetConnectionStringsProvider(DevExpress.DataAccess.Web.IDataSourceWizardConnectionStringsProvider)
[`DashboardConnectionStringsProvider`]: xref:DevExpress.DashboardAspNetCore.DashboardConnectionStringsProvider
[`dashboardConfigurator`]: xref:DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator
[`AddDashboards`]: xref:DevExpress.ExpressApp.Blazor.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards*

Use the [DashboardConnectionStringsProvider](xref:DevExpress.DashboardAspNetCore.DashboardConnectionStringsProvider) class to create new [SQL data sources](xref:117720#use-the-sql-data-source) based on connection strings from the _MySolution.Blazor.Server\appsettings.json_ file.

## Allow Custom SQL Queries

To enable [custom SQL queries](xref:117193) in your application, follow the steps below:

1. In the _MySolution.Blazor.Server\Startup.cs_ file, enable custom SQL queries on the server side:

    ```csharp{6}
    // ...
    .AddDashboards(options => {
        // ...
        options.SetupDashboardConfigurator = (dashboardConfigurator, serviceProvider) => {
            // ...
            dashboardConfigurator.AllowExecutingCustomSql = true;
        };
    })
    ```

2. In the _MySolution.Blazor.Server_ project, create a custom Razor component named `DashboardSettingsHelper` with the following definition:

    ```Razor
    @using DevExpress.DashboardBlazor

    @ChildContent
    <DxExtensions>
        <DxDataSourceWizard EnableCustomSql="true"/>
    </DxExtensions>

    @code {
        [Parameter] public RenderFragment ChildContent { get; set; }
        public static RenderFragment Create(RenderFragment childContent) =>
            @<DashboardSettingsHelper ChildContent=childContent />;
    }
    ```

    This Razor component updates settings of a client-side [DxDashboard](xref:DevExpress.DashboardBlazor.DxDashboard) control to allow end-users to write custom SQL queries.

3. In the _MySolution.Blazor.Server\Controllers_ folder, create the following Controller:

    ```csharp
    using DevExpress.ExpressApp;
    using DevExpress.ExpressApp.Dashboards.Blazor.Components;
    using DevExpress.Persistent.Base;
    using MySolution.Blazor.Server;

    public class DashboardCustomSqlQueryController : ObjectViewController<DetailView, IDashboardData> {
        protected override void OnActivated() {
            base.OnActivated();
            View.CustomizeViewItemControl<BlazorDashboardViewerViewItem>(this, CustomizeDashboardViewerViewItem);
        }
        void CustomizeDashboardViewerViewItem(BlazorDashboardViewerViewItem dashboardViewerViewItem) {
            dashboardViewerViewItem.ComponentModel.ChildContent = DashboardSettingsHelper.Create(dashboardViewerViewItem.ComponentModel.ChildContent);
        }
    }
    ```

    This controller uses the Razor component created in the previous step to customize the client-side [DxDashboard](xref:DevExpress.DashboardBlazor.DxDashboard) control. The code modifies the dashboard's [component model](xref:404767) instead of the component itself.

End-users can now write custom SQL queries.
