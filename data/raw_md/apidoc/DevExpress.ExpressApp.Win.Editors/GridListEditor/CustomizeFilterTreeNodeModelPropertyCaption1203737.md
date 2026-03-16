---
uid: DevExpress.ExpressApp.Win.Editors.GridListEditor.CustomizeFilterTreeNodeModelPropertyCaption
name: CustomizeFilterTreeNodeModelPropertyCaption
type: Event
summary: Occurs when a filter visual presentation is formed.
syntax:
  content: public event EventHandler<CustomizeFilterTreeNodeModelPropertyCaptionEventArgs> CustomizeFilterTreeNodeModelPropertyCaption
seealso: []
---
Handle this event to customize a property caption when it is shown in the [Filter Panel](xref:1424) and in the [Filter Editor](xref:114635) of the [](xref:DevExpress.XtraGrid.GridControl).

For example, you can customize a column caption in the application model to show special text in the column header and at the same time, keep the default property caption in the Filter Panel and in the Filter Editor.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
//...
public class CustomizeFilterTreeNodeModelPropertyCaptionController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        GridListEditor editor = View.Editor as GridListEditor;
        if(editor != null) {
            editor.CustomizeFilterTreeNodeModelPropertyCaption += 
Editor_CustomizeFilterTreeNodeModelPropertyCaption;
        }
    }
    private void Editor_CustomizeFilterTreeNodeModelPropertyCaption(object sender, 
CustomizeFilterTreeNodeModelPropertyCaptionEventArgs e) {
        e.Caption = e.DefaultCaption;
    }
}
```
***
