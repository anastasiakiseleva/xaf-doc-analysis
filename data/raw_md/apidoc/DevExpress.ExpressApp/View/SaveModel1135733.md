---
uid: DevExpress.ExpressApp.View.SaveModel
name: SaveModel()
type: Method
summary: Writes information on a View to the [Application Model](xref:112580).
syntax:
  content: public void SaveModel()
seealso: []
---
Use this method to save the current settings of a View's editor(s) to the [Application Model](xref:112580) node specified by the View's [View.Model](xref:DevExpress.ExpressApp.View.Model) property. These settings include those that correspond to properties of the Views | DetailView | Items and Views | DetailView | Layout  or, Views | ListView, and Views | ListView | Columns nodes.

By default, this method is automatically called to save the current properties of a View's editor(s) before assigning a new value to the [View.Model](xref:DevExpress.ExpressApp.View.Model) property.

Handle the [View.ModelSaving](xref:DevExpress.ExpressApp.View.ModelSaving) event to cancel saving information on a View's editors to the Application Model.

Handle the [View.CustomModelSaving](xref:DevExpress.ExpressApp.View.CustomModelSaving) event to perform a custom technique for saving the information.

Handle the [View.ModelSaved](xref:DevExpress.ExpressApp.View.ModelSaved) event to save custom information on a View to the Application Model before it is updated.
## Example

The code below saves the current application state:

[!include[<MySolution.Win\Controllers\MyController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp.Win;
// ...
public class MyController : ViewController { //or WindowController
    // ...
    private void action_Execute(object sender, SimpleActionExecuteEventArgs e) {
        // Save Model settings in all opened windows in a WinForms application.
        foreach(Frame frame in ((WinShowViewStrategyBase)Application.ShowViewStrategy).Windows) {
            frame.View.SaveModel();
            // OR
            // frame.SaveModel();
        }
        
        // OR
        // Save Model settings only in the main application window.
        // Application.MainWindow.SaveModel();
        
        // Save the latest Model settings to a Model difference storage.
        Application.SaveModelChanges();
    }

// ...
}
```
***