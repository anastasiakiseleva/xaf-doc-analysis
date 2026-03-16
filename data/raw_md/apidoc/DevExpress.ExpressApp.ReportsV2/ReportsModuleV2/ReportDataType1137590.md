---
uid: DevExpress.ExpressApp.ReportsV2.ReportsModuleV2.ReportDataType
name: ReportDataType
type: Property
summary: Specifies the report data type used by the Reports V2 module.
syntax:
  content: public Type ReportDataType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) object specifying the report data type used by the Reports module.
seealso: []
---
Use this property to specify a custom report data type to be used by the Reports module. To implement a custom report data supported by the [](xref:DevExpress.ExpressApp.ReportsV2.ReportsModuleV2) module, implement the [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) interface.