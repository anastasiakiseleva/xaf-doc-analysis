---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
name: GetObjectsCount(Type, CriteriaOperator)
type: Method
summary: Returns the number of objects specified.
syntax:
  content: int GetObjectsCount(Type objectType, CriteriaOperator criteria)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that identifies the type of objects against which the calculation will be performed.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: The [](xref:DevExpress.Data.Filtering.CriteriaOperator) that specifies the criteria for object selection in the database.
  return:
    type: System.Int32
    description: An integer value that is the count of persistent objects that satisfy the specified criteria.
seealso:
- linkId: DevExpress.ExpressApp.BaseObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
---
This method is intended to calculate the number of persistent objects in the database. For instance, this method is used before retrieving objects for the Lookup Property Editor. If there are more than the specified value, the Find editor is available.

The following code limits the number of objects that are created with the New Action:

# [C#](#tab/tabid-csharp)

```csharp{16}
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp.SystemModule;
//...
public class LimitTaskAmountController : ViewController {
    private NewObjectViewController controller;
    protected override void OnActivated() {
        base.OnActivated();
        controller = Frame.GetController<NewObjectViewController>();
        if (controller != null) {
            controller.ObjectCreating += controller_ObjectCreating;
        }
    }
    void controller_ObjectCreating(object sender, ObjectCreatingEventArgs e) {
        if ((e.ObjectType == typeof(Task)) && 
            (e.ObjectSpace.GetObjectsCount(typeof(Task), null) >= 3)) {
                e.Cancel = true;
                throw new UserFriendlyException(
                    "Cannot create a task. Maximum allowed task count is exceeded.");
        }
    }
    protected override void OnDeactivated() {
        if (controller != null) {
            controller.ObjectCreating -= controller_ObjectCreating;
        }
        base.OnDeactivated();
    }
}
```
***
