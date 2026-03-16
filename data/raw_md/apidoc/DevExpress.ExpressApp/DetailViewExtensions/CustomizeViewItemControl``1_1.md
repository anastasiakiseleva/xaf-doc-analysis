---
uid: DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0},System.String[])
name: CustomizeViewItemControl<T>(DetailView, Controller, Action<T>, String[])
type: Method
summary: Allows you to access and customize controls of specified [View Items](xref:112612).
syntax:
  content: |-
    public static void CustomizeViewItemControl<T>(this DetailView view, Controller controller, Action<T> customizeAction, params string[] viewItemsId)
        where T : ViewItem
  parameters:
  - id: view
    type: DevExpress.ExpressApp.DetailView
    description: A @DevExpress.ExpressApp.DetailView that contains the specified View Items.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A [Controller](xref:112621) to customize controls of the specified View Items.
  - id: customizeAction
    type: System.Action{{T}}
    description: A method to customize controls of the specified View Items.
  - id: viewItemsId
    type: System.String[]
    description: Identifiers of View Items.
  typeParameters:
  - id: T
    description: The type of View Items.
seealso: []
---
The following code snippet customizes controls of the `StartDate` and `DueDate` [Date Property Editors](xref:113536).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class CustomizeDateEditorController : ObjectViewController<DetailView, DemoTask> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<DatePropertyEditor>(this, CustomizeDateEditor, nameof(DemoTask.StartDate), nameof(DemoTask.DueDate));
    }
    private void CustomizeDateEditor(DatePropertyEditor propertyEditor) {
        propertyEditor.Control.Properties.ShowWeekNumbers = true;
    }
}
```
***

The following image demonstrates how this Controller affects the UI.

![Custom date editor](~/images/CustomizeViewItemControl_result.png)

You can find the View Item's identifier in the Model Editor.

![Id property in Model Editor](~/images/ViewItem_ID.png)
