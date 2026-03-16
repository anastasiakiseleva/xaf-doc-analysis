---
uid: DevExpress.ExpressApp.Frame.RegisterController(DevExpress.ExpressApp.Controller)
name: RegisterController(Controller)
type: Method
summary: Registers a specified [Controller](xref:112621) within a [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection.
syntax:
  content: public void RegisterController(Controller controller)
  parameters:
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [](xref:DevExpress.ExpressApp.Controller) object to be registered within the current [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection.
seealso: []
---
The **RegisterController** method is intended for internal use. It adds the Controller specified by the _controller_ parameter to the current [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection, and sets the [Controller.Frame](xref:DevExpress.ExpressApp.Controller.Frame) property to this Frame.  If the passed Controller is already registered in another Frame, an exception is raised.

Use a Frame's **GetController\<ControllerType>** method to access a Controller.