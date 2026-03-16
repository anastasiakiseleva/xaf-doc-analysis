---
uid: DevExpress.ExpressApp.ReportsV2.IInplaceReportV2.DataTypeName
name: DataTypeName
type: Property
summary: Gets the name of the report's data type.
syntax:
  content: string DataTypeName { get; }
  parameters: []
  return:
    type: System.String
    description: A string which is the name of the report's data type.
seealso: []
---
This property returns the name of the data type that the [report data source](xref:113593) is bound to. The data type of predefined reports is specified via the [PredefinedReportsUpdater.AddPredefinedReport\<T>](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport*) method. The data type of runtime reports is taken from the data source (from the [DataSourceBase.ObjectTypeName](xref:DevExpress.Persistent.Base.ReportsV2.DataSourceBase.ObjectTypeName) property).