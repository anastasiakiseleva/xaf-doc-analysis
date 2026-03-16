---
uid: DevExpress.ExpressApp.DetailViewCreatingEventArgs
name: DetailViewCreatingEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.DetailViewCreating](xref:DevExpress.ExpressApp.XafApplication.DetailViewCreating) event.
syntax:
  content: 'public class DetailViewCreatingEventArgs : ViewCreatingEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.DetailViewCreatingEventArgs._members
  altText: DetailViewCreatingEventArgs Members
---
The **DetailViewCreatingEventArgs** class declares properties specific to the [XafApplication.DetailViewCreating](xref:DevExpress.ExpressApp.XafApplication.DetailViewCreating) event which is designed to create custom [Detail Views](xref:112611). Use the [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) property value as the current object of the new Detail View. Assign the created Detail View to the [DetailViewCreatingEventArgs.View](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.View) property.

This class is inherited from the [](xref:DevExpress.ExpressApp.ViewCreatingEventArgs) class. So, you can use the [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace), [ViewCreatingEventArgs.ViewID](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID) and [ViewCreatingEventArgs.IsRoot](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.IsRoot) property values when creating a Detail View.