---
uid: DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem})
name: CustomizeViewItemControl(DetailView, Controller, Action<ViewItem>)
type: Method
summary: Allows you to access and customize controls of [View Items](xref:112612) the specified Detail View contains.
syntax:
  content: public static void CustomizeViewItemControl(this DetailView view, Controller controller, Action<ViewItem> customizeAction)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.DetailView
    description: A @DevExpress.ExpressApp.DetailView that contains the View Items whose controls the *customizeAction* method customizes.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [Controller](xref:112621) to customize controls of View Items.
  - id: customizeAction
    type: System.Action{DevExpress.ExpressApp.Editors.ViewItem}
    description: A method to customize controls of View Items.
seealso: []
---
The following code snippet specifies a minimum value in a `SpinEdit` control:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.XtraEditors;
// ...
public class SetMinValueController : ObjectViewController<DetailView, DemoTask> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl(this, SetMinValue);
    }
    private void SetMinValue(ViewItem viewItem) {
        SpinEdit spinEdit = viewItem.Control as SpinEdit;
        if (spinEdit != null) {
            spinEdit.Properties.MinValue = 0;
        }
    }
}
```
***

