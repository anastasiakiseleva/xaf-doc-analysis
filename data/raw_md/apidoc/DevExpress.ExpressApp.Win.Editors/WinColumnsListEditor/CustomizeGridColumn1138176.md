---
uid: DevExpress.ExpressApp.Win.Editors.WinColumnsListEditor.CustomizeGridColumn
name: CustomizeGridColumn
type: Event
summary: Occurs when a column is created.
syntax:
  content: public event EventHandler<CustomizeGridColumnEventArgs> CustomizeGridColumn
seealso: []
---
Handle this event to customize column settings. Use the **e.GridColumn** parameter to access the column instance. The following example demonstrates the [Controller](xref:112621) that handles the **CustomizeGridColumn** event and makes the **FullName** column of the **Contact** object's List View [fixed](xref:3483).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Editors;
// ...
public class CustomizeGridColumnController : ObjectViewController<ListView, Contact> {
    protected override void OnActivated() {
        base.OnActivated();
        GridListEditor listEditor = ((ListView)View).Editor as GridListEditor;
        if (listEditor != null) {
            listEditor.CustomizeGridColumn += listEditor_CustomizeGridColumn;
        }
    }
    void listEditor_CustomizeGridColumn(object sender, CustomizeGridColumnEventArgs e) {
        if (e.GridColumn.FieldName == "FullName") {
            e.GridColumn.Fixed = DevExpress.XtraGrid.Columns.FixedStyle.Left;
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Win.Editors
' ...
Public Class CustomizeGridColumnController
    Inherits ObjectViewController(Of ListView, Contact)
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        Dim listEditor As GridListEditor = TryCast(CType(View, ListView).Editor, GridListEditor)
        If listEditor IsNot Nothing Then
            AddHandler listEditor.CustomizeGridColumn, AddressOf listEditor_CustomizeGridColumn
        End If
    End Sub
    Private Sub listEditor_CustomizeGridColumn(ByVal sender As Object, ByVal e As CustomizeGridColumnEventArgs)
        If e.GridColumn.FieldName = "FullName" Then
            e.GridColumn.Fixed = DevExpress.XtraGrid.Columns.FixedStyle.Left
        End If
    End Sub
End Class
```

***

> [!IMPORTANT]
> Subscribe to **CustomizeGridColumn** in the overridden **OnActivated** method. Do not use the **OnViewControlsCreated** method for this purpose - columns are already initialized at that moment and the event will not be triggered.