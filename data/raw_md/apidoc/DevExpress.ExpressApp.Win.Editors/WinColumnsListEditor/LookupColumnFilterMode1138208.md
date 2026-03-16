---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.LookupColumnFilterMode
name: LookupColumnFilterMode
type: Property
summary: Specifies how the [Automatic Filtering Row](xref:10623) is displayed and how [Find Panel](xref:8869) performs a search in [Server](xref:118450) mode (see [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)) for lookup columns.
syntax:
  content: public ColumnFilterMode LookupColumnFilterMode { get; set; }
  parameters: []
  return:
    type: DevExpress.XtraGrid.ColumnFilterMode
    description: A [](xref:DevExpress.XtraGrid.ColumnFilterMode) enumeration value specifying how the Find Panel performs searching in **server** mode.
seealso: []
---
The following table demonstrates how the [Automatic Filtering Row](xref:10623) and [Find Panel](xref:17144) behavior changes depending on the **LookupColumnFilterMode** value in lookup columns.

| **LookupColumnFilterMode** Value | Auto Filter Row Behavior | Find Panel Behavior |
|---|---|---|
| **ColumnFilterMode.Value** | The Auto Filter Row cells are displayed using lookup editors. | The Find Panel searches over key property values of objects displayed by the [](xref:DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor) in [Server](xref:118450) mode. |
| **ColumnFilterMode.DisplayText** | The Auto Filter Row is displayed using text boxes. | The Find Panel searches over the display text of the visible columns. |

You can use the following Controller to access this property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class LookupColumnFilterModeController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        GridListEditor gridListEditor = View.Editor as GridListEditor;
        if (gridListEditor != null) {
            gridListEditor.LookupColumnFilterMode = DevExpress.XtraGrid.ColumnFilterMode.DisplayText;
        }
    }
}
```
***

To change the behavior for a specific column only, use the [GridColumn.FilterMode](xref:DevExpress.XtraGrid.Columns.GridColumn.FilterMode) property. To access this property, use the approach demonstrated in the following article [](xref:402154).