# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Actions;
// ...
public class MyViewController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        ObjectMethodActionsViewController controller = Frame.GetController<ObjectMethodActionsViewController>();
        if (controller != null) {
            SimpleAction markCompletedAction = controller.Actions["Task.MarkCompleted"] as SimpleAction;
            // ...
        }
        // ...
    }
}
```
***