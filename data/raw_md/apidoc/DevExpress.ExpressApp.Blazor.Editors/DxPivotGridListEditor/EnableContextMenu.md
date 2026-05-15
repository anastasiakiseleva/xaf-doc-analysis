---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.EnableContextMenu
name: EnableContextMenu
type: Property
summary: Enables/disables the Pivot Grid context menu.
syntax:
  content: public bool EnableContextMenu { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if the context menu is enabled; otherwise, `false`.'
defaultMemberValue: "true"
seealso: []
---
The `DxPivotGridListEditor` displays the context menu for [filter area, column area and data field headers](xref:405459#areas).

![Pivot Grid context menu](~/images/pivot-grid/xaf-blazor-pivot-grid-context-menu.png)

Set the `EnableContextMenu` property to `false` to disable the context menu.

# [SolutionName.Blazor.Server\Controllers\DisablePivotContextMenuController.cs](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public class DisablePivotContextMenuController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        if (View.Editor is DxPivotGridListEditor pivotListEditor) {
            pivotListEditor.EnableContextMenu = false;
        }
    }
}
```
 
***