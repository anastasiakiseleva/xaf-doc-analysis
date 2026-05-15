---
uid: DevExpress.ExpressApp.ReportsV2.Blazor.BlazorReportServiceController.NewReportWizardShowing
name: NewReportWizardShowing
type: Event
summary: Occurs before the XAF displays the [Report Wizard](xref:4254).
syntax:
  content: public event EventHandler<BlazorNewReportWizardShowingEventArgs> NewReportWizardShowing
seealso: []
---
When you call the @DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowWizard(System.Type) method, the `NewReportWizardShowing` event fires. Handle this event to run custom logic before the **Report Wizard** is displayed, or instead of displaying it. Set the handler’s`Handled` parameter to suppress the default **Report Wizard**.

Refer to the following help topic for an example: [How to: Add a Custom Column to the Reports List](xref:113672).