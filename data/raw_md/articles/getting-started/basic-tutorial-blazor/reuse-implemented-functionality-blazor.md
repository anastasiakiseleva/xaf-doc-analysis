---
uid: '401955'
title: Reuse Implemented Functionality
seealso:
- linkId: '118046'
---
# Reuse Implemented Functionality

This topic describes how to add [optional modules](xref:118046) to extend application functionality.

An XAF application consists of user-defined and standard XAF modules.

Modules can be platform-agnostic or platform-dependent. Platform-agnostic modules use framework features that are not specific to any platform and work on different platforms with the same code base. You can build applications for different platforms based on the same business logic if the applications refer to the same set of platform-agnostic modules.

You can extend or modify an XAF module, use [third-party modules](https://www.devexpress.com/products/net/application_framework/#community), or create your own reusable modules.

## Implement Property Value Validation

Follow the steps below to add the [Validation module](xref:113684) to your application and set up validation rules for entity objects.

1. Add the **DevExpress.ExpressApp.Validation.Blazor** NuGet package to the **SimpleProjectManager.Blazor.Server** project and the **DevExpress.ExpressApp.Validation.Win** NuGet package to the **SimpleProjectManager.Win** project. See the following topic for more information on how to install DevExpress NuGet packages: [](xref:116042).

2. In the **SimpleProjectManager.Blazor.Server** project, open the _Startup.cs_ file and add the Validation module to the application builder. Do the same in the _Startup.cs_ file of the **SimpleProjectManager.Win** project:

	# [C# (ASP.NET Core Blazor)](#tab/tabid-blazor)

	```csharp
	public class Startup {
	// ...
		public void ConfigureServices(IServiceCollection services) {
			// ...
			services.AddXaf(Configuration, builder => {
				builder.UseApplication<SimpleProjectManagerBlazorApplication>();
				builder.Modules
					// ...
					.AddValidation();
				// ...
			});
			// ...
		}
	}
	```

	# [C# (Windows Forms)](#tab/tabid-winforms)

	```csharp
	public class ApplicationBuilder : IDesignTimeApplicationFactory {
		public static WinApplication BuildApplication(string connectionString) {
		var builder = WinApplication.CreateBuilder();
		builder.UseApplication<SimpleProjectManagerWindowsFormsApplication>();
		builder.Modules
		//...
			.AddValidation();

		}
	}
	```
	
	***

3. Open the _SimpleProjectManager.Module\BusinessObjects\ProjectTask.cs_ file and apply the [](xref:DevExpress.Persistent.Validation.RuleCriteriaAttribute) to the `ProjectTask` class:

	```csharp
	using DevExpress.Persistent.Validation;
	// ...
	[RuleCriteria("EndDate >= StartDate", 
		CustomMessageTemplate = "Start Date must be less than End Date")]
	public class ProjectTask : BaseObject {
	    // ...
	}
	```

4. Run the application and change the task's end date. When you save the changes, XAF validates the task according to specified settings.

   ASP.NET Core Blazor

   :   ![|ASP.NET Core Blazor Validation, DevExpress|](~/images/SPM_ModulesRuntime_Blazor.png)

   Windows Forms

   :   ![Windows Forms Validation, DevExpress](~/images/SPM_ModulesRuntime_winforms.png)

## Highlight Property Editors

Follow the steps below to add the [Conditional Appearance](xref:113286) module to your application and highlight all tasks where status is "In progress".

1. Add the **DevExpress.ExpressApp.ConditionalAppearance** NuGet package to the **SimpleProjectManager.Module** project.

2. In the **Solution Explorer**, go to the **SimpleProjectManager.Module** project and open the _Module.cs_ file. Add the Conditional Appearance module to the [](xref:DevExpress.ExpressApp.ModuleBase.RequiredModuleTypes) collection.

	```csharp{9}
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.Updating;

	namespace SimpleProjectManager.Module;

	public sealed class SimpleProjectManagerModule : ModuleBase {
		public SimpleProjectManagerModule() {
			// ...
			RequiredModuleTypes.Add(typeof(DevExpress.ExpressApp.ConditionalAppearance.ConditionalAppearanceModule));
		}
		
		// ...
	}
	```
3. Open the `ProjectTask` class and apply `AppearanceAttribute` as displayed in the following code snippet:

	```csharp
	// ...
	using DevExpress.ExpressApp.ConditionalAppearance;

	namespace SimpleProjectManager.Module.BusinessObjects
	{
		// ...
		[Appearance("InProgress", TargetItems = "Subject;AssignedTo",
		Criteria = "Status = 1", BackColor = "LemonChiffon")]
		public class ProjectTask : BaseObject
		{
			// ...
		}

		// ...
	}
	```
	[`TargetItems`]: xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems
	[`Criteria`]: xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Criteria
	[`BackColor`]: xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor
	[`Appearance`]: xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute

4. Run the application. The task where status is "In progress" is highlighted now.

   ASP.NET Core Blazor -- List View
   :   ![|The ASP.NET Core Blazor conditional appearance in a List View, DevExpress|](~/images/spm-conditional-appearance-blazor-devexpress.png)
ASP.NET Core Blazor -- Detail View
   :   ![|The ASP.NET Core Blazor conditional appearance in a Detail View, DevExpress|](~/images/spm-conditional-appearance-detail-blazor-devexpress.png)

   Windows Forms -- List View
   :   ![The Windows Forms conditional appearance in a List View, DevExpress](~/images/spm-conditional-appearance-winforms-devexpress.png)
Windows Forms -- Detail View
   :   ![The Windows Forms conditional appearance in a Detail View, DevExpress](~/images/spm-conditional-appearance-detail-winforms-devexpress.png)
