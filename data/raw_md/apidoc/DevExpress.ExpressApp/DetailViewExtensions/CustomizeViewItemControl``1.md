---
uid: DevExpress.ExpressApp.DetailViewExtensions.CustomizeViewItemControl``1(DevExpress.ExpressApp.DetailView,DevExpress.ExpressApp.Controller,System.Action{``0})
name: CustomizeViewItemControl<T>(DetailView, Controller, Action<T>)
type: Method
summary: Allows you to access controls of [View Items](xref:112612) the specified Detail View contains.
syntax:
  content: |-
    public static void CustomizeViewItemControl<T>(this DetailView view, Controller controller, Action<T> customizeAction)
        where T : ViewItem
  parameters:
  - id: view
    type: DevExpress.ExpressApp.DetailView
    description: A @DevExpress.ExpressApp.DetailView that contains the View Items whose controls the *customizeAction* method customizes.
  - id: controller
    type: DevExpress.ExpressApp.Controller
    description: A Controller to customize controls of View Items.
  - id: customizeAction
    type: System.Action{{T}}
    description: A method to customize controls of View Items.
  typeParameters:
  - id: T
    description: The type of View Items.
seealso: []
---
The following code snippet customizes controls of [Date Property Editors](xref:113536).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class CustomizeDateEditorController : ObjectViewController<DetailView, DemoTask> {
    protected override void OnActivated() {
        base.OnActivated();
        View.CustomizeViewItemControl<DatePropertyEditor>(this, CustomizeDateEditor);
    }
    private void CustomizeDateEditor(DatePropertyEditor propertyEditor) {
        propertyEditor.Control.Properties.ShowWeekNumbers = true;
    }
}
```
***

The following image demonstrates how this Controller affects the UI.

![Custom date editor](~/images/CustomizeViewItemControl_result.png)