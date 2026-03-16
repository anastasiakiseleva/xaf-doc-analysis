---
uid: DevExpress.ExpressApp.Controller.FrameAssigned
name: FrameAssigned
type: Event
summary: Occurs after a [Frame (Window)](xref:112608) has been assigned to a Controller.
syntax:
  content: public event EventHandler FrameAssigned
seealso: []
---
When the **FrameAssigned** is raised, all Controllers loaded to the [Application Model](xref:112580) are created, and their [Controller.Frame](xref:DevExpress.ExpressApp.Controller.Frame) property is initialized. However a [View](xref:112611) is not yet assigned to these Controllers. Handle this event to perform specific actions with the current Controller or its Frame. For instance, you can access another [built-in](xref:113016) or custom Controller using the **Frame.GetController** method. The following code demonstrates how to deactivate a standard Controller by handling the **FrameAssigned** event.

# [C#](#tab/tabid-csharp)

```csharp
public partial class MyCustomController : ViewController {
   // ...
   private void MyCustomController_FrameAssigned(object sender, EventArgs e) {
      AboutInfoController controller = Frame.GetController<AboutInfoController>();
      if (controller != null) {
          controller.Active.SetItemValue("DisabledByMyCustomController", false);
      }
   }
}
```
***

To perform specific actions with a [](xref:DevExpress.ExpressApp.ViewController) before it is activated, override the **OnViewChanging** or **OnViewChanged** method.

To perform specific actions with a [](xref:DevExpress.ExpressApp.WindowController) before it is activated, override the **OnWindowChanging** method.