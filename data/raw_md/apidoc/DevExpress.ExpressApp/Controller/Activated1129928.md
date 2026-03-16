---
uid: DevExpress.ExpressApp.Controller.Activated
name: Activated
type: Event
summary: Occurs when a [](xref:DevExpress.ExpressApp.Controller) is activated.
syntax:
  content: public event EventHandler Activated
seealso:
- linkId: DevExpress.ExpressApp.Controller.Deactivated
- linkId: "402153"
- linkId: "112728"
- linkId: "112617"
- linkId: "112607"
---
This event represents the most useful aspect of Controllers. Handle this event to execute custom code when a Controller is activated, for example, to manage the Controller's Actions visibility and availability. You can also access the current [Window](xref:112608) and its [Action Containers](xref:112610) if this Controller is a [](xref:DevExpress.ExpressApp.WindowController) class descendant. If it is a [](xref:DevExpress.ExpressApp.ViewController) class descendant, you can customize the current [View](xref:112611).

> [!NOTE]
> View Controllers are activated after setting a View for their [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property. Window Controllers are activated after setting a Window for their [WindowController.Window](xref:DevExpress.ExpressApp.WindowController.Window) property.

A Controller is activated when the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection does not have any elements that have the _value_ set to **false** left.

For details on how to use Controllers, refer to the [Controllers](xref:112621) topic.