---
uid: "113672"
title: 'How to: Add a Custom Column to the Reports List'
seealso:
  - linkId: 113674
---
# How to: Add a Custom Column to the Reports List

This topic describes how to customize the persistent class for storing reports by adding extra information, such as a `Category` property. This property appears in the `Reports` List View and allows users to group, sort, or filter reports accordingly.

> [!ImageGallery]
> 
> ![Custom report column in Blazor App](~/images/xaf-blazor-custom-report-column.png)
> ![Custom report column in Win App](~/images/xaf-win-custom-report-column.png)


[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

## Step 1. Create a Custom Report Data Type

Inherit a new `MyReportDataV2` class from the `ReportDataV2` class and declare the `Category` property.

**File:** _MySolution.Module\BusinessObjects\MyReportDataV2.cs_

# [EF Core](#tab/tabid-EF-Core)
 
```csharp
public class MyReportDataV2 : DevExpress.Persistent.BaseImpl.EF.ReportDataV2 {
    public virtual string Category { get;set; }
}
```
# [XPO](#tab/tabid-XPO)
 
```csharp
public class MyReportDataV2 : DevExpress.Persistent.BaseImpl.ReportDataV2 {
    public MyReportDataV2(Session session) : base(session) { }
    private string category;
    public string Category {
        get { return category; }
        set { SetPropertyValue(nameof(Category), ref category, value); }
     }
}
```
***

If you use EF Core, add the `MyReportDataV2` class to `DbContext`:

**File:** _SolutionName.Module\BusinessObjects\SolutionNameDbContext.cs_

```csharp
public class SolutionNameDbContext : DbContext {
    // ...
    public DbSet<MyReportDataV2> MyReportDataV2 { get; set; }
}
```

## Step 2. Specify the ReportDataType Property

Assign the  `MyReportDataV2` type to the @DevExpress.ExpressApp.ReportsV2.ReportOptions.ReportDataType property:

**Files:** _SolutionName.WebApi\Startup.cs_, _SolutionName.Blazor.Server\Startup.cs_, _SolutionName.Win\Startup.cs_, _SolutionName.MiddleTier\Startup.cs_.


```csharp
// ...
builder.Modules
	.AddReports(options => {
		options.ReportDataType = typeof(MyReportDataV2);
		// ...
```
## Step 3. Add the New Property to the Report Wizard

> [!tip]
> You can [customize the ReportsStorage class](xref:113674) to update the property value in code if you do not want the additional property to be initialized by a user.

1. In the platform-agnostic module project, inherit from the `NewXafReportWizardParameters` class and declare the `Category` string property.
	
	**File:** _MySolution.Module\CustomReportWizardParameters.cs_

	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.DC;
	using DevExpress.ExpressApp.ReportsV2;
	using DevExpress.XtraReports.UI;
	// ...
	[DomainComponent]
	public class CustomReportWizardParameters : NewReportWizardParameters {
	    public CustomReportWizardParameters(XtraReport report, Type reportDataType) : 
	        base(report, reportDataType) { }
	    public string Category { get; set; }
	    public override void AssignData(IReportDataV2Writable reportData) {
	        base.AssignData(reportData);
	        if (reportData is MyReportDataV2) {
	            ((MyReportDataV2)reportData).Category = Category;
	        }
	    }
	}
	```
	***

2. In the ASP.NET Core Blazor project, create a [View Controller](xref:112621). Access the standard @DevExpress.ExpressApp.ReportsV2.Blazor.BlazorReportServiceController and subscribe to its @DevExpress.ExpressApp.ReportsV2.Blazor.BlazorReportServiceController.NewReportWizardShowing event. In the event handler, pass an instance of the `CustomReportWizardParameters` class to the Report Wizard.

	**File:** _MySolution.Blazor.Server\Controllers\ReportWizardModifyController.cs_

	# [C#](#tab/tabid-csharp1)

	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.ReportsV2.Blazor;
	// ...
	public class ReportWizardModifyController : ViewController {
		BlazorReportServiceController reportServiceController;
		public ReportWizardModifyController() { }
		protected override void OnActivated() {
			base.OnActivated();
			reportServiceController = Frame.GetController<BlazorReportServiceController>();
			if(reportServiceController != null) {
				reportServiceController.NewReportWizardShowing += ReportServiceController_NewReportWizardShowing;
			}
		}
		private void ReportServiceController_NewReportWizardShowing(object sender, BlazorNewReportWizardShowingEventArgs e) {
			if(!e.ReportDataType.Equals(typeof(MyReportDataV2)))
				return;
			CustomReportWizardParameters newReportParamsObject = 
			new CustomReportWizardParameters(e.WizardParameters.Report, e.WizardParameters.ReportDataType);
			newReportParamsObject.Category = "Default";
			e.WizardParameters = newReportParamsObject;
		}
		protected override void OnDeactivated() {
			reportServiceController.NewReportWizardShowing -= ReportServiceController_NewReportWizardShowing;
			reportServiceController = null;
			base.OnDeactivated();
		}
	}
	```

	***

3. In the WinForms project, perform similar actions. Create a [View Controller](xref:112621). Access the standard @DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController and subscribe to its @DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.NewXafReportWizardShowing event. In the event handler, pass an instance of the `CustomReportWizardParameters` class to the Report Wizard.

	**File:** _MySolution.Win\Controllers\ReportWizardModifyController.cs_

	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.ReportsV2.Win;
	// ...
	public class ReportWizardModifyController : ViewController {
	    WinReportServiceController reportServiceController;
	    public ReportWizardModifyController() { }
	    protected override void OnActivated() {
	        base.OnActivated();
	        reportServiceController = Frame.GetController<WinReportServiceController>();
	        if (reportServiceController != null) {
	            reportServiceController.NewXafReportWizardShowing +=
	                reportServiceController_NewXafReportWizardShowing;
	        }
	    }
	    protected override void OnDeactivated() {
	        reportServiceController.NewXafReportWizardShowing -=
	            reportServiceController_NewXafReportWizardShowing;
	        reportServiceController = null;
	        base.OnDeactivated();
	    }
	    void reportServiceController_NewXafReportWizardShowing(object sender,
	        NewXafReportWizardShowingEventArgs e) {
	        if (!e.ReportDataType.Equals(typeof(MyReportDataV2))) return;
	        CustomReportWizardParameters newReportParamsObject = new
	            CustomReportWizardParameters(e.WizardParameters.Report, e.WizardParameters.ReportDataType);
	        newReportParamsObject.Category = "Default";
	        e.WizardParameters = newReportParamsObject;
	    }
	}
	```
	***

## Customize the Report Wizard Parameters Window

Steps in the previous section add the following [Detail Views](xref:112611) to the Application Model:

* **View > CustomReportWizardParameters > CustomReportWizardParameters_DetailView**
* **View > SolutionName.Module.BusinessObjects > MyReportData > MyReportData_DetailView**

Start the [Model Editor](xref:112582) and adjust these Detail View layouts to customize the Report Wizard Parameters window. For detailed instructions, see the following topic: <xref:112817>.

## Specify Custom Column Values in Predefined Static Reports

The approach described above works for user-created reports generated with the Report Wizard and saved through the standard storage pipeline. Predefined static reports require additional handling because they are created and registered in code and do not use the same UI flow.

To specify a custom property for predefined reports (for example, the `Category` field), assign the value programmatically as follows:

1. Create a `PredefinedReportDataContainer` descendant with a property that holds a category name:

	# [SolutionName.Module.PredefinedReportDataContainerEx.cs](#tab/tabid-sc)
	```csharp
	using DevExpress.ExpressApp.ReportsV2;

	namespace SolutionName.Module {
		public class PredefinedReportDataContainerEx : PredefinedReportDataContainer {
			public PredefinedReportDataContainerEx(Type reportType, string displayName, string categoryName) : base(reportType, displayName) {
				Category = categoryName;
			}
			public string Category { get; set; }
		}
	}
	```
	***

2. Use this descendant to create a predefined report with a category name in the @DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.GetModuleUpdaters* method: 
	# [SolutionName.Module.Module.cs](#tab/tabid-sc)
	```csharp
	// ...
	public override IEnumerable<ModuleUpdater> GetModuleUpdaters(IObjectSpace objectSpace, Version versionFromDB) {
		ModuleUpdater updater = new DatabaseUpdate.Updater(objectSpace, versionFromDB);
		PredefinedReportsUpdater predefinedReportsUpdater = new PredefinedReportsUpdater(Application, objectSpace, versionFromDB);
		predefinedReportsUpdater.PredefinedReports.Add(new PredefinedReportDataContainerEx(typeof(PredefinedReport1), "Employee Information", "Predefined Report"));
		return new ModuleUpdater[] { updater, predefinedReportsUpdater };
	}
	// ...
	```
	***

3. Create a `ReportStorageService` descendant and override its `CopyFrom` method so that it copies a category name to a created MyReportDataV2:

	# [SolutionName.Module.CustomReportsStorage.cs](#tab/tabid-sc)
	```csharp
	using DevExpress.ExpressApp;
	using DevExpress.ExpressApp.DC;
	using DevExpress.ExpressApp.ReportsV2;
	using DevExpress.ExpressApp.ReportsV2.Services;
	using DevExpress.ExpressApp.Services.Security;
	using Microsoft.Extensions.Options;
	using SolutionName.Module.BusinessObjects;

	namespace SolutionName.Module {
		public class CustomReportsStorage : ReportStorageService {
			public CustomReportsStorage(ITypesInfo typesInfo, IServiceProvider serviceProvider, IObjectSpaceFactory objectSpaceFactory, IOptions<ReportOptions> options, IDataManipulationRight dataManipulationRight) : base(typesInfo, serviceProvider, objectSpaceFactory, options, dataManipulationRight) { }
			public override void CopyFrom(IReportDataV2 sourceReportData, IReportDataV2Writable targetReportData) {
				base.CopyFrom(sourceReportData, targetReportData);
				if (targetReportData is MyReportDataV2 customReportData) {
					customReportData.Category = "User Report";
				}
			}

		}
	}
	```
	***

4. Register `CustomReportsStorage` in your XAF application. The required steps differ depending on the target platform:

	* In an **XAF Blazor** application, add a line that registers your service in the `ConfigureServices` method after the `AddXaf` method call.
	* In an **XAF WinForms** application, add a line that registers your service in the `BuildApplication` method after the `WinApplication.CreateBuilder` method call.
	* In a **Web API** application, add a line that registers your service in the `ConfigureServices` method after the `AddXafWebApi` method call.

	# [MySolution.Blazor.Server\Startup.cs](#tab/tabid-blazor)

	```csharp{9}
	using DevExpress.ExpressApp.ReportsV2;
	//...
		public class Startup {
			// ...
			public void ConfigureServices(IServiceCollection services) {
				services.AddXaf(Configuration, builder => {
					//...
				});
				services.AddScoped<IReportStorage, CustomReportStorage>();
			}
			// ...
		}
	```

	# [MySolution.Win\Startup.cs](#tab/tabid-win)

	```csharp{6}
	using DevExpress.ExpressApp.ReportsV2;
	//...
	public class ApplicationBuilder : IDesignTimeApplicationFactory {
		public static WinApplication BuildApplication(string connectionString) {
			var builder = WinApplication.CreateBuilder();
			builder.Services.AddScoped<IReportStorage, CustomReportStorage>();
			//...
		}
		// ...
	}
	```

	# [MySolution.WebApi\Startup.cs](#tab/tabid-webAPI)

	```csharp{10}
	using DevExpress.ExpressApp.ReportsV2;
	//...
	namespace MySolution.WebApi {
		public class Startup {
			// ...
			public void ConfigureServices(IServiceCollection services) {
				services.AddXafWebApi(builder => {
					// ...
				}, Configuration);
				services.AddScoped<IReportStorage, CustomReportStorage>();
			}
			// ...
		}
	}
	```

	***