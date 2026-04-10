The following code snippet uses a [Parametrized Action](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) to create a new `Department` object and add it to the `Departments` collection of the current `Contact` object.

# [C#](#tab/tabid-csharp)

```csharp{<:0:>}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
// ...
public class AddDepartmentController : ObjectViewController<DetailView, Contact> {
    public AddDepartmentController() {
        ParametrizedAction addDepartmentAction = new ParametrizedAction(this, "AddDepartment", PredefinedCategory.Edit, typeof(string));
        addDepartmentAction.Execute += AddDepartmentAction_Execute;
    }
    private void AddDepartmentAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        Department department = ObjectSpace.CreateObject<Department>();
        department.Title = e.ParameterCurrentValue as string;
        Contact contact = (Contact)View.CurrentObject;
        contact.Departments.Add(department);
    }
}
```
***