---
uid: DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{DevExpress.ExpressApp.Editors.ViewItem},System.String[])
name: CustomizeViewItemControl(DetailView, Controller, Action<ViewItem>, String[])
type: Method
summary: Allows you to access and customize controls of specified [View Items](xref:112612).
syntax:
  content: public static void CustomizeViewItemControl(this DetailView view, Controller controller, Action<ViewItem> customizeAction, params string[] viewItemsId)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.DetailView
    description: A @DevExpress.ExpressApp.DetailView that contains the specified View Items.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [Controller](xref:112621) to customize controls of the specified View Items.
  - id: customizeAction
    type: System.Action{DevExpress.ExpressApp.Editors.ViewItem}
    description: A method to customize controls of the specified View Items.
  - id: viewItemsId
    type: System.String[]
    description: Identifiers of View Items.
seealso: []
---
The following code snippet customizes controls of the `ActualWorkHours` and `EstimatedWorkHours` View Items:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Editors;
using DevExpress.XtraEditors;
// ...
public class SetMinValueController : ObjectViewController<DetailView, DemoTask> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl(this, SetMinValue, nameof(DemoTask.ActualWorkHours), nameof(DemoTask.EstimatedWorkHours));
    }
    private void SetMinValue(ViewItem viewItem) {
        SpinEdit spinEdit = (SpinEdit)viewItem.Control;
        spinEdit.Properties.MinValue = 0;
    }
}
```
***

You can find the View Item's identifier in the Model Editor.

![Id property in Model Editor](~/images/ViewItem_ID.png)
