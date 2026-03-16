---
uid: DevExpress.ExpressApp.Editors.ListEditor.ControlsCreated
name: ControlsCreated
type: Event
summary: Occurs after a [](xref:DevExpress.ExpressApp.Editors.ListEditor)'s control is created.
syntax:
  content: public event EventHandler ControlsCreated
seealso: []
---
Handle the **ControlsCreated** event to modify a [List Editor](xref:113189)'s control after it is created in a [List View](xref:112611). For example, the code below shows how to access [GridView](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.GridView) and change the *FocusedCell.BackColor** property to orange when the [GridListEditor](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) is used to represent data. See the (xref:113189) topic for more details about available **ListEditor** classes.


# [C#](#tab/tabid-csharp)
```csharp
public class ListEditorController : ViewController<ListView> {
    private GridListEditor listEditor = null;
    private void listEditor_ControlsCreated(object sender, EventArgs e) {
        ((GridListEditor)sender).GridView.Appearance.FocusedCell.BackColor = Color.Orange;
    }
    protected override void OnActivated() {
        base.OnActivated();
        listEditor = View.Editor as GridListEditor;
        if (listEditor != null) {
            listEditor.ControlsCreated += listEditor_ControlsCreated;
            }
    }
    protected override void OnDeactivated() {
        if (listEditor != null) {
            listEditor.ControlsCreated -= listEditor_ControlsCreated;
            }
        base.OnDeactivated();
    }
}
```
***

