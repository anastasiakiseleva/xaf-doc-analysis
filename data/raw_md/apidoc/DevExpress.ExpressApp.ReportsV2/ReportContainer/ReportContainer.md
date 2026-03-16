---
uid: DevExpress.ExpressApp.ReportsV2.ReportContainer
name: ReportContainer
type: Class
summary: An object that specifies the report markup ([](xref:DevExpress.XtraReports.UI.XtraReport) object), the associated parameters object type and the report's display name.
syntax:
  content: 'public class ReportContainer : IReportContainer'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.ReportContainer._members
  altText: ReportContainer Members
---
To get an [](xref:DevExpress.ExpressApp.ReportsV2.ReportContainer) instance by is handle, use the [ReportsStorage.GetReportContainerByHandle](xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.GetReportContainerByHandle*) method.

To create a custom Report Container, implement the **ReportContainer** interface, handle the [ReportsStorage.CreateCustomReportContainer](xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.CreateCustomReportContainer) event and pass an instance of your custom Report Container to the [CreateCustomReportContainerEventArgs.ReportContainer](xref:DevExpress.ExpressApp.ReportsV2.CreateCustomReportContainerEventArgs.ReportContainer) parameter.
