---
uid: "117450"
seealso:
- linkId: "403400"
title: Create, View and Modify Dashboards in a WinForms Application
owner: Ekaterina Kiseleva
---
# Create, View and Modify Dashboards in a WinForms Application

This topic describes how to create and view a dashboard at runtime in a WinForms application when the [Dashboards Module](xref:117449) is added.

* In the [Navigation](xref:113198), open the Reports group, choose the **Dashboards** item and click **New**.
	
	![DashboardWinNew](~/images/dashboardwinnew125570.png)
	
	> [!NOTE]
	> If you cannot locate the **Reports** | **Dashboards** navigation item, ensure that the Dashboards Module is added in the Application Designer and the [DashboardsModule.GenerateNavigationItem](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.GenerateNavigationItem) property is set to **true**.
* In the invoked [Data Source Wizard](xref:115219), select **XAF Object Data Source** and click **Next**.
	
	![DashboardWinDataSource](~/images/dashboardwindatasource125572.png)
* Then, choose the [business object](xref:113664) type to be used as the dashboard data source and click **Finish**.
	
	![DashboardWinDataType](~/images/dashboardwindatatype125573.png)
	
	> [!TIP]
	> In the types list, you can see the types that have the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.VisibleInDashboardsAttribute) applied, or have the [IModelClassDashboardsVisibility.IsVisibleInDashboards](xref:DevExpress.ExpressApp.Model.IModelClassDashboardsVisibility.IsVisibleInDashboards) property set to **true**.
* In the invoked [Dashboard Designer](xref:116518), setup the dashboard according to the [Creating Dashboards in the WinForms Designer](xref:115954) guidelines.
	
	![DashboardWinDesigner](~/images/dashboardwindesigner125576.png)
	
	> [!IMPORTANT]
	> [!include[DashboardLocalizedEnumsNote](~/templates/dashboardlocalizedenumsnote111834.md)]
* After a dashboard is saved in the designer, it is added to the **Dashboards** List View. You can double-click a dashboard to view it.
	
	![DashboardWinListView](~/images/dashboardwinlistview125578.png)
	
* To modify an existing dashboard, select it and click the **ShowDashboardDesigner** [Action](xref:112622) in the toolbar or ribbon bar.
	
	![DashboardShowDesignerWin](~/images/dashboardshowdesignerwin125632.png)
	
	This Action is also available in the context menu.
	
	![DashboardShowDesignerContextWin](~/images/dashboardshowdesignercontextwin125633.png)
