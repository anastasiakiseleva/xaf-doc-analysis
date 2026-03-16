---
uid: DevExpress.Persistent.BaseImpl.EF.ReportDataV2
name: ReportDataV2
type: Class
summary: The entity class used to store reports in the [Reports V2 Module](xref:113591).
syntax:
  content: 'public class ReportDataV2 : BaseObject, IReportDataV2Writable, IReportDataV2, IInplaceReportV2'
seealso:
- linkId: DevExpress.Persistent.BaseImpl.EF.ReportDataV2._members
  altText: ReportDataV2 Members
---
To create a custom persistent container for reports, inherit this class or implement the [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) interface from scratch. Then, pass the implemented type to the [ReportsModuleV2.ReportDataType](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType) property. The example is provided in the [How to: Add a Custom Column to the Reports List](xref:113672) topic.