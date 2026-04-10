The following code snippet adds the cloned object to the current List View instead of displaying it in the Detail View. Note that the code only works when the current View is an [editable List View](xref:113249). The default behavior persists when the current View is a Detail View or non-editable List View.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.CloneObject;
using DevExpress.Persistent.BaseImpl.EF;
using Microsoft.EntityFrameworkCore.Metadata;

namespace YourApplicationName.Module.Controllers;

public class MyCloneObjectController : CloneObjectViewController  {
    // ...
    protected override void OnActivated() {
        base.OnActivated();
        this.CustomShowClonedObject +=
            new EventHandler<CustomShowClonedObjectEventArgs>(
                MyCloneObjectController_CustomShowClonedObject);
    }
    private void MyCloneObjectController_CustomShowClonedObject(
        object sender, CustomShowClonedObjectEventArgs e) {
        if ((View is ListView) && (View.AllowEdit.ResultValue)) {
            e.TargetObjectSpace.CommitChanges();
            ((ListView)View).CollectionSource.Add(ObjectSpace.GetObject(e.ClonedObject));
            e.Handled = true;
        }
    }
}
```
***