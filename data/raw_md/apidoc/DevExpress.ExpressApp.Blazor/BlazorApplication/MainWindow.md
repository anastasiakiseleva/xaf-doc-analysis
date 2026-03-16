---
uid: DevExpress.ExpressApp.Blazor.BlazorApplication.MainWindow
name: MainWindow
type: Property
summary: Provides access to the Blazor application's main [Window](xref:112608).
syntax:
  content: public override Window MainWindow { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Window
    description: An object that represents the current application's main Window.
seealso: []
---
Overrides the [XafApplication.MainWindow](xref:DevExpress.ExpressApp.XafApplication.MainWindow) property.

A main Window is the Window which is first displayed when starting the application (except the logon Window). This Window contains the base features of the application. To determine whether a Window is main, use the [Window.IsMain](xref:DevExpress.ExpressApp.Window.IsMain) property.

You can customize the main Window. For this purpose, access it via the **MainWindow** property.