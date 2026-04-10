The following code snippet enables automatic merge in XAF applications:

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

namespace MainDemo.Module.Controllers;

public class AutoMergeViewController : ViewController {
    private ProcessDataLockingInfoController lockController;

    private void OnDataLocking(object sender, DataLockingProcessingEventArgs e) {
        foreach (var info in e.DataLockingInfo.ObjectLockingInfo) {
            info.CanAutoMerge = info.CanMerge;
        }
    }

    protected override void OnActivated() {
        base.OnActivated();
        lockController = Frame.GetController<ProcessDataLockingInfoController>();
        lockController.DataLockingProcessing += OnDataLocking;
    }

    protected override void OnDeactivated() {
        base.OnDeactivated();
        if (lockController != null) {
            lockController.DataLockingProcessing -= OnDataLocking;
            lockController = null;
        }
    }
}
```