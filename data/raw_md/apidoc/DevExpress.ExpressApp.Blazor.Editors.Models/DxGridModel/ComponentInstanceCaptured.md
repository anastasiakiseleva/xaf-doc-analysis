---
uid: DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel.ComponentInstanceCaptured
name: ComponentInstanceCaptured
type: Event
summary: Occurs after the underlying component is created for the current model and allows access to the component instance.
syntax:
  content: public event EventHandler<ComponentInstanceCapturedEventArgs<IGrid>> ComponentInstanceCaptured
seealso: []
---
[!include[](~/templates/component-instance-captured-description.md)]

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public partial class GridListEditorController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        if (View.Editor is DxGridListEditor editor) {
            editor.GridModel.ComponentInstanceCaptured += (s, e) => {
                e.ComponentInstance.CollapseAllGroupRows();
            };
        }
    }
}
```