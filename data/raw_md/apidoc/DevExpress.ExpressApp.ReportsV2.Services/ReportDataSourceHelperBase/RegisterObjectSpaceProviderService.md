---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.RegisterObjectSpaceProviderService(DevExpress.XtraReports.UI.XtraReport)
name: RegisterObjectSpaceProviderService(XtraReport)
type: Method
summary: Registers a service that supplies an [](xref:DevExpress.ExpressApp.IObjectSpace) when it is required by the report data source.
syntax:
  content: public void RegisterObjectSpaceProviderService(XtraReport report)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
seealso: []
---
The [Data Sources for Reports V2](xref:113593) require the [](xref:DevExpress.ExpressApp.IObjectSpace) to dynamically bind data. The **RegisterObjectSpaceProviderService** method is called by the [ReportDataSourceHelperBase.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport*) method.  You can override the virtual **CreateReportObjectSpaceProvider** method to customize the **RegisterObjectSpaceProviderService** method behavior. To use your own implementation of the [](xref:DevExpress.ExpressApp.ReportsV2.ReportDataSourceHelper) class, assign its instance to the [ReportsModuleV2.ReportsDataSourceHelper](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportsDataSourceHelper) property.