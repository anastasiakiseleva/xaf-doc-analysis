---
uid: DevExpress.ExpressApp.ViewCreatingEventArgs
name: ViewCreatingEventArgs
type: Class
summary: The base class for event arguments passed to the [XafApplication.ListViewCreating](xref:DevExpress.ExpressApp.XafApplication.ListViewCreating), [XafApplication.DetailViewCreating](xref:DevExpress.ExpressApp.XafApplication.DetailViewCreating), [XafApplication.DashboardViewCreating](xref:DevExpress.ExpressApp.XafApplication.DashboardViewCreating) and [XafApplication.ViewCreating](xref:DevExpress.ExpressApp.XafApplication.ViewCreating) events.
syntax:
  content: 'public class ViewCreatingEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ViewCreatingEventArgs._members
  altText: ViewCreatingEventArgs Members
---
The **ViewCreatingEventArgs** class declares properties specific to the events which are designed  to create custom [Views](xref:112611). These properties are required to create both a [](xref:DevExpress.ExpressApp.DetailView) and [](xref:DevExpress.ExpressApp.ListView). The created View must be assigned to the [ViewCreatingEventArgs.View](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.View) property to prevent further creation of a default View.

This class' descendants are used when creating a particular Detail or List View: [](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs) and [](xref:DevExpress.ExpressApp.ListViewCreatingEventArgs).