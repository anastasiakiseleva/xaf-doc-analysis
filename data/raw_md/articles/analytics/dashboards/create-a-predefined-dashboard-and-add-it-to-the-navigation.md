---
uid: "117453"
seealso: []
title: Create a Predefined Dashboard and Add it to the Navigation
owner: Ekaterina Kiseleva
---
# Create a Predefined Dashboard and Add it to the Navigation

This topic describes how to provide a predefined dashboard that is available to users immediately after application deployment.

* Create a dashboard at runtime. You can review the following topics to learn how to do it.
	
	* [Create, View and Modify Dashboards in a WinForms Application](xref:117450)
	* [Create, View and Modify Dashboards in an ASP.NET Core Blazor Application](xref:403400)
* Save the dashboard to an XML file.
	
	* In a WinForms application, you can use the **Save As** button in the [Dashboard Designer](xref:116518).
		
		![DashboardSaveAsWin](~/images/dashboardsaveaswin125655.png)
	* In an ASP.NET Core Blazor application, you can click the **Export To XML** action when _viewing_ the dashboard.
		
		![The Export To XML Action](~/images/Dashboard_ExportToXML_Blazor.png)
* Add the created XML file to the [module project](xref:118045) as a [resource file](https://learn.microsoft.com/en-us/visualstudio/ide/managing-application-resources-dotnet).
	
	![DashboardResource](~/images/dashboardresource125665.png)
* Open the [!include[File_Updater](~/templates/file_updater111114.md)] file and add the following code to the [ModuleUpdater.UpdateDatabaseAfterUpdateSchema](xref:DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema) method.
	
	# [C#](#tab/tabid-csharp)
	
	```csharp
	using DevExpress.ExpressApp.Dashboards;
	using MySolution.Module.Properties;
	// ...
	public override void UpdateDatabaseAfterUpdateSchema() {
	    base.UpdateDatabaseAfterUpdateSchema();
	    DashboardsModule.AddDashboardData<DashboardData>(
	        ObjectSpace, "My Dashboard", Resources.MyDashboard1);
	    // ...
	    ObjectSpace.CommitChanges();
	}
	```
	***

	Note that [multi-tenant applications](xref:404436) have specific implementation features. Refer to the following help topic for more information: [Register Predefined Dashboards in a Multi-Tenant Application](xref:113239#register-predefined-dashboards-in-a-multi-tenant-application).

* Run the [Model Editor](xref:112582). To add the dashboard to a certain [navigation group](xref:113198), right-click its _Items_ child node, and choose **Add…** | **DashboardNavigationItem**.
	
	![DashboardNavigationItem](~/images/dashboardnavigationitem125662.png)
* Focus the created node and set the [IModelDashboardNavigationItem.DashboardTitle](xref:DevExpress.ExpressApp.Dashboards.IModelDashboardNavigationItem.DashboardTitle) property to the title of the required dashboard.
	
	![DashboardTitle](~/images/dashboardtitle125663.png)
	
	> [!IMPORTANT]
	> As the dashboard is identified by its title, do not change the title after the navigation item is added.
* Run the application to ensure that the dashboard is added to the navigation.
	
	![DashboardNavigationWin](~/images/dashboardnavigationwin125666.png)

> [!TIP]
> If you are going to use predefined dashboards only, you can remove the Dashboards List View from the navigation. Set the [DashboardsModule.GenerateNavigationItem](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.GenerateNavigationItem) property to **false** for this purpose.
