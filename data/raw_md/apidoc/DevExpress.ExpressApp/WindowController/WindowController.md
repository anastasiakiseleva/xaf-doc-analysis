---
uid: DevExpress.ExpressApp.WindowController
name: WindowController
type: Class
summary: Represents a [Window Controller](xref:112621).
syntax:
  content: 'public class WindowController : Controller'
seealso:
- linkId: DevExpress.ExpressApp.WindowController._members
  altText: WindowController Members
---
A **Window Controller** class is a descendant of the [](xref:DevExpress.ExpressApp.Controller) class. Use it as an ancestor for a custom Controller which is intended to perform features with a [Window](xref:112608). To implement custom code to be performed at runtime, use the Controller class' mechanisms of activation and deactivation, i.e. handle the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) and [Controller.Deactivated](xref:DevExpress.ExpressApp.Controller.Deactivated) events. Window Controllers are activated in Windows only (not in Frames). You can access the parent Window via the [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property.

You can specify the Windows for which a Window Controller will be activated. For this purpose, use the [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) property. You can also prohibit Controller activation for a particular Window by overriding the **WindowController.OnWindowChanging** method.

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

If you need to implement features with [Views](xref:112611) only, use the [](xref:DevExpress.ExpressApp.ViewController) class as an ancestor. This class is the second descendant of the [](xref:DevExpress.ExpressApp.Controller) class, that can be used to implement features.