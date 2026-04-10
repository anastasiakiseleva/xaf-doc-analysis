---
uid: DevExpress.ExpressApp.Controller.AfterConstruction
name: AfterConstruction
type: Event
summary: Occurs after a Controller is created.
syntax:
  content: public event EventHandler AfterConstruction
seealso: []
---
Handle this event to perform specific actions directly after creating the current Controller.

The following example specifies the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) property:

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