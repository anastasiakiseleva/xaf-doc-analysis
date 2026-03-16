---
uid: DevExpress.ExpressApp.Dashboards.DashboardsModule.DashboardDataType
name: DashboardDataType
type: Property
summary: Specifies the dashboard data type used by the Dashboards Module.
syntax:
  content: public Type DashboardDataType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) object specifying the report data type used by the Dashboards Module.
seealso: []
---
Use this property to specify a custom dashboard data type to be used by the Dashboards Module. To implement a custom dashboard data type supported by the [](xref:DevExpress.ExpressApp.Dashboards.DashboardsModule) module, implement the [](xref:DevExpress.Persistent.Base.IDashboardData) interface.