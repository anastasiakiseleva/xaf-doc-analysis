---
uid: DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)
name: CreateObject(Type)
type: Method
summary: Creates an object of the specified type.
syntax:
  content: object CreateObject(Type type)
  parameters:
  - id: type
    type: System.Type
    description: A [](xref:System.Type) object which is the type of the object to be created.
  return:
    type: System.Object
    description: An object that represents the created object of the specified type.
seealso:
- linkId: "113711"
---
The following example uses a [Parametrized Action](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) to create a new **Department** object and refresh the [Detail View](xref:112611#detail-view). The new department becomes available in the **Contact.Department** [Lookup List View](xref:112611#list-view).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MainDemo.Module.BusinessObjects;
// ...
public class AddDepartmentController : ObjectViewController<DetailView, Contact> {
    public AddDepartmentController() {
        ParametrizedAction addDepartmentAction = new ParametrizedAction(
            this, "AddDepartment", PredefinedCategory.Edit, typeof(string));
        addDepartmentAction.Execute += AddDepartmentAction_Execute;
    }
    private void AddDepartmentAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        using(IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Department))) {
            Department department = objectSpace.CreateObject<Department>();
            department.Title = e.ParameterCurrentValue as string;
            objectSpace.CommitChanges();
        }
        View.Refresh();
    }
}
```
***

If you implement the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you don't have to override the **CreateObject** method entirely. The [BaseObjectSpace.CreateObject](xref:DevExpress.ExpressApp.BaseObjectSpace.CreateObject(System.Type)) method invokes a protected virtual **BaseObjectSpace.CreateObjectCore** method and then sets the returned object modified by calling the [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method for it. So, you should only override the **CreateObjectCore** method.

The created object will be saved to the database when calling the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method.