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
***