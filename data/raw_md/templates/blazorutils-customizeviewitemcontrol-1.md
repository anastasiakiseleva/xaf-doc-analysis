# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;
using DevExpress.ExpressApp.Blazor.Utils;
// ...
public class LookupActionVisibilityController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<LookupPropertyEditor>(this, e => {
            e.HideNewButton();
            e.HideEditButton();
        });
    }
}
```
***