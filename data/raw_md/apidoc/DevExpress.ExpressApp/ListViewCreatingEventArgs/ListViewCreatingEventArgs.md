---
uid: DevExpress.ExpressApp.ListViewCreatingEventArgs
name: ListViewCreatingEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.ListViewCreating](xref:DevExpress.ExpressApp.XafApplication.ListViewCreating) event.
syntax:
  content: 'public class ListViewCreatingEventArgs : ViewCreatingEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ListViewCreatingEventArgs._members
  altText: ListViewCreatingEventArgs Members
---
The **ListViewCreatingEventArgs** class declares properties specific to the [XafApplication.ListViewCreating](xref:DevExpress.ExpressApp.XafApplication.ListViewCreating) event designed to create custom [List Views](xref:112611). Use the [ListViewCreatingEventArgs.CollectionSource](xref:DevExpress.ExpressApp.ListViewCreatingEventArgs.CollectionSource) property value as a collection source for the new List View. Assign the created List View to the [ListViewCreatingEventArgs.View](xref:DevExpress.ExpressApp.ListViewCreatingEventArgs.View) property.

This class is inherited from the [](xref:DevExpress.ExpressApp.ViewCreatingEventArgs) class. So, you can use the [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace), [ViewCreatingEventArgs.ViewID](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID) and [ViewCreatingEventArgs.IsRoot](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.IsRoot) property values when creating a List View.