---
uid: "404214"
seealso:
- linkId: 112811
- linkId: 112813
- linkId: 113688
title: 'How to: Add the Scheduler Module'
owner: Anastasiya Kisialeva
---
# How to: Add the Scheduler Module

This article describes how to add the [Scheduler](xref:112812) module to Windows Forms and ASP.NET Core Blazor applications.

The module implements a calendar component for scheduling appointments and events.

## Step-by-Step Instructions

1. Add the **DevExpress.ExpressApp.Scheduler** NuGet package to the **MySolution.Module** project. See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042).

2. In the **Solution Explorer**, go to the **MySolution.Module** project and open the _Module.cs_ file. Add the Scheduler module to the [](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection. Then, add the `Event` and `Resource` classes to the [](xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes) collection.
	
	In Entity Framework Core-based applications:

	```csharp{7-9}
    //...
	namespace MySolution.Module;
	//...
	public sealed class MySolutionModule : ModuleBase {
    	public MySolutionModule() {
        	//...
        	RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.Scheduler.SchedulerModuleBase));
        	AdditionalExportedTypes.Add(typeof(DevExpress.Persistent.BaseImpl.EF.Event));
        	AdditionalExportedTypes.Add(typeof(DevExpress.Persistent.BaseImpl.EF.Resource));
    	}
	//...
	}
	```
	[`AdditionalExportedTypes`]: xref:DevExpress.ExpressApp.ModuleBase.AdditionalExportedTypes
	[`RequiredModuleTypes`]: xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes

	In XPO-based applications:

	```csharp{7-9}
    //...
	namespace MySolution.Module;
	//...
	public sealed class MySolutionModule : ModuleBase {
    	public MySolutionModule() {
        	//...
        	RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.Scheduler.SchedulerModuleBase));
        	AdditionalExportedTypes.Add(typeof(DevExpress.Persistent.BaseImpl.Event));
        	AdditionalExportedTypes.Add(typeof(DevExpress.Persistent.BaseImpl.Resource));
    	}
	//...
	}
	```

3. _Optional._ If you use [Entity Framework Core](https://learn.microsoft.com/en-us/ef/core/), go to the _MySolution.Module\BusinessObjects_ folder, open the _MySolutionDbContext.cs_ file. Then, register the `Event` and `Resource` types in the application's `DbContext`:
	
	```csharp
	namespace MyApplication.Module.BusinessObjects;
	//..
	public class MySolutionDbContext : DbContext {
		// ..
		public DbSet<Event> Events { get; set; }
		public DbSet<Resource> Resources { get; set; }
		}
	```

	[!include[](~/templates/update-ef-core.md)]

4. Add the following NuGet packages to platform-specific projects in your application:
   * **MySolution.Blazor.Server** project: **DevExpress.ExpressApp.Scheduler.Blazor**
   * **MySolution.Win** project: **DevExpress.ExpressApp.Scheduler.Win**

5. In ASP.NET Core Blazor application, navigate to the _MySolution.Blazor.Server\Startup.cs_ file and call the @DevExpress.ExpressApp.Blazor.ApplicationBuilder.SchedulerApplicationBuilderExtensions.AddScheduler(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Scheduler.Blazor.SchedulerOptions}) method.

   In Windows Forms application, navigate to the _MySolution.Win\Startup.cs_ file and call the @DevExpress.ExpressApp.Win.ApplicationBuilder.SchedulerApplicationBuilderExtensions.AddScheduler(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Scheduler.Win.SchedulerOptions}) method.

	# [C# (ASP.NET Core Blazor)](#tab/tabid-csharp-blazor)
	 
	```csharp{9}
	public class Startup {
	// ...
		public void ConfigureServices(IServiceCollection services) {
			// ...
			services.AddXaf(Configuration, builder => {
				builder.UseApplication<MySolutionBlazorApplication>();
				builder.Modules
					// ...
					.AddScheduler();
				// ...
			});
			// ...
		}
	}
	```

   # [C# (Windows Forms)](#tab/tabid-csharp-xpo)

	```csharp{9}
	//...
	namespace MySolution.Win;
    
	public class ApplicationBuilder : IDesignTimeApplicationFactory {
    	public static WinApplication BuildApplication(string connectionString) {
        	var builder = WinApplication.CreateBuilder();
        	builder.UseApplication<MySolutionWindowsFormsApplication>();
        	builder.Modules
            	.AddScheduler()
				//...
    	}
	//...
	}
	```
	***
	
6. Build the project and run the application. The **Scheduler Event** item appears in the navigation control.

   ASP.NET Core Blazor
   :   ![|Scheduler Module ASP.NET Core Blazor, DevExpress|](~/images/how-to-add-scheduler-module-blazor.png)

   Windows Forms
   :   ![|Scheduler Module Windows Forms, DevExpress|](~/images/how-to-add-scheduler-module-result.png)

> [!TIP]
> XAF has a special Notifications module you can use to set notifications for events. For more information about this module, refer to the following topic: [How to: Use Notifications with the Scheduler Event](xref:113687).
