---
uid: DevExpress.ExpressApp.Blazor.Editors.DxPivotGridListEditor.ComponentCaptured
name: ComponentCaptured
type: Event
summary: Occurs after the underlying @DevExpress.Blazor.PivotTable component is created for the current model and allows access to the component instance.
syntax:
  content: public event EventHandler<PivotGridCapturedEventArgs> ComponentCaptured
seealso: []
---
A component model replicates [parameters](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/#component-parameters) of the related component. You can use these parameters to configure the underlying component before creation. However, the model does not allow you to access the current component state or call its methods directly.

Handle the `ComponentCaptured` event to access underlying component instance and its full API.

# [SolutionName.Blazor.Server\Controllers\CollapseAllRowsController.cs](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor.Editors;

public class CollapseAllRowsController : ViewController {
    public class TestController : ViewController<ListView> {
        protected override void OnViewControlsCreated() {
            base.OnViewControlsCreated();
            if (View.Editor is DxPivotGridListEditor editor) {
                editor.ComponentCaptured += (s, e) => {
                    // Collapse every PivotGrig row
                    e.PivotGrid.CollapseAllRows();
                };
            }
        }
    }
}
```
***
