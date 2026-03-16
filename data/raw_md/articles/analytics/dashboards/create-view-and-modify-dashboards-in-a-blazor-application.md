---
uid: "403400"
title: Create, View, and Modify Dashboards in an ASP.NET Core Blazor Application
owner: Yekaterina Kiseleva
seealso:
  - linkId: "117450"
---
# Create, View, and Modify Dashboards in an ASP.NET Core Blazor Application

This topic describes how end users can create and view a dashboard at runtime in an ASP.NET Core Blazor application with the [Dashboards Module](xref:117449).

1. In the [Navigation](xref:113198) menu, expand the **Reports** group, choose the **Dashboards** item, and click **New**.
	
	![Create a new dashboard](~/images/BlazorDashboard_New.png)
	
	If the Navigation control does not display the **Reports** | **Dashboards** item, ensure the following:
	* The Dashboards Module is added and configured correctly as described in the following help topic: [Add the Dashboards Module to Your Application](xref:117449#add-the-dashboards-module-to-your-application). 
	* The [DashboardsModule.GenerateNavigationItem](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.GenerateNavigationItem) property is set to **true**.

2. In the displayed [](xref:DevExpress.DashboardBlazor.DxDashboard) control, open the dashboard menu, specify the dashboard name in the **Title** menu item, and choose a [business object](xref:113664) type to be used as a data source:
	
	![The dashboard menu button](~/images/BlazorDashboard_MenuButton.png)

	![The dashboard menu](~/images/BlazorDashboard_Menu.png)
	
	> [!TIP]
	> The **Data Sources** list contains the types decorated with the [DefaultClassOptions](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [VisibleInDashboards](xref:DevExpress.Persistent.Base.VisibleInDashboardsAttribute) attribute.

3. Configure the newly created dashboard as described in the following help topic: [Creating Dashboards on the Web](xref:116994).
	
	![Configure a new dashboard](~/images/BlazorDashboard_Designer.png)
	
	> [!IMPORTANT]
	> [!include[DashboardLocalizedEnumsNote](~/templates/dashboardlocalizedenumsnote111834.md)]

4. Save the dashboard. You can find it in the **Dashboards** List View. Click your dashboard to view it.

	Note that in an ASP.NET Core Blazor application, you can access dashboards added in a WinForms application, and visa versa.

5. To modify an existing dashboard, open it and click the **Working Mode** [Action](xref:112622):
	
	![Switch between viewer and designer modes](~/images/BlazorDashboard_WorkingMode.png)

> [!Note]
> In ASP.NET Core Blazor applications, you can edit dashboards in desktop browsers only.
