---
uid: DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager.DashboardDesignerCreated
name: DashboardDesignerCreated
type: Event
summary: Occurs after a [](xref:DevExpress.DashboardWin.DashboardDesigner) control has been created.
syntax:
  content: public event EventHandler<DashboardDesignerShownEventArgs> DashboardDesignerCreated
seealso: []
---
Allows you to access the WinForms [](xref:DevExpress.DashboardWin.DashboardDesigner) control used to create and modify dashboards in WinForms XAF applications.

The [DashboardDesignerShownEventArgs.DashboardDesigner](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerShownEventArgs.DashboardDesigner) event parameter returns the created [](xref:DevExpress.DashboardWin.DashboardDesigner) and allows you to customize it.

Note that the event is raised before assigning the [DashboardDesigner.Dashboard](xref:DevExpress.DashboardWin.DashboardDesigner.Dashboard) property.