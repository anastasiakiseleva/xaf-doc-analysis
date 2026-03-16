---
uid: DevExpress.ExpressApp.ReportsV2.ReportsControllerCore.ExecuteReportAction
name: ExecuteReportAction
type: Property
summary: An [Action](xref:112622) that executes the selected report.
syntax:
  content: public SimpleAction ExecuteReportAction { get; protected set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SimpleAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SimpleAction) that executes the selected report.
seealso: []
---
Internally, this Action calls the [ReportServiceController.ShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview*) method of the [](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController) Controller. You can override the protected **ShowPeportPreview** method to change the Action behavior.