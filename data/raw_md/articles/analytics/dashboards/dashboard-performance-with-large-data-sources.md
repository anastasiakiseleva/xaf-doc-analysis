---
uid: "117720"
seealso: []
title: Dashboard Performance With Large Data Sources
---
# Dashboard Performance With Large Data Sources

This topic lists recommendations you can use to improve performance and reduce memory consumption. You may need to use these techniques when a dashboard is bound to a large collection of objects and has performance issues.

## Limit the Number of Objects Loaded in the Dashboard Designer 

> [!Note]
> ASP.NET Core Blazor applications do not support this technique.

If you do not need to load the entire data set to the Dashboard Designer, you can use the [DashboardDataProvider.TopReturnedRecordsInDesigner](xref:DevExpress.ExpressApp.Dashboards.DashboardDataProvider.TopReturnedRecordsInDesigner) property to limit the number of loaded objects. To access the [](xref:DevExpress.ExpressApp.Dashboards.DashboardDataProvider) object, use the static [DashboardsModule.DataProvider](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.DataProvider) property. The following example demonstrates how to set the `TopReturnedRecordsInDesigner` property in the [platform-agnostic module](xref:118045)'s constructor:

**File**: _MySolution.Module\Module.cs_.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp.Dashboards;
// ...
public sealed partial class MySolutionModule : ModuleBase {
    // ...
    public MySolutionModule() {
        // ...
        DashboardsModule.DataProvider.TopReturnedRecordsInDesigner = 100;
    }
    // ...
}
```
***

## Disable Automatic Updates in the WinForms Dashboard Designer
When you perform a data-aware operation in the WinForms Dashboard Designer, the dashboard sends a query to a data source and updates itself automatically according to the returned data. It can take a significant amount of time to update the dashboard according to each change. In this case, you can disable automatic updates and update the dashboard manually when needed. For more information, refer to the following help topic: [Automatic and Manual Updates](xref:115209).

## Filter Data
When you filter the dashboard data source, the criteria is applied server side. This allows you to reduce the amount of loaded data. Refer to the following help topics for instructions on how to apply filters:

Windows Forms
:   * [Filtering](xref:16507)
    * [Passing Parameter Values](xref:16170)

ASP.NET Core Blazor
:   * [](xref:404466)
    * [Filter Data Sources](xref:117457)
    * [Dashboard Parameters](xref:117062)

## Use DataView Mode

> [!Note]
> Entity Framework Core does not support DataView mode.

### Windows Forms

Follow the steps below to retrieve a lightweight read-only list of data records instead of loading the collection of persistent objects.

1. Inherit from the [](xref:DevExpress.ExpressApp.Dashboards.DashboardDataProvider) class and override its `CreateViewService` method:

    **File**: _MySolution.Module\CustomDashboardDataProvider.cs_.

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.DashboardCommon;
    using DevExpress.ExpressApp.Dashboards;
    using DevExpress.Persistent.Base;
    // ...
    public class CustomDashboardDataProvider : DashboardDataProvider {
        protected override IObjectDataSourceCustomFillService CreateViewService(IDashboardData dashboardData) {
            if(dashboardData.Title == "Sales Overview") {
                return new DashboardViewDataSourceFillService();
            }
            return base.CreateViewService(dashboardData);
        }
    }
    ```
    ***

2. Use the static [DashboardsModule.DataProvider](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.DataProvider) property to register the custom dashboard data provider in the [platform-agnostic module](xref:118045)'s constructor:

    **File**: _MySolution.Module\Module.cs_.

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Dashboards;
    // ...
    public sealed partial class MySolutionModule : ModuleBase {
        // ...
        public MySolutionModule() {
            // ...
            DashboardsModule.DataProvider = new CustomDashboardDataProvider();
        }
        // ...
    }
    ```
    ***

### ASP.NET Core Blazor

> [!Note]
> You cannot use DataView mode in the following situations:
> - when you design dashboards; only enable DataView mode if you do not plan to edit your dashboards;
> - when you use [cross-data source filtering](xref:117060#filtering-across-data-sources).

In ASP.NET Core Blazor applications, you cannot enable DataView mode for a specific dashboard, but you can do it globally for all dashboards. See the following code snippet for an example:

**File**: _MySolution.Blazor.Server\Startup.cs_.

# [C#](#tab/tabid-csharp1)
```csharp{12-14}
using DevExpress.ExpressApp.Dashboards.Blazor.Services;
// ...
public class Startup {
    // ...
    public void ConfigureServices(IServiceCollection services) {
        // ...
        services.AddXaf(Configuration, builder => {
            // ...
            builder.Modules
                .AddDashboards(options => {
                    // ...
                    options.SetupDashboardConfigurator = (dashboardConfigurator, serviceProvider) => {
                        dashboardConfigurator.SetObjectDataSourceCustomFillService(new BlazorDashboardViewDataSourceFillService(serviceProvider));
                    };
                })
                // ...
        }
        // ...
    }
    // ...
}
```
***

## Use the SQL Data Source

You can use [SQL Data Source](xref:16151) instead of XAF Object Data Source when you [create a dashboard](xref:117450). This data source allows you to access data directly and bypass [Object Space](xref:113707) and the ORM data layer. In most cases, this improves performance. The following help topic demonstrates how to use this data source in ASP.NET Core Blazor applications: [Use SQL Data Sources (ASP.NET Core Blazor)](xref:404405).

Note the following limitations when you use this technique:
* Custom logic implemented in [business classes](xref:113664) (for example, calculated properties) does not execute.
* [Security System](xref:113366) rules are ignored and your data is not secured.
* The Module does not save credentials for non-XAF data sources inside dashboards due to security reasons. The @DevExpress.DataAccess.UI.Wizard.SqlWizardSettings.DatabaseCredentialsSavingBehavior property allows you to change this behavior. Alternatively, you can pass credentials for such data sources manually, as demonstrated in the following article: [How to: Pass Credentials to the Dashboards Module when You Use External Data Sources](https://supportcenter.devexpress.com/ticket/details/t473885/how-to-provide-credentials-for-the-dashboards-module-when-using-external-data-sources)).
