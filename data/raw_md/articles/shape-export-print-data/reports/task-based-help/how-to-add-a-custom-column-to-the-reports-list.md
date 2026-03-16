---
uid: "113672"
seealso: []
title: 'How to: Add a Custom Column to the Reports List'
owner: Ekaterina Kiseleva
---
# How to: Add a Custom Column to the Reports List

This topic describes how to customize the persistent class used to store [reports](xref:113591) to associate additional information with report objects. For instance, if you add the `Category` property, an additional column will be added to the `Reports` List View, and end users will be able to group, sort, or filter by categories.

**WinForms**  
![ReportsV2_WizParamsRuntime](~/images/reportsv2_wizparamsruntime117543.png)

**Blazor**  
![ReportsV2_WizParamsRuntime_Blazor](~/images/ReportsV2_WizParamsRuntime_Blazor.png)

[!include[ReportsV2ExampleNote](~/templates/reportsv2examplenote111131.md)]

## Inherit ReportDataV2
### Entity Framework Core

If you use Entity Framework Core, create the `MyReportDataV2` entity derived from [](xref:DevExpress.Persistent.BaseImpl.EF).[](xref:DevExpress.Persistent.BaseImpl.EF.ReportDataV2). Then, add your custom entity to the `DbContext`.

**File:** _MySolution.Module\BusinessObjects\MyReportDataV2.cs_

# [C#](#tab/tabid-csharp1)

```csharp
public class MyReportDataV2 : DevExpress.Persistent.BaseImpl.EF.ReportDataV2 {
    public virtual string Category { get;set; }
}

public class MySolutionDbContext : DbContext {
    // ...
    public DbSet<ReportDataV2> ReportDataV2 { get; set; }
    public DbSet<MyReportDataV2> MyReportDataV2 { get; set; }
}
```

***

### XPO

If you use XPO, create the `MyReportDataV2` persistent class derived from [](xref:DevExpress.Persistent.BaseImpl).[](xref:DevExpress.Persistent.BaseImpl.ReportDataV2).

**File:** _MySolution.Module\BusinessObjects\MyReportDataV2.cs_

# [C#](#tab/tabid-csharp)

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

## Specify ReportsModuleV2.ReportDataType

### With Application Builder

In applications that use the Application Builder, assign the type of your custom report data class to the `ReportsOptions.ReportDataType` property as shown below:

**File:** _MySolution.Blazor.Server\Startup.cs_

# [C#](#tab/tabid-csharp1)

```csharp
builder.Modules
    .AddReports(options => {
        options.ReportDataType = typeof(MyReportDataV2);
    })
```
***

### Without Application Builder

In applications that do not use the Application Builder, you can specify the [ReportDataType](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType) setting as follows.

**File:** _WinApplication.Designer.cs_

# [C#](#tab/tabid-csharp)

```csharp
partial class MainDemoWinApplication {
	// ...
	private void InitializeComponent() {
		// ...
        // reportsModuleV21
		// 
		this.reportsModuleV21.ReportDataType = typeof(MyReportDataV2);
		// ...
	}
}
```
***

## Add the New Property to the Report Wizard
> [!NOTE]
> This feature is not supported in **ASP.NET Core Blazor**. See the [Limitations](#limitations) section for more information.
>
> You can also omit this section if you do not want the additional property to be initialized by a user. Instead, you can [customize the ReportsStorage class](xref:113674) to update the property value in code.

To make the newly introduced property visible in the Report Wizard, do the following.

* In the platform-agnostic module project, inherit from the `NewXafReportWizardParameters` class and declare the `Category` string property.
	
	**File:** _MySolution.Module\CustomReportWizardParameters.cs_

	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.DC;
	using DevExpress.ExpressApp.ReportsV2;
	using DevExpress.ExpressApp.ReportsV2.Win;
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
* In the [WinForms application project](xref:118045), implement a [View Controller](xref:112621). Override the `OnActivated` method, access the standard [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController) and subscribe to its [WinReportServiceController.NewXafReportWizardShowing](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.NewXafReportWizardShowing) event. In the event handler, pass an instance of the `CustomReportWizardParameters` class to the Report Wizard.
	
	**File:** _MySolution.Win\Controllers.ReportWizardModifyController.cs_

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

* In the ASP.NET Core Blazor [application project](xref:118045), implement one more [View Controller](xref:112621). Similarly, override the `OnActivated` method, access the standard `DevExpress.ExpressApp.ReportsV2.Blazor.BlazorReportServiceController`, and subscribe to its `BlazorReportServiceController.NewReportWizardShowing` event. In the event handler, pass an instance of the `CustomReportWizardParameters` class to the Report Wizard.

	**File:** _MySolution.Blazor.Server\Controllers.ReportWizardModifyController.cs_

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

After you complete these steps, the following [Detail Views](xref:112611) are added to the Application Model:

* **MyReportData_DetailView**
* **CustomReportWizardParameters_DetailView**

To place the new **Category** item at the desired position, start the [Model Editor](xref:112582) and adjust these Detail View layouts.

![ReportsV2_WizParams](~/images/reportsv2_wizparams117542.png)

For a detailed explanation of how to customize a Detail View's layout, refer to the [View Items Layout Customization](xref:112817) help topic.

## Limitations

XAF does not support the capability to display and edit custom report properties in the New Report Wizard under the ASP.NET Core Blazor platform. An end user can use the Report ListView's _Edit_ action to specify a custom property value:

![Edit Custom Report Properties](~/images/reports-edit-custom-property.png)
