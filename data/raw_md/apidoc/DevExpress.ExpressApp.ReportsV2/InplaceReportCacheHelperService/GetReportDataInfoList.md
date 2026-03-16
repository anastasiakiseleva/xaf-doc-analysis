---
uid: DevExpress.ExpressApp.ReportsV2.InplaceReportCacheHelperService.GetReportDataInfoList(System.Type)
name: GetReportDataInfoList(Type)
type: Method
summary: Returns information on all report data objects that are stored in the application database, have the [IInplaceReportV2.IsInplaceReport](xref:DevExpress.ExpressApp.ReportsV2.IInplaceReportV2.IsInplaceReport) property set to **true** and the [IReportDataV2.DataType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.DataType) property set to the given type.
syntax:
  content: public virtual List<ReportDataInfo> GetReportDataInfoList(Type targetObjectType)
  parameters:
  - id: targetObjectType
    type: System.Type
    description: A **System.Type** object that specifies the [IReportDataV2.DataType](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2.DataType) of the required inplace reports.
  return:
    type: System.Collections.Generic.List{DevExpress.ExpressApp.ReportsV2.ReportDataInfo}
    description: A **List\<ReportDataInfo>** object that contains information on inplace report data objects that target the given type.
seealso: []
---
