---
uid: DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater.AddPredefinedReport``1(System.String,System.Type)
name: AddPredefinedReport<T>(String, Type)
type: Method
summary: Adds the specified predefined report to the [](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater) instance.
syntax:
  content: |-
    public void AddPredefinedReport<T>(string displayName, Type dataType)
        where T : XtraReport
  parameters:
  - id: displayName
    type: System.String
    description: A string which is the report's display name.
  - id: dataType
    type: System.Type
    description: A type of the business object used by the report's data source.
  typeParameters:
  - id: T
    description: ''
seealso: []
---
The **AddPredefinedReport\<T>** method's generic parameter specifies the report type (the type of an [](xref:DevExpress.XtraReports.UI.XtraReport) descendant specifying the predefined report layout). An example of using this method is available in the [](xref:DevExpress.ExpressApp.ReportsV2.PredefinedReportsUpdater) topic.