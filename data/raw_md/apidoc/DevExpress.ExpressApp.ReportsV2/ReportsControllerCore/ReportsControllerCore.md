---
uid: DevExpress.ExpressApp.ReportsV2.ReportsControllerCore
name: ReportsControllerCore
type: Class
summary: An [](xref:DevExpress.ExpressApp.ObjectViewController) that provides the [ReportsControllerCore.ExecuteReportAction](xref:DevExpress.ExpressApp.ReportsV2.ReportsControllerCore.ExecuteReportAction) used to execute reports.
syntax:
  content: 'public abstract class ReportsControllerCore : ReportDataViewController'
seealso:
- linkId: DevExpress.ExpressApp.ReportsV2.ReportsControllerCore._members
  altText: ReportsControllerCore Members
---
Activated in List Views that display [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) objects.

The [ReportsControllerCore.ExecuteReportAction](xref:DevExpress.ExpressApp.ReportsV2.ReportsControllerCore.ExecuteReportAction) introduced in this abstract Controller is initialized in the WinForms-specific descendant - [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportsController).

`ReportsControllerCore` modifies the default behavior of the [](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController). It handles the [ListViewProcessCurrentObjectController.CustomProcessSelectedItem](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomProcessSelectedItem) event in order to execute the current report when a report object is clicked in List View instead of opening the report data Detail View.

`ReportsControllerCore` contains the protected virtual `ShowReportPreview` method that displays the preview of the selected report. This method is called on executing the [ReportsControllerCore.ExecuteReportAction](xref:DevExpress.ExpressApp.ReportsV2.ReportsControllerCore.ExecuteReportAction). Internally, this method calls the [ReportServiceController.ShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview*) method of the [](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController) Controller.