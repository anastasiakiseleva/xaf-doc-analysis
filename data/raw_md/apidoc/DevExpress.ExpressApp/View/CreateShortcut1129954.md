---
uid: DevExpress.ExpressApp.View.CreateShortcut
name: CreateShortcut()
type: Method
summary: Returns key information on the current [](xref:DevExpress.ExpressApp.View).
syntax:
  content: public ViewShortcut CreateShortcut()
  return:
    type: DevExpress.ExpressApp.ViewShortcut
    description: A [](xref:DevExpress.ExpressApp.ViewShortcut) object that provides access to the current View's identifiers.
seealso: []
---
A Shortcut represent the key information on a View:  object type, key property value of the View's current object and ID. This information is necessary to create and locate Views. Use this method to store information on a particular View to create it via the [XafApplication.ProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.ProcessShortcut(DevExpress.ExpressApp.ViewShortcut)) method. For instance, this technique is used in the **ViewNavigationController** that stores the history of Views displayed in the current Window.