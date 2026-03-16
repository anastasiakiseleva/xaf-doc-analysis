---
uid: DevExpress.ExpressApp.Controller.AfterConstruction
name: AfterConstruction
type: Event
summary: Occurs after a Controller is created.
syntax:
  content: public event EventHandler AfterConstruction
seealso: []
---
Handle this event to perform specific actions directly after creating the current Controller. For instance, initialize the Controller's properties that are not listed in the **Designer**'s **Properties**window.

The following example demonstrates how to specify the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) property:

# [C#](#tab/tabid-csharp)

```csharp
public partial class MyCustomController : ViewController {
   // ...
   private void MyCustomController_AfterConstruction(object sender, EventArgs e) {
      TargetObjectType = typeof(ReportDataV2);
   }
}
```
***