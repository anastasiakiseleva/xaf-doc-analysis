---
uid: DevExpress.ExpressApp.ViewController
name: ViewController
type: Class
summary: A [View Controller](xref:112621).
syntax:
  content: 'public class ViewController : Controller'
seealso:
- linkId: DevExpress.ExpressApp.ViewController._members
  altText: ViewController Members
---
A **ViewController** class is a descendant of the [](xref:DevExpress.ExpressApp.Controller) class. Use it as an ancestor for a custom Controller which is intended to function with a [View](xref:112611). View Controllers are registered within both a [Window and Frame](xref:112608). You can access the parent [](xref:DevExpress.ExpressApp.Frame) using the [Controller.Frame](xref:DevExpress.ExpressApp.Controller.Frame) property, and its View using the [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property. The Object Space used by the current View can be accessed via the protected **ObjectSpace** property. To implement custom code to be performed at runtime, use the Controller's mechanisms for activation and deactivation, i.e., handle the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) and [Controller.Deactivated](xref:DevExpress.ExpressApp.Controller.Deactivated) events.

You can specify the Views for which a View Controller will be activated. For this purpose, use the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType), [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId), [ViewController.TargetViewNesting](xref:DevExpress.ExpressApp.ViewController.TargetViewNesting) and [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType) properties (see [How do I specify in which View (form) a Controller should be activated](xref:113103)). You can also prohibit Controller activation for a particular View by overriding the **ViewController.OnViewChanging** method.

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

If you need to implement features with Windows (e.g., customize a Window's [Template](xref:112609) or View), use the [](xref:DevExpress.ExpressApp.WindowController) class instead of **ViewController**.