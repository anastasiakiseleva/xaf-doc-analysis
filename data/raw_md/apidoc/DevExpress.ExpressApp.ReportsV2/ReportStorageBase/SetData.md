---
uid: DevExpress.ExpressApp.ReportsV2.ReportStorageBase.SetData(DevExpress.XtraReports.UI.XtraReport,System.String)
name: SetData(XtraReport, String)
type: Method
summary: Stores the specified report to a Report Storage using the specified handle.
syntax:
  content: public virtual void SetData(XtraReport report, string url)
  parameters:
  - id: report
    type: DevExpress.XtraReports.UI.XtraReport
    description: An [](xref:DevExpress.XtraReports.UI.XtraReport) object to be saved.
  - id: url
    type: System.String
    description: A [](xref:System.String) specifying the handle which should be used to save a report.
seealso: []
---
Call the [ReportsStorage.CanSetData](xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.CanSetData(System.String)) method before using **SetData** to determine whether or not it is allowed to use the specified handle to store a report.