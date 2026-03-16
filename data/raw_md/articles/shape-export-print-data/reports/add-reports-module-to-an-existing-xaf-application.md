---
uid: "404243"
title: Add Reports V2 Module to an Existing XAF Application
owner: Andrey Kozhevnikov
---
# Add Reports V2 Module to an Existing XAF Application

To add the **Reports V2** module to an existing XAF application, install the appropriate NuGet package:

| Platform | Module | NuGet package |
| -------- | ------ | ------------- |
| platform-agnostic | @DevExpress.ExpressApp.ReportsV2.ReportsModuleV2 | **DevExpress.ExpressApp.ReportsV2** |
| ASP.NET Core Blazor | `DevExpress.ExpressApp.ReportsV2.Blazor.ReportsBlazorModuleV2` | **DevExpress.ExpressApp.ReportsV2.Blazor** |
| WinForms | @DevExpress.ExpressApp.ReportsV2.Win.ReportsWindowsFormsModuleV2 | **DevExpress.ExpressApp.ReportsV2.Win** |

Next, use either of the following techniques:

* [!include[<@DevExpress.ExpressApp.Blazor.ApplicationBuilder.ReportsApplicationBuilderExtensions.AddReports(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.ReportsV2.Blazor.ReportsOptions}) / @DevExpress.ExpressApp.Win.ApplicationBuilder.ReportsApplicationBuilderExtensions.AddReports(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.ReportsV2.Win.ReportsOptions})>,<ASP.NET Core Blazor / WinForms>](~/templates/ExtraModulesNote_ApplicationBuilder.md)]
* If you do not use an application builder, you can add these Modules to the [ModuleBase.RequiredModuleTypes](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection of the platform-specific Module.

The following additional steps may be required:

## Entity Framework Core-Based Application

1. Navigate to the _MySolution.Module\\BusinessObjects\\MySolutionDbContext.cs_ file and include the [](xref:DevExpress.Persistent.BaseImpl.EF.ReportDataV2) entity in the data model:  

    ```csharp
    using DevExpress.Persistent.BaseImpl.EF;
    // ...
    public class MySolutionEFCoreDbContext : DbContext {
        // ...
        public DbSet<ReportDataV2> ReportData { get; set; }
        // ...
    }
    ```	

2. Navigate to the  _MySolution.Blazor.Server\\Startup.cs_ file (ASP.NET Core Blazor) or the _MySolution.Win\\Startup.cs_ file (Windows Forms) and specify the `ReportDataType` explicitly:

    ```csharp{5}
    // ...
    builder.Modules
        .AddReports(options => {
            options.EnableInplaceReports = true;
            options.ReportDataType = typeof(DevExpress.Persistent.BaseImpl.EF.ReportDataV2);
            options.ReportStoreMode = DevExpress.ExpressApp.ReportsV2.ReportStoreModes.XML;
        })
    ```
### ASP.NET Core Blazor Application Without Application Builder

1. Navigate to the _MySolution.Blazor.Server\\Startup.cs_ file and call `AddXafReporting` in the `Startup.ConfigureServices` method to register the Reports V2 Module services in @Microsoft.Extensions.DependencyInjection.IServiceCollection:

	```csharp
	using DevExpress.ExpressApp.ReportsV2.Blazor;
	// ...
	public class Startup {
		// ...
		public void ConfigureServices(IServiceCollection services){
			//...
			services.AddXafReporting();
		}
        // ...
	}
	```
