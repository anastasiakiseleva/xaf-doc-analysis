---
uid: DevExpress.ExpressApp.DashboardViewCreatingEventArgs
name: DashboardViewCreatingEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.DashboardViewCreating](xref:DevExpress.ExpressApp.XafApplication.DashboardViewCreating) event.
syntax:
  content: 'public class DashboardViewCreatingEventArgs : ViewCreatingEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.DashboardViewCreatingEventArgs._members
  altText: DashboardViewCreatingEventArgs Members
---
The **DashboardViewCreatingEventArgs** class declares properties specific to the [XafApplication.DashboardViewCreating](xref:DevExpress.ExpressApp.XafApplication.DashboardViewCreating) event which is designed to create custom [Dashboard Views](xref:112611). Assign the created Dashboard View to the [DashboardViewCreatingEventArgs.View](xref:DevExpress.ExpressApp.DashboardViewCreatingEventArgs.View) property.

This class is inherited from the [](xref:DevExpress.ExpressApp.ViewCreatingEventArgs) class. So, you can use the [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace), [ViewCreatingEventArgs.ViewID](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID) and [ViewCreatingEventArgs.IsRoot](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.IsRoot) property values when creating a Dashboard View.