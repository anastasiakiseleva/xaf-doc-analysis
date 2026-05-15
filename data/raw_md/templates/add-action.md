# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
// ...
public class CustomViewController : ViewController {
    public CustomViewController() {
        SimpleAction customAction = new SimpleAction(this, "CustomAction", PredefinedCategory.View);
        // or
        customAction.Category = PredefinedCategory.View.ToString();
        // or 
        customAction.Category = "View";
        // or 
        customAction.Category = "MyCustomCategory";
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
' ...
Public Class CustomViewController
    Inherits ViewController
    Public Sub New()
        Dim customAction As New SimpleAction(Me, "CustomAction", PredefinedCategory.View)
        ' or
        customAction.Category = PredefinedCategory.View.ToString()
        ' or 
        customAction.Category = "View"
        ' or 
        customAction.Category = "MyCustomCategory"
    End Sub
End Class
```

***
[`ViewController`]: xref:DevExpress.ExpressApp.ViewController
[`SimpleAction`]: xref:DevExpress.ExpressApp.Actions.SimpleAction
