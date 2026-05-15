# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Actions;
// ...
public class MyViewController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        ObjectMethodActionsViewController controller = Frame.GetController<ObjectMethodActionsViewController>();
        if (controller != null) {
            SimpleAction markCompletedAction = controller.Actions["Task.MarkCompleted"] as SimpleAction;
            // ...
        }
        // ...
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.SystemModule
Imports DevExpress.ExpressApp.Actions
' ...
Public Class MyViewController
    Inherits ViewController
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        Dim controller As ObjectMethodActionsViewController = Frame.GetController(Of ObjectMethodActionsViewController)()
        If controller IsNot Nothing Then
            Dim markCompletedAction As SimpleAction = TryCast(controller.Actions("Task.MarkCompleted"), SimpleAction)
            ' ...
        End If
        ' ...
    End Sub
End Class
```

***