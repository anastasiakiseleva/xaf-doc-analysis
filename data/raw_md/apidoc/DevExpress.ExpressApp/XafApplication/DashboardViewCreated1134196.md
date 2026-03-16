---
uid: DevExpress.ExpressApp.XafApplication.DashboardViewCreated
name: DashboardViewCreated
type: Event
summary: Occurs after a [Dashboard View](xref:112611) has been created.
syntax:
  content: public event EventHandler<DashboardViewCreatedEventArgs> DashboardViewCreated
seealso: []
---
Handle this event to customize the [](xref:DevExpress.ExpressApp.DashboardView) that has been created via the [XafApplication.CreateDashboardView](xref:DevExpress.ExpressApp.XafApplication.CreateDashboardView(DevExpress.ExpressApp.IObjectSpace,System.String,System.Boolean)) method. This Dashboard View is specified by the handler's [DashboardViewCreatedEventArgs.View](xref:DevExpress.ExpressApp.DashboardViewCreatedEventArgs.View) parameter.