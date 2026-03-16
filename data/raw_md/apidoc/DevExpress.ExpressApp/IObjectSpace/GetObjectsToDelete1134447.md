---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectsToDelete(System.Boolean)
name: GetObjectsToDelete(Boolean)
type: Method
summary: Returns a collection of persistent objects that will be deleted when the current transaction is committed, including objects that will be deleted in the parent transaction(s), optionally.
syntax:
  content: ICollection GetObjectsToDelete(bool includeParent)
  parameters:
  - id: includeParent
    type: System.Boolean
    description: '**true**, to include persistent objects that will be deleted in the parent transaction(s); otherwise, **false**.'
  return:
    type: System.Collections.ICollection
    description: The collection of persistent objects that will be deleted when the current transaction is committed.
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.Committing
  altText: IObjectSpace.Committing event
---
When an object is deleted, it's not deleted from the database immediately. It's marked as an object to be deleted and removed from the database the next time the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method is called.

The `GetObjectsToDelete` method is intended to provide a collection of objects that are marked as deleted in the current transaction.

The code below demonstrates how you can use the `GetObjectsToDelete` method in your application:

```csharp{16}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Blazor;
using YourSolutionName.Module.BusinessObjects;
using System.ComponentModel;

namespace YourSolutionName.Module.Controllers;

public class HandleCommitController :ObjectViewController<DetailView, Contact> {
    protected override void OnActivated() {
        base.OnActivated();
        View.ObjectSpace.Committing += ObjectSpace_Committing;
    }

    private void ObjectSpace_Committing(object sender, CancelEventArgs e) {
        var os = (IObjectSpace)sender;
        var objectsToDelete = os.GetObjectsToDelete(includeParent: true);
        foreach(var item in objectsToDelete) {
            Contact deletedContact = item as Contact;
            if(deletedContact != null && deletedContact.FirstName == "NOT FOR DELETE") {
                e.Cancel = true;
                break;
            }
        }
    }

    protected override void OnDeactivated() {
        View.ObjectSpace.Committing -= ObjectSpace_Committing;
    }
}
```

In XPO applications with [Deferred Deletion](xref:2026) enabled, the `GetObjectsToDelete` method returns an empty collection. In such scenarios, use the @DevExpress.ExpressApp.IObjectSpace.GetObjectsToSave(System.Boolean) method instead.