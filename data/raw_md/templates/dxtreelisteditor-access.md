```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace YourSolutionName.Blazor.Server.Controllers;
public class ColumnResizeModeViewController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is DxTreeListEditor treeListEditor) {
            treeListEditor.TreeListModel.ColumnResizeMode =
                DevExpress.Blazor.TreeListColumnResizeMode.ColumnsContainer;
        }
    }
}
```