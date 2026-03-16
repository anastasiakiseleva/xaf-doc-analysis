---
uid: DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.ShowDesigner(DevExpress.ExpressApp.IObjectSpace,System.Type,DevExpress.Persistent.Base.IDashboardData)
name: ShowDesigner(IObjectSpace, Type, IDashboardData)
type: Method
summary: Shows a [](xref:DevExpress.DashboardWin.DashboardDesigner) with the provided [](xref:DevExpress.DashboardCommon.Dashboard).
syntax:
  content: public void ShowDesigner(IObjectSpace objectSpace, Type dashboardDataType, IDashboardData dashboardData)
  parameters:
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object specifying the current View's [Object Space](xref:113707).
  - id: dashboardDataType
    type: System.Type
    description: A type implementing the [](xref:DevExpress.Persistent.Base.IDashboardData) interface. An implementation used by the Dashboards Module is specified in the [DashboardsModule.DashboardDataType](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule.DashboardDataType) property.
  - id: dashboardData
    type: DevExpress.Persistent.Base.IDashboardData
    description: An [](xref:DevExpress.Persistent.Base.IDashboardData) object. The [IDashboardData.Content](xref:DevExpress.Persistent.Base.IDashboardData.Content) property should contain the current [](xref:DevExpress.DashboardCommon.Dashboard).
seealso: []
---
Use the **ShowDesigner** method to show the [](xref:DevExpress.DashboardWin.DashboardDesigner) that allows end-users to edit a [](xref:DevExpress.DashboardCommon.Dashboard).

Use the [DashboardDesignerManager.GetDashboardData](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.GetDashboardData) method to get the [](xref:DevExpress.Persistent.Base.IDashboardData) after the Dashboard Designer is closed.