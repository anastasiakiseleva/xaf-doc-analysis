---
uid: DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupBeforePrint(DevExpress.XtraReports.UI.XtraReport)
name: SetupBeforePrint(XtraReport)
type: Method
summary: Prepares the report for further printing.
syntax:
  content: public void SetupBeforePrint(XtraReport report)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object that specifies the report.
seealso: []
---
If you want to print a report in code, you should use the **SetupBeforePrint** method that executes the [ReportDataSourceHelperBase.SetupReport](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.SetupReport*) method and triggers the [ReportDataSourceHelper.BeforeShowPreview](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.BeforeShowPreview) event.

An example of using the **SetupBeforePrint** method is provided in the [How to: Print a Report Without Displaying a Preview](xref:113601) topic.