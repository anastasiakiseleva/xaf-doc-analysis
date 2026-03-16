---
uid: DevExpress.ExpressApp.Controller
name: Controller
type: Class
summary: The base class for [Controllers](xref:112621).
syntax:
  content: 'public abstract class Controller : Component, ISupportUpdate'
seealso:
- linkId: DevExpress.ExpressApp.Controller._members
  altText: Controller Members
---

Use Controllers to change your application's flow or implement custom user interaction. Custom code in a Controller is executed when XAF creates a [Window](xref:112608) or [Frame](xref:112608) for this Controller.

Controllers also serve as containers for [Actions](xref:112622).

Controllers in XAF support [dependency injection](xref:404364) in .NET ASP.NET Core Blazor and Windows Forms applications.

To implement a Controller, inherit from the `Controller` class or one of its descendants, such as:

[](xref:DevExpress.ExpressApp.ViewController)
:   Used to implement custom features in nested or root [Views](xref:112611)

[](xref:DevExpress.ExpressApp.WindowController)
:   Used to implement custom features in [Windows](xref:112608).

## Visual Studio Controller Template

The DevExpress [Template Kit](xref:405447#create-a-new-item) includes ready-to-use Controller templates that allow you to create a custom Controller in your project. 

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

## Built-in Controller Customization

XAF supplies built-in Controllers to perform basic functions in ASP.NET Core Blazor and Windows Forms applications. To customize the behavior of a particular Controller in code, inherit from it or subscribe to its events. For additional information, refer to the following topics:

* [](xref:112621)
* [](xref:112676)


XAF automatically instantiates public Controllers with public parameterless constructors.

## Custom Code in Controllers

To provide custom code that XAF performs at runtime, use Controller's activation and deactivation mechanisms.

To activate or deactivate a Controller, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property.

To determine the current state of a Controller, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property in a conditional expression. Alternatively, use the [BoolList.ResultValue](xref:DevExpress.ExpressApp.Utils.BoolList.ResultValue) property of the object that the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property returns.

To provide custom code that XAF executes each time a Controller is activated or deactivated, handle the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) and [Controller.Deactivated](xref:DevExpress.ExpressApp.Controller.Deactivated) events or override the `OnActivated` and `OnDeactivated` methods.

To access a Controller's Action collection in code, use the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) property.
