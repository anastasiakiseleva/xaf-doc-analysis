---
uid: DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController.NewXafReportWizardShowing
name: NewXafReportWizardShowing
type: Event
summary: Occurs before invoking the [Report Wizard](xref:4254).
syntax:
  content: public event EventHandler<NewXafReportWizardShowingEventArgs> NewXafReportWizardShowing
seealso: []
---
The **NewXafReportWizardShowing** event is raised as the result of invoking the  [ReportServiceController.ShowWizard](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowWizard(System.Type)) method. Handle this event to implement custom logic to be executed before or instead of invoking the **Report Wizard**. Set the handler's **Handled** parameter to suppress the default **Report Wizard**.