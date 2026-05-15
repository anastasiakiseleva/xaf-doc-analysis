---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.PivotGridModel
name: PivotGridModel
type: Property
summary: Exposes members of the underlying @DevExpress.Blazor.PivotTable.DxPivotTable class.
syntax:
  content: public DxPivotTableModel PivotGridModel { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Blazor.Editors.Models.DxPivotTableModel
    description: An object that you can use to access @DevExpress.Blazor.PivotTable.DxPivotTable settings.
seealso: []
---
Use the `PivotGridModel` property to access Pivot Grid component properties.

The following code sample shows a controller in the Blazor project that enables [Grand Totals](xref:DevExpress.Blazor.PivotTable.DxPivotTable.ShowRowGrandTotals) in the Pivot Grid:

# [SolutionName.Blazor.Server\Controllers\PivotGridController.cs](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public class PivotGridController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is DxPivotGridListEditor pivotListEditor) {
            pivotListEditor.PivotGridModel.ShowRowGrandTotals = true;
        }
    }
}
```

***

For more information about Component Models, refer to the following topic: <xref:404767>.