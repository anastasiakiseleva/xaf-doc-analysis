---
uid: DevExpress.ExpressApp.ReportsV2.IReportDataV2.DataType
name: DataType
type: Property
summary: Gets the type of persistent objects that are displayed within the report.
syntax:
  content: Type DataType { get; }
  parameters: []
  return:
    type: System.Type
    description: A **System.Type** value that specifies the type of persistent objects displayed within the report.
seealso: []
---
This property returns the data type that the [report data source](xref:113593) is bound to. The data type of predefined reports is specified via the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method. The data type of runtime reports is taken from the data source.