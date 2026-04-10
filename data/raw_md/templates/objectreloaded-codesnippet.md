The following code snippet reloads the parent Detail View when one of the child objects is reloaded.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Module.Controllers {
    public class MyViewController : ObjectViewController<DetailView, Parent> {
        protected override void OnActivated() {
            base.OnActivated();
            ObjectSpace.ObjectReloaded += ObjectSpace_ObjectReloaded;
        }
        private void ObjectSpace_ObjectReloaded(object sender, ObjectManipulatingEventArgs e) {
            Child child = e.Object as Child;
            if (child != null && ReferenceEquals(child.Parent, View.CurrentObject)) {
                View.Refresh();
            }
        }
        protected override void OnDeactivated() {
            ObjectSpace.ObjectReloaded -= ObjectSpace_ObjectReloaded;
            base.OnDeactivated();
        }
    }
}
```
***