---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjects``1(DevExpress.Data.Filtering.CriteriaOperator)
name: GetObjects<T>(CriteriaOperator)
type: Method
summary: Returns an **IList** collection of objects of the specified type, retrieved to the current Object Space and filtered according to the specified criteria.
syntax:
  content: IList<T> GetObjects<T>(CriteriaOperator criteria)
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) which specifies the criteria for object selection.
  typeParameters:
  - id: T
    description: The @System.Type of objects that are retrieved.
  return:
    type: System.Collections.Generic.IList{{T}}
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type. Only objects that satisfy the specified criteria will be retrieved to this collection.
seealso:
- linkId: "113707"
- linkId: "113711"
---
The following example uses a [Parametrized Action](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) to search for a **Person** by **LastName**, and then assigns all deferred tasks to that person.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.Generic;
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
using DevExpress.Persistent.BaseImpl;
// ...
public class AssignTasksController : ObjectViewController<ListView, MainDemo.Module.BusinessObjects.DemoTask> {
    public AssignTasksController() {
        ParametrizedAction assignTasksAction = new ParametrizedAction(
            this, "AssignTasks", PredefinedCategory.Edit, typeof(string));
        assignTasksAction.Execute += AssignTasksAction_Execute;
    }
    private void AssignTasksAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        IObjectSpace objectSpace = View.ObjectSpace;
        string personParamValue = e.ParameterCurrentValue as string;
        CriteriaOperator personCriteria = CriteriaOperator.Parse("Contains([LastName], ?)", personParamValue);
        Person person = (Person)objectSpace.FindObject(typeof(Person), personCriteria);
        if(person != null) {
            CriteriaOperator taskCriteria = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred);
            IList<MainDemo.Module.BusinessObjects.DemoTask> tasks =
                objectSpace.GetObjects<MainDemo.Module.BusinessObjects.DemoTask>(taskCriteria);
            foreach(MainDemo.Module.BusinessObjects.DemoTask task in tasks) {
                task.AssignedTo = person;
            }
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Collections.Generic
Imports DevExpress.Data.Filtering
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.Persistent.Base
Imports DevExpress.Persistent.Base.General
Imports DevExpress.Persistent.BaseImpl

Public Class AssignTasksController
    Inherits ObjectViewController(Of ListView, MainDemo.Module.BusinessObjects.DemoTask)
    Public Sub New()
        Dim assignTasksAction As New ParametrizedAction(Me, "AssignTasks", PredefinedCategory.Edit, GetType(String))
        AddHandler assignTasksAction.Execute, AddressOf AssignTasksAction_Execute
    End Sub
    Private Sub AssignTasksAction_Execute(ByVal sender As Object, ByVal e As ParametrizedActionExecuteEventArgs)
        Dim objectSpace As IObjectSpace = View.ObjectSpace
        Dim personParamValue As String = TryCast(e.ParameterCurrentValue, String)
        Dim personCriteria As CriteriaOperator = CriteriaOperator.Parse("Contains([LastName], ?)", personParamValue)
        Dim person As Person = CType(objectSpace.FindObject(GetType(Person), personCriteria), Person)
        If person IsNot Nothing Then
            Dim taskCriteria As CriteriaOperator = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred)
            Dim tasks As IList(Of MainDemo.Module.BusinessObjects.DemoTask) = _
                objectSpace.GetObjects(Of MainDemo.Module.BusinessObjects.DemoTask)(taskCriteria)
            For Each task As MainDemo.Module.BusinessObjects.DemoTask In tasks
                task.AssignedTo = person
            Next task
        End If
    End Sub
End Class
```

***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjects\<T>** method. It's implemented in the **BaseObjectSpace** class. To get the specified objects, the **BaseObjectSpace.GetObjects\<T>(CriteriaOperator criteria)** method invokes a generic protected virtual **CreateCollection** method that does nothing and returns null. So, you should override the generic **CreateCollection** method in your descendant.