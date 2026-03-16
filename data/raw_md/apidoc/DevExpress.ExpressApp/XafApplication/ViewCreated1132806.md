---
uid: DevExpress.ExpressApp.XafApplication.ViewCreated
name: ViewCreated
type: Event
summary: Occurs after a [View](xref:112611) has been created.
syntax:
  content: public event EventHandler<ViewCreatedEventArgs> ViewCreated
seealso: []
---
Handle this event to customize the [](xref:DevExpress.ExpressApp.View) that has been created via the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) or [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*)method. This Detail View is specified by the handler's [DetailViewCreatedEventArgs.View](xref:DevExpress.ExpressApp.DetailViewCreatedEventArgs.View) parameter. This List View is specified by the handler's [ListViewCreatedEventArgs.ListView](xref:DevExpress.ExpressApp.ListViewCreatedEventArgs.ListView) parameter.