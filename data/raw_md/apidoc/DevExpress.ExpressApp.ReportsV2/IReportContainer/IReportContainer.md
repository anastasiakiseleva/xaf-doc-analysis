---
uid: DevExpress.ExpressApp.ReportsV2.IReportContainer
name: IReportContainer
type: Interface
summary: Implemented by Report Containers.
syntax:
  content: public interface IReportContainer
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.IReportContainer._members
  altText: IReportContainer Members
---
Report Container is an object that specifies the report markup ([](xref:DevExpress.XtraReports.UI.XtraReport) object), the associated parameters object type and the report's display name.

The default implementation of this interface used by the [Reports V2 Module](xref:113591) is [](xref:DevExpress.ExpressApp.ReportsV2.ReportContainer).

To create a custom Report Container, implement the `IReportContainer` interface, handle the `DevExpress.ExpressApp.ReportsV2.ReportStorageBase.CreateCustomReportContainer` event and pass an instance of your custom Report Container to the [CreateCustomReportContainerEventArgs.ReportContainer](xref:DevExpress.ExpressApp.ReportsV2.CreateCustomReportContainerEventArgs.ReportContainer) parameter.

To get an [](xref:DevExpress.ExpressApp.ReportsV2.IReportContainer) instance by is handle, use the [ReportsStorage.GetReportContainerByHandle](xref:DevExpress.ExpressApp.ReportsV2.ReportStorageBase.GetReportContainerByHandle*) method.
