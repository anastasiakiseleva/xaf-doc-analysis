---
uid: DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.ShowDesigner(DevExpress.ExpressApp.IObjectSpace,System.Type)
name: ShowDesigner(IObjectSpace, Type)
type: Method
summary: Shows an empty [](xref:DevExpress.DashboardWin.DashboardDesigner).
syntax:
  content: public void ShowDesigner(IObjectSpace objectSpace, Type dashboardDataType)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the current View's [Object Space](xref:113707).
  - id: dashboardDataType
    type: System.Type
    description: A type implementing the [](xref:DevExpress.Persistent.Base.IDashboardData) interface. An implementation used by the Dashboards Module is specified in the [DashboardsModule.DashboardDataType](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.DashboardDataType) property.
seealso: []
---
Use the **ShowDesigner** method to show an empty [](xref:DevExpress.DashboardWin.DashboardDesigner) that allows end-users to create a new [](xref:DevExpress.DashboardCommon.Dashboard). The newly created **Dashboard** will be stored in the [IDashboardData.Content](xref:DevExpress.Persistent.Base.IDashboardData.Content) property of the **dashboardDataType** object.

Use the [DashboardDesignerManager.GetDashboardData](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.GetDashboardData) method to get the [](xref:DevExpress.Persistent.Base.IDashboardData) after the Dashboard Designer is closed.

If the [DashboardDesignerManager.SkipDataSourceWizard](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.SkipDataSourceWizard) property is set to **false**, the [Data Source Wizard](xref:17652) is displayed together with the Dashboard Designer.