---
uid: DevExpress.ExpressApp.Win.Editors.GridListEditor.AppearanceFocusedCellMode
name: AppearanceFocusedCellMode
type: Property
summary: Specifies whether the appearance settings for the focused cell are enabled.
syntax:
  content: public AppearanceFocusedCellMode AppearanceFocusedCellMode { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.Editors.AppearanceFocusedCellMode
    description: An [](xref:DevExpress.ExpressApp.Win.Editors.AppearanceFocusedCellMode) enumeration value specifying whether the appearance settings for the focused cell are enabled.
seealso:
- linkId: DevExpress.XtraGrid.Views.Grid.GridOptionsSelection.EnableAppearanceFocusedCell
---
The following code snippet demonstrates how to disable appearance settings for the focused cell in view mode for all [List Views](xref:112611) that use **GridListEditor**.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
//...
public class MyController : ViewController<ListView> {
    protected override void OnViewControlsCreated() {
        base.OnViewControlsCreated();
        GridListEditor gridEditor = View.Editor as GridListEditor;
        if (gridEditor != null) {
            gridEditor.AppearanceFocusedCellMode = AppearanceFocusedCellMode.Disabled;
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Win.Editors
'...
Public Class MyController
    Inherits ViewController(Of ListView)
    Protected Overrides Sub OnViewControlsCreated()
        MyBase.OnViewControlsCreated()
        Dim gridEditor As GridListEditor = TryCast(View.Editor, GridListEditor)
        If gridEditor IsNot Nothing Then
            gridEditor.AppearanceFocusedCellMode = AppearanceFocusedCellMode.Disabled
        End If
    End Sub
End Class
```

***