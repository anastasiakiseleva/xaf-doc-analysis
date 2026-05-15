---
uid: "113656"
seealso: []
title: 'How to: Disable an Action When the Current View Has Unsaved Changes'
---
# How to: Disable an Action When the Current View Has Unsaved Changes

This topic demonstrates how to disable an [Action](xref:112622) when business objects loaded to the current [Object Space](xref:113707) are changed. For this purpose, the [IObjectSpace.ModifiedChanged](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedChanged) event is handled, and the [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property is set based on the [IObjectSpace.IsModified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified) property.

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

As a result, the **Action1** is grayed out in the UI when there are unsaved changes in the current View. It is impossible to execute the Action until changes are saved to a data store (e.g., using the **Save** Action). When the changes are saved, the **Action1** reverts to its normal state.