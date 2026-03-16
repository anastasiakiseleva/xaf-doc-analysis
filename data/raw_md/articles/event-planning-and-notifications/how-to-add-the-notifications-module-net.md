---
uid: "404940"
title: How to Add the Notifications Module
owner: Anastasiya Kisialeva
---
# How to Add the Notifications Module

This article describes how to add the [Notifications](xref:113690) module to ASP.NET Core Blazor and Windows Forms applications.

The module allows you to display reminders for [scheduler](xref:112811) appointments or any custom business object.

## Step-by-Step Instructions

1. Add the **DevExpress.ExpressApp.Notifications** NuGet package to the **MySolution.Module** project. See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042).

2. In the **Solution Explorer**, go to the **MySolution.Module** project and open the _Module.cs_ file. Add the Notifications module to the [](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection.
	
	```csharp{7-9}
    //...
	namespace MySolution.Module;
	//...
	public sealed class MySolutionModule : ModuleBase {
    	public MySolutionModule() {
        	//...
        	RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.Notifications.NotificationsModule));
    	}
	//...
	}
	```

4. Add the following NuGet packages to platform-specific projects in your application:
   * _MySolution.Blazor.Server_ project: **DevExpress.ExpressApp.Notifications.Blazor**
   * _MySolution.Win_ project: **DevExpress.ExpressApp.Notifications.Win**

5. In ASP.NET Core Blazor application, navigate to the _MySolution.Blazor.Server\Startup.cs_ file and call the @DevExpress.ExpressApp.Blazor.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Blazor.NotificationsOptions}) method.

   In Windows Forms application, navigate to the _MySolution.Win\Startup.cs_ file and call the @DevExpress.ExpressApp.Win.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Win.NotificationsOptions}) method.

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
					.AddNotifications();
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
            	.AddNotifications()
				//...
    	}
	//...
	}
	```
	***
	
> [!TIP]
> For more information about this module, refer to the following topic: [How to: Use Notifications with the Scheduler Event](xref:113687).
