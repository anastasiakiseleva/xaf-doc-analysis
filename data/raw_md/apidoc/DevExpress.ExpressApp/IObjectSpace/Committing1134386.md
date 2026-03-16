---
uid: DevExpress.ExpressApp.IObjectSpace.Committing
name: Committing
type: Event
summary: Occurs before persistent objects are saved to the database.
syntax:
  content: event EventHandler<CancelEventArgs> Committing
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges
- linkId: DevExpress.ExpressApp.IObjectSpace.Committed
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaving
---
The [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method call raises the **Committing** event before the changes are stored in the database. In the **Committing** event handler, set the **CancelEventArgs.Cancel** parameter to **true** to prevent the commit. This parameter's default value is **false**.

[!include[<Committing>](~/templates/do-commit-remark.md)]

The following example prevents commits in the **Payment** [Detail View](xref:112611#detail-view):

# [C#](#tab/tabid-csharp)

```csharp{10-12}
using System.ComponentModel;
using DevExpress.ExpressApp;

// ...
public class CancelCommitController : ObjectViewController<DetailView, MainDemo.Module.BusinessObjects.Payment> {
    protected override void OnActivated() {
        base.OnActivated();
        View.ObjectSpace.Committing += ObjectSpace_Committing;
    }
    private void ObjectSpace_Committing(object sender, CancelEventArgs e) {
        e.Cancel = true;
    }
    protected override void OnDeactivated() {
        View.ObjectSpace.Committing -= ObjectSpace_Committing;
    }
}
```
***

[!include[<30-39><37-48>](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]

For another example, see the @DevExpress.ExpressApp.IObjectSpace.GetObjectsToDelete(System.Boolean) method description.
