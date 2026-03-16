---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupBeforePrint(DevExpress.XtraReports.UI.XtraReport)
name: SetupBeforePrint(XtraReport)
type: Method
summary: Prepares the report for further printing.
syntax:
  content: void SetupBeforePrint(XtraReport report)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
seealso: []
---

If you want to print a report in code, you should use the `SetupBeforePrint` method that executes the [IReportDataSourceHelper.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.SetupReport*) method and triggers the [IReportDataSourceHelper.BeforeShowPreview](xref:DevExpress.ExpressApp.ReportsV2.IReportDataSourceHelper.BeforeShowPreview) event.

An example on how to use the `SetupBeforePrint` method is available in the [How to: Print a Report Without Displaying a Preview](xref:113601) topic.
