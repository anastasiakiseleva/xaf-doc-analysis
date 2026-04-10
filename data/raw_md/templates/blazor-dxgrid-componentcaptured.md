# [C#](#tab/tabid-csharp1)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Blazor.Server.Controllers;

public class TestController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if(View.Editor is DxGridListEditor editor) {
            editor.GridComponentCaptured += (s, e) => {
                e.Grid.CollapseAllGroupRows();
            };
        }
    }
}
```
***