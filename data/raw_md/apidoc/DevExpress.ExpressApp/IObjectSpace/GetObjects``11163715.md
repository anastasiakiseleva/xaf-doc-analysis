---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjects``1(DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty},System.Boolean)
name: GetObjects<T>(CriteriaOperator, IList<SortProperty>, Boolean)
type: Method
summary: Returns a sorted **IList** collection of objects of the specified type, retrieved to the current Object Space and filtered according to the specified criteria.
syntax:
  content: IList<T> GetObjects<T>(CriteriaOperator criteria, IList<SortProperty> sorting, bool inTransaction)
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) which specifies the criteria for object selection.
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: An **IList\<**[](xref:DevExpress.Xpo.SortProperty)**>** object that specifies sorting.
  - id: inTransaction
    type: System.Boolean
    description: '**true**, if the filter takes unsaved changes into account; otherwise, **false**. Has effect in XPO only.'
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
The following example uses a [Parametrized Action](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) to search for a **Person** by **LastName**, and then assigns the deferred task with the nearest due date to that person.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections.Generic;
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
using DevExpress.Xpo.DB;
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
            List<SortProperty> sorting = new List<SortProperty>();
            sorting.Add(new SortProperty("DueDate", SortingDirection.Descending));
            CriteriaOperator taskCriteria = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred);
            IList<MainDemo.Module.BusinessObjects.DemoTask> tasks =
                    objectSpace.GetObjects<MainDemo.Module.BusinessObjects.DemoTask>(taskCriteria, sorting, false);
            if(tasks.Count > 0) {
                MainDemo.Module.BusinessObjects.DemoTask task = (MainDemo.Module.BusinessObjects.DemoTask)tasks[0];
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
Imports DevExpress.Xpo
Imports DevExpress.Xpo.DB

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
            Dim sorting As New List(Of SortProperty)()
            sorting.Add(New SortProperty("DueDate", SortingDirection.Descending))
            Dim taskCriteria As CriteriaOperator = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred)
            Dim tasks As IList(Of MainDemo.Module.BusinessObjects.DemoTask) = objectSpace.GetObjects( _
                Of MainDemo.Module.BusinessObjects.DemoTask)(taskCriteria, sorting, False)
            If tasks.Count > 0 Then
                Dim task As MainDemo.Module.BusinessObjects.DemoTask = _
                    CType(tasks(0), MainDemo.Module.BusinessObjects.DemoTask)
                task.AssignedTo = person
            End If
        End If
    End Sub
End Class

```

***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjects\<T>** method. It's implemented in the **BaseObjectSpace** class. To get the specified objects, the **BaseObjectSpace.GetObjects(Type type, CriteriaOperator criteria, bool inTransaction)** method invokes a protected virtual **CreateCollection** method that does nothing and returns null. So, you should override the **CreateCollection** method in your descendant.