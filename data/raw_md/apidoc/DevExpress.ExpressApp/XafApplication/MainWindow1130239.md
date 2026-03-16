---
uid: DevExpress.ExpressApp.XafApplication.MainWindow
name: MainWindow
type: Property
summary: Provides access to the application's main [Window](xref:112608).
syntax:
  content: |-
    [Browsable(false)]
    public virtual Window MainWindow { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Window
    description: A [](xref:DevExpress.ExpressApp.Window) object that represents the current application's main Window.
seealso: []
---
A main Window is the Window which is first displayed when starting the application (except the logon Window). This Window contains the base features of the application. To determine whether a Window is main use the [Window.IsMain](xref:DevExpress.ExpressApp.Window.IsMain) property.

You can customize the main Window. For this purpose, access it via the **MainWindow** property.