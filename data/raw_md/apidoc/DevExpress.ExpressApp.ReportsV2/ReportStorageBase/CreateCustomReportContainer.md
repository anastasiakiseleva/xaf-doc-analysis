---
uid: DevExpress.ExpressApp.ReportsV2.ReportStorageBase.CreateCustomReportContainer
name: CreateCustomReportContainer
type: Event
summary: Occurs when the [](xref:DevExpress.ExpressApp.ReportsV2.IReportContainer) object is created.
syntax:
  content: |-
    [Browsable(false)]
    public event EventHandler<CreateCustomReportContainerEventArgs> CreateCustomReportContainer
seealso: []
---
Report Container is an object that specifies the report markup ([](xref:DevExpress.XtraReports.UI.XtraReport) object), the associated parameter object type and the report's display name.

Handle the **CreateCustomReportContainer** event to create a custom Report Container using the [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) object passed via the [CreateCustomReportContainerEventArgs.ReportData](xref:DevExpress.ExpressApp.ReportsV2.CreateCustomReportContainerEventArgs.ReportData) parameter.

