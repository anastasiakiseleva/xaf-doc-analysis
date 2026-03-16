---
uid: DevExpress.ExpressApp.ReportsV2.ReportOptions.ReportDataType
name: ReportDataType
type: Property
summary: Specifies the type of the report data objects used to persist reports.
syntax:
  content: public Type ReportDataType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: The [](xref:System.Type) of the report data objects used to persist reports.
seealso: []
---
The following example demonstrates how to specify this property: 

[!include[<options.ReportDataType = typeof(DevExpress.Persistent.BaseImpl.ReportDataV2);>](~/templates/AddReports_Blazor_example.md)]