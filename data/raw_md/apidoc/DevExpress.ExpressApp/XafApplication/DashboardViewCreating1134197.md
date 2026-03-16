---
uid: DevExpress.ExpressApp.XafApplication.DashboardViewCreating
name: DashboardViewCreating
type: Event
summary: Occurs when creating a [Dashboard View](xref:112611).
syntax:
  content: public event EventHandler<DashboardViewCreatingEventArgs> DashboardViewCreating
seealso: []
---
Handle this event to provide a custom Dashboard View instead of a default one. Use the handler's [ViewCreatingEventArgs.ViewID](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID) parameter to get information on the created Dashboard View. To do this use the application's [XafApplication.FindModelView](xref:DevExpress.ExpressApp.XafApplication.FindModelView(System.String)) method passing the View ID as a parameter. Create the Dashboard View in the Object Space passed as the handler's [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace) parameter.