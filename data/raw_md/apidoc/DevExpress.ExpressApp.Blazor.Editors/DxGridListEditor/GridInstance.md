---
uid: DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.GridInstance
name: GridInstance
type: Property
summary: Provides access to methods of the DxGrid control.
syntax:
  content: public IGrid GridInstance { get; }
  parameters: []
  return:
    type: DevExpress.Blazor.IGrid
    description: An `IGrid` object.
seealso: []
---
Use the `GridInstance` property to call methods of the grid control. To change grid properties, use `GridModel`.

The `DxGrid` instance becomes available after it is rendered. Always check that `GridInstance` is not null.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Blazor.Editors;

namespace MySolution.Blazor.Server.Controllers;

public class TestController : ViewController<ListView> {
    public TestController() {
        SimpleAction simpleAction = new SimpleAction(this, "Test Action", DevExpress.Persistent.Base.PredefinedCategory.Edit);
        simpleAction.Execute += (s, e) => {
            if(View.Editor is DxGridListEditor editor) {
                // Always check that GridInstance is not `null`.
                editor.GridInstance?.CollapseAllGroupRows();
            }
        };
    }
}
```

The following code sample uses the @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.GridComponentCaptured event to access `DxGrid` API:

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
> [!NOTE]
> Do not cache the grid instance in controller fields because the grid can be disposed of and then rendered again when a user navigates the XAF application. Handle the @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.GridComponentCaptured event every time you access the grid instance.