The following code shows how to manually save child collection changes made in the parent Detail View:

```csharp{<:0:>}
using DevExpress.ExpressApp;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using YourSolutionName.Module.BusinessObjects;

namespace YourSolutionName.Module.Controllers {
    public class MyViewController : ObjectViewController<DetailView, Parent> {
        List<Child> detailObjectsCache = new List<Child>();
        protected override void OnActivated() {
            base.OnActivated();
            ObjectSpace.CustomCommitChanges += ObjectSpace_CustomCommitChanges;
            ObjectSpace.Committing += ObjectSpace_Committing;
            ObjectSpace.Committed += ObjectSpace_Committed;
            ObjectSpace.Reloaded += ObjectSpace_Reloaded;
        }
        protected override void OnDeactivated() {
            ObjectSpace.CustomCommitChanges -= ObjectSpace_CustomCommitChanges;
            ObjectSpace.Committing -= ObjectSpace_Committing;
            ObjectSpace.Committed -= ObjectSpace_Committed;
            ObjectSpace.Reloaded -= ObjectSpace_Reloaded;
            base.OnDeactivated();
        }
        void ObjectSpace_Reloaded(object sender, EventArgs e) {
            detailObjectsCache.Clear();
        }
        void ObjectSpace_Committed(object sender, EventArgs e) {
            detailObjectsCache.Clear();
        }
        void ObjectSpace_Committing(object sender, CancelEventArgs e) {
            IObjectSpace os = (IObjectSpace)sender;
            for (int i = os.ModifiedObjects.Count - 1; i >= 0; i--) {
                object item = os.ModifiedObjects[i];
                if (typeof(Child).IsAssignableFrom(item.GetType())) {
                    detailObjectsCache.Add(item as Child);
                    os.RemoveFromModifiedObjects(item);
                }
            }
        }
        void ObjectSpace_CustomCommitChanges(object sender, HandledEventArgs e) {
            // Implement custom logic to save Detail objects here. 
            foreach (Child detailObject in detailObjectsCache) {
                //...  
            }
        }
    }
}
```