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
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.EFCore
Imports DevExpress.Persistent.Base
' ...
Public Class AddDepartmentController
    Inherits ObjectViewController(Of DetailView, Contact)

    Public Sub New()
        Dim addDepartmentAction As New ParametrizedAction(Me, "AddDepartment", PredefinedCategory.Edit, GetType(String))
        AddHandler addDepartmentAction.Execute, AddressOf AddDepartmentAction_Execute
    End Sub
    Private Sub AddDepartmentAction_Execute(ByVal sender As Object, ByVal e As ParametrizedActionExecuteEventArgs)
        Using objectSpace As EFCoreObjectSpace = CType(Application.CreateObjectSpace(GetType(Department)), EFCoreObjectSpace)
            Dim department As Department = objectSpace.CreateObject(Of Department)()
            department.Title = TryCast(e.ParameterCurrentValue, String)
            objectSpace.CommitChanges()
        End Using
        View.Refresh()
    End Sub
End Class
```

***
