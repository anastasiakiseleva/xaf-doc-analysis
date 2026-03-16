---
uid: DevExpress.ExpressApp.XafApplication.DetailViewCreated
name: DetailViewCreated
type: Event
summary: Occurs after a [Detail View](xref:112611) has been created.
syntax:
  content: public event EventHandler<DetailViewCreatedEventArgs> DetailViewCreated
seealso: []
---
Handle this event to customize the [](xref:DevExpress.ExpressApp.DetailView) that has been created via the [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) method. This Detail View is specified by the handler's [DetailViewCreatedEventArgs.View](xref:DevExpress.ExpressApp.DetailViewCreatedEventArgs.View) parameter.