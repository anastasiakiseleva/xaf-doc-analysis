The code below saves the current application state:

[!include[<MySolution.Win/Controllers/MyController.cs>](~/templates/platform_specific_file_path.md)]

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.ExpressApp.Win;
// ...
public class MyController : ViewController { //or WindowController
// ...
    private void action_Execute(object sender, SimpleActionExecuteEventArgs e) {
        // Save Model settings in all opened windows in a WinForms application.
        foreach(Frame frame in ((WinShowViewStrategyBase)Application.ShowViewStrategy).Windows) {
            frame.SaveModel();
            // OR
            // frame.View.SaveModel();
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