---
uid: "117449"
title: Dashboards Module
owner: Ekaterina Kiseleva
seealso:
  - linkId: "117450"
  - linkId: "403400"
  - linkId: "117453"
  - linkId: "117454"
---
# Dashboards Module
<!--TODO: review the topic for webforms content -->
The **Dashboards Module** integrates [DevExpress Dashboard](xref:12049) controls into ASP.NET Core Blazor and Windows Forms XAF applications.

![Dashboards_XCRM](~/images/dashboards_xcrm125563.png)

[!include[<Dashboards Module>](~/templates/main-demo-tip.md)]

## Dashboards Module Capabilities
{|
|-

! For users
! For developers
|-

| * Create dashboards at runtime and persist them. Dashboards are stored with other [business objects](xref:113664) in the application database.
* View and modify existing dashboards in the **Dashboards** List View. You can use the **Dashboards** [navigation item](xref:113198) to invoke this View.
| * Create predefined dashboards that are available to users after an application's deployment.
* Create [navigation items](xref:113198) associated with individual dashboards.
* Customize the dashboard's control options and behavior.
|}

> [!NOTE]
> The [](xref:DevExpress.ExpressApp.DashboardView) and Dashboard Module are different XAF concepts. Dashboard Views display multiple XAF Views in a single [Frame](xref:112608) - they do not use DevExpress Dashboard controls.

## Dashboards Module Components

### Modules

| Platform | Module | NuGet package |
| -------- | ------ | ------------- |
| Platform-agnostic | [](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule) | **DevExpress.ExpressApp.Dashboards** |
| WinForms | [](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardsWindowsFormsModule) | **DevExpress.ExpressApp.Dashboards.Win** |
| ASP.NET Core Blazor | [](xref:DevExpress.ExpressApp.Dashboards.Blazor.DashboardsBlazorModule) | **DevExpress.ExpressApp.Dashboards.Blazor** |

### Integrated DevExpress Controls

ASP.NET Core Blazor
:   [](xref:DevExpress.DashboardBlazor.DxDashboard)
Windows Forms
:   [](xref:DevExpress.DashboardWin.DashboardDesigner)  
    [](xref:DevExpress.DashboardWin.DashboardViewer)

### View Items

The Dashboards Module uses the following [View Items](xref:112612) to host dashboard controls in ASP.NET Core Blazor and Windows Forms XAF applications:

* @DevExpress.ExpressApp.Dashboards.Blazor.Components.BlazorDashboardViewerViewItem
* [](xref:DevExpress.ExpressApp.Dashboards.Win.WinDashboardViewerViewItem)

### Application Model Extensions

The Dashboards Module extends the [Application Model](xref:112579) with the [](xref:DevExpress.ExpressApp.Dashboards.IModelDashboardNavigationItem) node and adds the [IModelClassDashboardsVisibility.IsVisibleInDashboards](xref:DevExpress.ExpressApp.Model.IModelClassDashboardsVisibility.IsVisibleInDashboards) property to the [](xref:DevExpress.ExpressApp.Model.IModelClass) node.

## Dashboard Data Type

The Module uses the following [built-in business objects](xref:112571) (entities) that implement the [](xref:DevExpress.Persistent.Base.IDashboardData) interface to store dashboards:

* [DevExpress.Persistent.BaseImpl.DashboardData](xref:DevExpress.Persistent.BaseImpl.DashboardData) (in XPO-based applications)
* [DevExpress.Persistent.BaseImpl.EF.DashboardData](xref:DevExpress.Persistent.BaseImpl.EF.DashboardData) (in EF Core-based applications)

You can also use a custom dashboard data type. To do this, follow these steps:
1. Inherit from `DashboardData` or implement the `IDashboardData` interface.
2. Add the required properties and register the custom type in DbContext.
3. Specify the custom type in the following properties:

   * [Dashboards.Blazor.DashboardsOptions.DashboardDataType](xref:DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions.DashboardDataType) property in the _YourSolutionName\Blazor.Server\Startup.cs_ file
   * [Dashboards.Win.DashboardsOptions.DashboardDataType](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardsOptions.DashboardDataType) property in the _YourSolutionName\Win\Startup.cs_ file

> [!TIP]
>  To display the `DashboardData` object's Detail View, use the technique listed in the following help topic: [Ways to Show a View](xref:112803).

## Add the Dashboards Module to Your Application

Use either of the following techniques to add the Dashboards Module:

* [!include[ExtraModulesNote](~/templates/extramodulesnote1111180.md)]
* [!include[<@DevExpress.ExpressApp.Win.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Dashboards.Win.DashboardsOptions}) / @DevExpress.ExpressApp.Blazor.ApplicationBuilder.DashboardsApplicationBuilderExtensions.AddDashboards(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Dashboards.Blazor.DashboardsOptions})>,<WinForms / ASP.NET Core Blazor>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]
* If you do not use an application builder, you can add these Modules to the [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection of the platform-specific Module.

> [!TIP]
> Make sure that you installed the appropriate platform-specific NuGet package.

The following additional steps may be required:

### Entity Framework Core-Based Application

1. Navigate to the _MySolution.Module\\BusinessObjects\\MySolutionDbContext.cs_ file and include the [](xref:DevExpress.Persistent.BaseImpl.EF.DashboardData) entity in the data model:  

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    public class MySolutionEFCoreDbContext : DbContext {
        // ...
        public DbSet<DashboardData> DashboardData { get; set; }
        // ...
    }
    ```	

2. Navigate to the _MySolution.Blazor.Server\\Startup.cs_ file (ASP.NET Core Blazor) or the _MySolution.Win\\Startup.cs_ file (Windows Forms) and specify the `DashboardDataType` explicitly:

    ```csharp{4}
    // ...
    builder.Modules
        .AddDashboards(options => {
            options.DashboardDataType = typeof(DevExpress.Persistent.BaseImpl.EF.DashboardData);
        })
    ```

### ASP.NET Core Blazor Application Without Application Builder

1. Open the following file: _MySolution.Blazor.Server\\Startup.cs_.

2. In the `Startup.ConfigureServices` method, call the [AddXafDashboards](xref:DevExpress.ExpressApp.Dashboards.Blazor.StartupExtensions.AddXafDashboards(Microsoft.Extensions.DependencyInjection.IServiceCollection,System.Action{DevExpress.ExpressApp.Dashboards.Blazor.Services.BlazorDashboardConfigurator,System.IServiceProvider})) method to register Dashboards Module services.
3. In the `Startup.Configure` method, call the [MapXafDashboards](xref:DevExpress.ExpressApp.Dashboards.Blazor.StartupExtensions.MapXafDashboards(Microsoft.AspNetCore.Routing.IEndpointRouteBuilder,System.String,System.String)) method to configure endpoints for the Dashboards Module.

    ```csharp
    using DevExpress.ExpressApp.Dashboards.Blazor;
    // ...
    public class Startup {
        // ...
        public void ConfigureServices(IServiceCollection services){
            //...
            services.AddXafDashboards();
        }
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env) {
            // ...
            app.UseEndpoints(endpoints => {
                endpoints.MapXafDashboards();
                // ...
            })
        }
    }
    ```

## Troubleshooting

For more information on how to resolve problems that can occur when you use the **Dashboards Module**, refer to the following topic: [](xref:404346).
