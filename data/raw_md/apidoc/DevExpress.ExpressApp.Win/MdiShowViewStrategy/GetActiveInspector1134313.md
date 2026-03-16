---
uid: DevExpress.ExpressApp.Win.MdiShowViewStrategy.GetActiveInspector
name: GetActiveInspector()
type: Method
summary: Returns the active Inspector [Window](xref:112608).
syntax:
  content: public WinWindow GetActiveInspector()
  return:
    type: DevExpress.ExpressApp.Win.WinWindow
    description: A [](xref:DevExpress.ExpressApp.Win.WinWindow) object representing the active Inspector Window.
seealso: []
---
An XAF Windows Forms application provides two types of Windows - **Explorer** and **Inspector**.

* **Explorer Window** - contains navigation items and can display several List and Detail Views in tabs (when the MDI is  used).
* **Inspector Window** - does not provide navigation items and displays a single View

The following example demonstrates how to use this method in a Window Controller to access a current Window and View in MDI mode:

[!include[<MySolution.Win/Controllers/CustomWindowController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)

```csharp{14}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win;
using DevExpress.Persistent.Base;
// ...
public class CustomWindowController : WindowController {
    public CustomWindowController() {
        SimpleAction myAction = new SimpleAction(this, "MyAction", PredefinedCategory.View);
        myAction.Execute += MyAction_Execute;
    }
    private void MyAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        MdiShowViewStrategy strategy = Application.ShowViewStrategy as MdiShowViewStrategy;
        if (strategy != null) {
            WinWindow currentWindow = strategy.GetActiveInspector();
            if (currentWindow != null) {
                View _view = currentWindow.View;
                // custom logic
            }
        }
    }
}
```
***