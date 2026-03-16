---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.RegisterReportEnumLocalizer(DevExpress.XtraReports.UI.XtraReport)
name: RegisterReportEnumLocalizer(XtraReport)
type: Method
summary: Registers a localizer for enumeration types used in a report.
syntax:
  content: public void RegisterReportEnumLocalizer(XtraReport report)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
seealso: []
---
The **RegisterReportEnumLocalizer** method is called by the [ReportDataSourceHelperBase.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport*) method.  You can override the virtual **CreateReportEnumLocalizer** method to customize the **RegisterReportEnumLocalizer** method behavior. To use your own implementation of the [](xref:DevExpress.ExpressApp.ReportsV2.ReportDataSourceHelper) class, assign its instance to the [ReportsModuleV2.ReportsDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportsDataSourceHelper) property.