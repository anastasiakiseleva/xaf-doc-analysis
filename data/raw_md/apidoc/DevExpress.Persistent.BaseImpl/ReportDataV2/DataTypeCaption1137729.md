---
uid: DevExpress.Persistent.BaseImpl.ReportDataV2.DataTypeCaption
name: DataTypeCaption
type: Property
summary: Gets the type caption of persistent objects that are displayed within the report.
syntax:
  content: public string DataTypeCaption { get; }
  parameters: []
  return:
    type: System.String
    description: A string that specifies the type caption of persistent objects that are displayed within the report.
seealso: []
---
This property returns the caption of the data type that the [report data source](xref:113593) is bound to. The data type of predefined reports is specified via the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method. The data type of runtime reports is taken from the data source.