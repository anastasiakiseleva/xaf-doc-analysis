Use the [DxGridListEditor.GridModel](xref:DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.GridModel) property to access grid component properties.

The code sample below demonstrates a controller in the Blazor project that changes a [](xref:DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel.ColumnResizeMode) property value.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

namespace YourSolutionName.Blazor.Server.Controllers;
public class ColumnResizeModeViewController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is DxGridListEditor gridListEditor) {
            gridListEditor.GridModel.ColumnResizeMode =
                DevExpress.Blazor.GridColumnResizeMode.ColumnsContainer;
        }
    }
}
```

***