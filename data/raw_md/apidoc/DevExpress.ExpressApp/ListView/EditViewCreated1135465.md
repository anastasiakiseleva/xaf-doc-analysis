---
uid: DevExpress.ExpressApp.ListView.EditViewCreated
name: EditViewCreated
type: Event
summary: Occurs after the [ListView.EditView](xref:DevExpress.ExpressApp.ListView.EditView) has been created.
syntax:
  content: public event EventHandler<DetailViewCreatedEventArgs> EditViewCreated
seealso: []
---
Handle this event to access the [Detail View](xref:112611) displayed together with a [List View](xref:112611).

The following example demonstrates how to make the **Department** Detail View in **MasterDetailMode** read-only:

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp;
// ...
public class AllowNewViewController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        if(View.Model.MasterDetailMode == MasterDetailMode.ListViewAndDetailView) {
            if(View.EditView != null) {
                SetAllowEdit(View.EditView);
            }
            View.EditViewCreated += new EventHandler<DetailViewCreatedEventArgs>(AllowNewViewController_EditViewCreated);
        }
    }
    private void AllowNewViewController_EditViewCreated(object sender, DetailViewCreatedEventArgs e) {
        SetAllowEdit(e.View);
    }
    private void SetAllowEdit(DetailView editView) {
        editView.AllowEdit.SetItemValue("ByObjectType", View.ObjectTypeInfo.Type != typeof(Department));
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        View.EditViewCreated -= AllowNewViewController_EditViewCreated;
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports System
Imports DevExpress.ExpressApp
' ...
Public Class AllowNewViewController
    Inherits ViewController(Of ListView)

    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        If View.Model.MasterDetailMode = MasterDetailMode.ListViewAndDetailView Then
            If View.EditView IsNot Nothing Then
                SetAllowEdit(View.EditView)
            End If
            AddHandler View.EditViewCreated, AddressOf AllowNewViewController_EditViewCreated
        End If
    End Sub
    Private Sub AllowNewViewController_EditViewCreated(ByVal sender As Object, ByVal e As DetailViewCreatedEventArgs)
        SetAllowEdit(e.View)
    End Sub
    Private Sub SetAllowEdit(ByVal editView As DetailView)
        editView.AllowEdit.SetItemValue("ByObjectType", View.ObjectTypeInfo.Type IsNot GetType(Department))
    End Sub
    Protected Overrides Sub OnDeactivated()
        MyBase.OnDeactivated()
        RemoveHandler View.EditViewCreated, AddressOf AllowNewViewController_EditViewCreated
    End Sub
End Class
```

***