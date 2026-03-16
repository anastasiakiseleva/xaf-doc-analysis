---
uid: DevExpress.ExpressApp.WindowController.SetWindow(DevExpress.ExpressApp.Window)
name: SetWindow(Window)
type: Method
summary: Sets a specified [Window](xref:112608) for a Window Controller.
syntax:
  content: public void SetWindow(Window newWindow)
  parameters:
  - id: newWindow
    type: DevExpress.ExpressApp.Window
    description: A [](xref:DevExpress.ExpressApp.Window) object that represents a Window to be set for the current Window Controller.
seealso: []
---
Window Controllers are used to perform specific actions with their Window when they are activated (see [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated)). This method sets the Window specified by the _Window_ parameter to the current Window Controller. Not any Window can be set for a Window Controller. If the specified Window does not satisfy to the Window Controller's [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) property, it is not assigned and the Controller is not activated.

Generally, you do not need to use this method. When a Window is created, the [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property of all the Window Controllers from its [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) library is set to this Window object. You can override the **WindowController.OnWindowChanging** method that is raised before setting a Window. For instance, you can prohibit activation of the current Window Controller, if it is not intended for the Window which is being set for it.