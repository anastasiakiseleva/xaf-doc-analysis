---
uid: DevExpress.ExpressApp.ReportsV2.IInplaceReportV2
name: IInplaceReportV2
type: Interface
summary: Implemented by persistent classes used to store reports that can be used as inplace repors.
syntax:
  content: public interface IInplaceReportV2
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.IInplaceReportV2._members
  altText: IInplaceReportV2 Members
---
Inplace reports can be executed for a selected set of business objects using the [PrintSelectionBaseController.ShowInReportAction](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportAction) Action.

To create a custom persistent container for inplace reports, implement **IInplaceReportV2** and [](xref:DevExpress.ExpressApp.ReportsV2.IInplaceReportV2) interfaces, and pass the implemented type to the [ReportsModuleV2.ReportDataType](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType) property.xref:DevExpress.ExpressApp.Rep