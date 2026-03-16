---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataV2
name: IReportDataV2
type: Interface
summary: Implemented by persistent classes used to store reports used by the [Reports V2 Module](xref:113591).
syntax:
  content: public interface IReportDataV2
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.IReportDataV2._members
  altText: IReportDataV2 Members
---
Built-in implementation of this interface used by default in XPO applications is the [](xref:DevExpress.Persistent.BaseImpl.ReportDataV2) class. In Entity Framework applications, the [](xref:DevExpress.Persistent.BaseImpl.EF.ReportDataV2) entity can be used. To create a custom persistent container for reports, implement the **IReportDataV2** interface, and pass the implemented type to the [ReportsModuleV2.ReportDataType](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType) property.