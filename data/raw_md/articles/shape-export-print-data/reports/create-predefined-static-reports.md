---
uid: "113645"
seealso: []
title: Create Predefined Static Reports
---
# Create Predefined Static Reports

This topic describes how to [create an XtraReport at Design Time](xref:2587) and then register it. An XAF application displays registered reports in the **Reports** List View. These predefined reports _cannot be modified by a user_. However, a _user can copy a predefined report_ with the help of the **Copy Predefined Report** Action and then modify the copy.

Follow the steps below to create an **XtraReport** and register it for use with the **Reports V2** module.

1. Use the **DevExpress v.<:xx.x:> Report** project item template (see [Report Wizard](xref:4254)) to add an empty [](xref:DevExpress.XtraReports.UI.XtraReport) to your project. Select the **Blank** report type and click the **Finish** button.
	
	![Report Wizard, DevExpress](~/images/xtrareport_wizard117445.png)

	The _XtraReport1.cs_ item appears in the module project of your application.

    ![|XtraReport1 Item in the Solution Explorer, DevExpress|](~/images/xtrareport1-item-in-solutionp-wizard-devexpress.png)

2. The **Reports V2** module supports the following [Data Source](xref:113593) components to use in XAF-compatible XtraReport classes: [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) and [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource). Drag the **CollectionDataSource** item from the **Toolbox** to the created report.
	
	![|Report Data Sources in Toolbox, DevExpress|](~/images/collectiondatasource-item-in-toolbox-devexpress.png)
	
	> [!NOTE]
	> You can use the `ViewDataSource` component instead of the `CollectionDataSource`. For more information about the difference between these components refer to the following topic: [Data Sources for Reports V2](xref:113593).

3. Invoke the **Properties** window for the **collectionDataSource1** item and set value of the **ObjectTypeName** property to the name of the business class you want to use for your report.
	
	![|CollectionDataSource Properties, DevExpress|](~/images/datasource_populate117437.png)

    The business class properties should appear in the **Field List** window.

    ![|Field List Populated with Data Source Items, DevExpress|](~/images/report-designer-field-list-devexpress.png)


4. Drag the required fields to the report or run the **Report Wizard** to generate the required layout automatically.
	
	![Report_Designer-Smart_Tag](~/images/report_designer-smart_tag117446.png)
	
	To learn more about report design, refer to the following topics of the Reporting documentation: [Report Designer](xref:4256) and [Report Wizard](xref:4254). Note that the `CollectionDataSource` and `ViewDataSource` components only provide a list of fields to the designer and you cannot preview the report at design time.
	
	> [!NOTE]
	> * At design time, the Preview tab of the Report Designer is empty. The [](xref:DevExpress.Persistent.Base.ReportsV2.CollectionDataSource) and [](xref:DevExpress.Persistent.Base.ReportsV2.ViewDataSource) components do not connect to a database directly and require an [](xref:DevExpress.ExpressApp.IObjectSpace) instance to load data. XAF creates the instance at runtime only, therefore it cannot load data at design time.
	> * Currently, [Custom Fields](xref:113583) are not available in the Reports Designer at design time.

5. After you save the report, register it in your XAF application. Navigate to the [ModuleBase.GetModuleUpdaters](xref:DevExpress.ExpressApp.ModuleBase.GetModuleUpdaters(DevExpress.ExpressApp.IObjectSpace,System.Version)) method in the _Module.cs_ file. Instantiate the [](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater) class and use the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method to add a report. Add the updater object to the method's return value.
	
	**File:** _MySolution.Module\Module.cs_

	# [C#](#tab/tabid-csharp)

	```csharp{14-18}
	// ...
	using DevExpress.ExpressApp.ReportsV2;
	using MySolution.Module.BusinessObjects;

	namespace MySolution.Module;

	public sealed class MySolutionModule : ModuleBase {
		public MySolutionModule() {
			// ...
		}

		public override IEnumerable<ModuleUpdater> GetModuleUpdaters(
			IObjectSpace objectSpace, Version versionFromDB) {
			ModuleUpdater updater = new DatabaseUpdate.Updater(objectSpace, versionFromDB);
			PredefinedReportsUpdater predefinedReportsUpdater =
				new PredefinedReportsUpdater(Application, objectSpace, versionFromDB);
			predefinedReportsUpdater.AddPredefinedReport<XtraReport1>("Employee DOB Information", typeof(Employee));
			return new ModuleUpdater[] { updater, predefinedReportsUpdater };
		}
		// ...
	}
	```

	***
	
	> [!NOTE]
	> * [!include[PredefinedReportsUpdater_MultipleInstancesNote](~/templates/predefinedreportsupdater_multipleinstancesnote111179.md)]
	> * [Multi-tenant applications](xref:404436) have specific implementation features. Refer to the following help topic for more information: [Register Predefined Reports in a Multi-Tenant Application](xref:113239#register-predefined-reports-in-a-multi-tenant-application).

6. Run the application. Note that the designed **XtraReport** is available in the **Reports** List View. A user can double-click a report to preview it in a [Print Preview Form](xref:5184).

   ASP.NET Core Blazor
   :   ![|XAF ASP.NET Core Blazor Report List View, DevExpress|](~/images/static-report-listview-blazor-devexpress.png)  
       ![|XAF ASP.NET Core Blazor Report Preview, DevExpress|](~/images/static-report-preview-blazor-devexpress.png)
   Windows Forms
   :   ![XAF Windows Forms Report List View, DevExpress](~/images/static-report-listview-winforms-devexpress.png)  
       ![XAF Windows Forms Report Preview, DevExpress](~/images/static-report-preview-winforms-devexpress.png)

If you want to skip the preview dialog, refer to the [How to: Print a Report Without Displaying a Preview](xref:113601) example.

> [!IMPORTANT]
> When you create a predefined report with scripts that end users can possibly [modify](xref:113647), do not use [](xref:DevExpress.XtraReports.UI.XtraReport) events directly. Instead, use the [XtraReport.Scripts](xref:DevExpress.XtraReports.UI.XtraReport.Scripts) and/or [XRControl.Scripts](xref:DevExpress.XtraReports.UI.XRControl.Scripts) properties in the [Report Designer](xref:4256), as demonstrated in the following topic: [Scripting Overview](xref:2615). Otherwise, when you use the **Copy Predefined Report** Action, XAF does not copy your code to user scripts.
>
> This technique requires that you add references to assemblies used in scripts to the [XtraReport.ScriptReferences](xref:DevExpress.XtraReports.UI.XtraReport.ScriptReferences) property. Assemblies used in your application are attached to scripts automatically. If classes from such assemblies cause errors during script evaluation, either use fully qualified names or add the _using_ directive at the beginning of the script.
