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

# [VB.NET](#tab/tabid-vb)

```vb{<:1:>}
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base

Public Class AddDepartmentController
    Inherits ObjectViewController(Of DetailView, Contact)
    Public Sub New()
        Dim addDepartmentAction As New ParametrizedAction(
            Me, "AddDepartment", PredefinedCategory.Edit, GetType(String))
        AddHandler addDepartmentAction.Execute, AddressOf AddDepartmentAction_Execute
    End Sub
    Private Sub AddDepartmentAction_Execute(ByVal sender As Object, ByVal e As ParametrizedActionExecuteEventArgs)
        Dim department As Department = ObjectSpace.CreateObject(Of Department)()
        department.Title = TryCast(e.ParameterCurrentValue, String)
        Dim contact As Contact = CType(View.CurrentObject, Contact)
        contact.Departments.Add(department)
    End Sub
End Class

```

***