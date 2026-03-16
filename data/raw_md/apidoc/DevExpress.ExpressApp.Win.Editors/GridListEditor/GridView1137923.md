---
uid: DevExpress.ExpressApp.Win.Editors.GridListEditor.GridView
name: GridView
type: Property
summary: Provides access to the Grid Control's [View](xref:3464) that is used to display data in the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor).
syntax:
  content: public GridView GridView { get; }
  parameters: []
  return:
    type: DevExpress.XtraGrid.Views.Grid.GridView
    description: A [](xref:DevExpress.XtraGrid.Views.Grid.GridView) object that is the **GridControl**'s View used to display data in the **GridListEditor**.
seealso: []
---
The **GridListEditor** uses the **GridControl** as its control. The **GridControl** displays data in a UI via special Views. Note, that these Views are not related to the [Views](xref:112611) used in **XAF** to construct a UI. The **GridControl**'s Views are represented by the **GridView** class instances. The **GridView** class provides a two-dimensional representation of data from a data source in grid format.

The example below demonstrates how to set the alternating row color for all [List Views](xref:112611#list-view) in a WinForms application.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Drawing;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class ListEditorController : ViewController<ListView> {
    private GridListEditor listEditor;
    private void ListEditor_ControlsCreated(object sender, EventArgs e) {
        DevExpress.XtraGrid.Views.Grid.GridView gridView = ((GridListEditor)View.Editor).GridView;
        gridView.OptionsView.EnableAppearanceOddRow = true;
        gridView.Appearance.OddRow.BackColor = Color.FromArgb(244, 244, 244);
    }
    protected override void OnActivated() {
        base.OnActivated();
        listEditor = View.Editor as GridListEditor;
        if (listEditor != null) {
            listEditor.ControlsCreated += ListEditor_ControlsCreated;
        }
    }
    protected override void OnDeactivated() {
        if(listEditor != null) {
            listEditor.ControlsCreated -= ListEditor_ControlsCreated;
        }
        base.OnDeactivated();
    }
}
```
***

> [!NOTE]
> To run this code, add the _DevExpress.ExpressApp.XtraGrid.v<:xx.x:>.dll_ assembly to References.