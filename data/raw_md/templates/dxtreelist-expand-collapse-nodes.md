```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Blazor.Server.Controllers;

public class TestController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if(View.Editor is DxTreeListEditor editor) {
            editor.TreeListComponentCaptured += (s, e) => {
                // Expand all nodes.
                e.TreeList.ExpandAll();
                // Collapse all nodes.
                e.TreeList.CollapseAll();
            };
        }
    }
}
```