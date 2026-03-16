---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport(DevExpress.XtraReports.UI.XtraReport)
name: SetupReport(XtraReport)
type: Method
summary: Initializes the specified report.
syntax:
  content: public void SetupReport(XtraReport report)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object.
seealso: []
---
Internally, this method invokes the following [](xref:DevExpress.ExpressApp.ReportsV2.ReportDataSourceHelper) methods, sequentially:

* [ReportDataSourceHelperBase.SetupReportDataSource](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReportDataSource(DevExpress.XtraReports.UI.XtraReport,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean,DevExpress.Xpo.SortProperty[],System.Boolean))
* [ReportDataSourceHelper.SetXafReportParametersObject](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetXafReportParametersObject(DevExpress.XtraReports.UI.XtraReport,DevExpress.ExpressApp.ReportsV2.ReportParametersObjectBase))
* [ReportDataSourceHelper.RegisterObjectSpaceProviderService](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.RegisterObjectSpaceProviderService(DevExpress.XtraReports.UI.XtraReport))
* [ReportDataSourceHelper.RegisterReportEnumLocalizer](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.RegisterReportEnumLocalizer(DevExpress.XtraReports.UI.XtraReport))
* [ReportDataSourceHelper.AttachCriteriaWithReportParametersManager](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.AttachCriteriaWithReportParametersManager(DevExpress.XtraReports.UI.XtraReport))

An example on how to use this method is available in the following topic: [](xref:113606).