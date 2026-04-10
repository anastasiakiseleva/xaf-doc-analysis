The Controller below specifies the `IsMarkedAsDeleted` property of `CustomDeleteObjectsEventArgs.Objects` instead of removing them:

**File**: _MySolution.Module\Controllers\CustomDeleteObjectController.cs_.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
// ...
public class CustomDeleteObjectController : ObjectViewController<DetailView, Employee> {
    protected override void OnActivated() {
        base.OnActivated();
        ObjectSpace.CustomDeleteObjects += ObjectSpace_CustomDeleteObjects;
    }
    private void ObjectSpace_CustomDeleteObjects(object sender, CustomDeleteObjectsEventArgs e) {
        foreach (object deletingObject in e.Objects) {
            Employee employee = ObjectSpace.GetObject(deletingObject) as Employee;
            // IsMarkedAsDeleted is a custom Employee's property
            employee.IsMarkedAsDeleted = true;
        }
        e.Handled = true;
    }
    protected override void OnDeactivated() {
        ObjectSpace.CustomDeleteObjects -= ObjectSpace_CustomDeleteObjects;
        base.OnDeactivated();
    }
}
```
***

> [!NOTE]
> This event is raised only when you use @DevExpress.ExpressApp.IObjectSpace methods to delete objects.  
> 
> EF Core and XPO have similar functionality out of the box:
> * [XPO: Deferred and Immediate Object Deletion](xref:2026).
> * [EF Core: Soft Deletion](xref:405259)