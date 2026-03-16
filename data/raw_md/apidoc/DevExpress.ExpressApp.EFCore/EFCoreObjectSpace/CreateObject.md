---
uid: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.CreateObject(System.Type)
name: CreateObject(Type)
type: Method
summary: Creates an object of the specified type.
syntax:
  content: public override object CreateObject(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: The type of the object to be created.
  return:
    type: System.Object
    description: A created object of the specified type.
seealso: []
---
This method calls the @DevExpress.ExpressApp.CompositeObjectSpace.CreateObject(System.Type) method and throws an exception if the specified type is not registered.

The following example shows how to use this method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.EFCore;
using DevExpress.Persistent.Base;
// ...
public class AddDepartmentController : ObjectViewController<DetailView, Contact> {
    public AddDepartmentController() {
        ParametrizedAction addDepartmentAction = new ParametrizedAction(
            this, "AddDepartment", PredefinedCategory.Edit, typeof(string));
        addDepartmentAction.Execute += AddDepartmentAction_Execute;
    }
    private void AddDepartmentAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        using (EFCoreObjectSpace objectSpace = (EFCoreObjectSpace)Application.CreateObjectSpace(typeof(Department))) {
            Department department = (Department)objectSpace.CreateObject(typeof(Department));
            department.Title = e.ParameterCurrentValue as string;
            objectSpace.CommitChanges();
        }
        View.Refresh();
    }
}
```
***
