The following code disables an [Action](xref:112622) when business objects in the current [Object Space](xref:113707) are changed.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using System;
// ...
public class ViewController1 : ViewController {
    SimpleAction action1;
    public ViewController1() {
        action1 = new SimpleAction(this, "Action1", DevExpress.Persistent.Base.PredefinedCategory.View);
    }
    protected override void OnActivated() {
        base.OnActivated();
        ObjectSpace.ModifiedChanged += ObjectSpace_ModifiedChanged;
        UpdateActionState();
    }
    void ObjectSpace_ModifiedChanged(object sender, EventArgs e) {
        UpdateActionState();
    }
    protected virtual void UpdateActionState() {
        action1.Enabled["ObjectSpaceIsModified"] = !ObjectSpace.IsModified;
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        ObjectSpace.ModifiedChanged -= ObjectSpace_ModifiedChanged;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports System
' ...
Public Class ViewController1
    Inherits ViewController

    Private action1 As SimpleAction
    Public Sub New()
        action1 = New SimpleAction(Me, "Action1", DevExpress.Persistent.Base.PredefinedCategory.View)
    End Sub
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        AddHandler ObjectSpace.ModifiedChanged, AddressOf ObjectSpace_ModifiedChanged
        UpdateActionState()
    End Sub
    Private Sub ObjectSpace_ModifiedChanged(ByVal sender As Object, ByVal e As EventArgs)
        UpdateActionState()
    End Sub
    Protected Overridable Sub UpdateActionState()
        action1.Enabled("ObjectSpaceIsModified") = Not ObjectSpace.IsModified
    End Sub
    Protected Overrides Sub OnDeactivated()
        MyBase.OnDeactivated()
        RemoveHandler ObjectSpace.ModifiedChanged, AddressOf ObjectSpace_ModifiedChanged
    End Sub
End Class
```

***