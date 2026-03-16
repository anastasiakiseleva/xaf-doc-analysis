---
uid: DevExpress.ExpressApp.XafApplication.ProcessShortcut(DevExpress.ExpressApp.ViewShortcut)
name: ProcessShortcut(ViewShortcut)
type: Method
summary: Creates a View by a specified shortcut.
syntax:
  content: public View ProcessShortcut(ViewShortcut shortcut)
  parameters:
  - id: shortcut
    type: DevExpress.ExpressApp.ViewShortcut
    description: A [](xref:DevExpress.ExpressApp.ViewShortcut) object that provides key information on the View to be created.
  return:
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) object that represents the [View](xref:112611) to be created.
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CustomProcessShortcut
- linkId: DevExpress.ExpressApp.View.CreateShortcut
- linkId: "113471"
---
A shortcut represent the key information on a View:  object type, key property value of the View's current object and ID. You can use a shortcut to create a View. To do this, call the **ProcessShortcut** method passing the required shortcut. This method will create an Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)) and a [List View or Detail View](xref:112611) in it. The View type and other View settings are set from the [Application Model](xref:112580)'s **Views** | **View** node which is specified by the [ViewShortcut.ViewId](xref:DevExpress.ExpressApp.ViewShortcut.ViewId) property. For example, this method is used in the **ViewNavigationController** that stores the shortcuts of the Views displayed in the current Window.

If you need to create a custom View by a shortcut, handle the [XafApplication.CustomProcessShortcut](xref:DevExpress.ExpressApp.XafApplication.CustomProcessShortcut) event which is raised when the **ProcessShortcut** method is called.