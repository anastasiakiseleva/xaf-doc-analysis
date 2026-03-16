---
uid: DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview(System.String)
name: ShowPreview(String)
type: Method
summary: Displays the Preview Report window.
syntax:
  content: public void ShowPreview(string reportContainerHandle)
  parameters:
  - id: reportContainerHandle
    type: System.String
    description: Gets the handle of the [](xref:DevExpress.ExpressApp.ReportsV2.ReportContainer) object.
seealso: []
---
An example of using this method is provided in the [Invoke the Report Preview from Code](xref:113703) topic.

The **ShowPreview** method throws an **InvalidCastException** if you use a custom data source that does not support the [](xref:DevExpress.Persistent.Base.ReportsV2.ISupportSorting) interface. In this instance, use the [ReportDataSourceHelper.CustomSetSorting](xref:DevExpress.ExpressApp.ReportsV2.Services.ReportDataSourceHelperBase.CustomSetSorting) event to specify sorting.