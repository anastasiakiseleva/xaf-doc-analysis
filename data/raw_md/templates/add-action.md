# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
// ...
public class CustomViewController : ViewController {
    public CustomViewController() {
        SimpleAction customAction = new SimpleAction(this, "CustomAction", PredefinedCategory.View);
        // or
        customAction.Category = PredefinedCategory.View.ToString();
        // or 
        customAction.Category = "View";
        // or 
        customAction.Category = "MyCustomCategory";
    }
}
```
***
[`ViewController`]: xref:DevExpress.ExpressApp.ViewController
[`SimpleAction`]: xref:DevExpress.ExpressApp.Actions.SimpleAction
