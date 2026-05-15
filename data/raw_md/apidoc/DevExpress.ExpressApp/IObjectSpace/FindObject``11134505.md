---
uid: DevExpress.ExpressApp.IObjectSpace.FindObject``1(DevExpress.Data.Filtering.CriteriaOperator)
name: FindObject<ObjectType>(CriteriaOperator)
type: Method
summary: Searches for the first object that matches the specified criteria. The object's type is designated by the specified generic type parameter. The search takes uncommitted changes into account.
syntax:
  content: ObjectType FindObject<ObjectType>(CriteriaOperator criteria)
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) descendant which is the criteria for matching persistent objects.
  typeParameters:
  - id: ObjectType
    description: The @System.Type of objects that are retrieved.
  return:
    type: '{ObjectType}'
    description: An object which is the first persistent object which matches the specified criteria.
seealso:
- linkId: "113711"
---
The following example uses a [Parametrized Action](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) to search for a **Person** by **LastName**, and then assigns all deferred tasks to that person.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections;
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
        Person person = objectSpace.FindObject<Person>(personCriteria);
        if(person != null) {
            CriteriaOperator taskCriteria = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred);
            IList tasks = objectSpace.GetObjects(
                typeof(MainDemo.Module.BusinessObjects.DemoTask), taskCriteria);
            foreach(MainDemo.Module.BusinessObjects.DemoTask task in tasks) {
                task.AssignedTo = person;
            }
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports System.Collections
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
        Dim person As Person = objectSpace.FindObject(Of Person)(personCriteria)
        If person IsNot Nothing Then
            Dim taskCriteria As CriteriaOperator = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred)
            Dim tasks As IList = objectSpace.GetObjects( _
                GetType(MainDemo.Module.BusinessObjects.DemoTask), taskCriteria)
            For Each task As MainDemo.Module.BusinessObjects.DemoTask In tasks
                task.AssignedTo = person
            Next task
        End If
    End Sub
End Class
```

***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, you don't have to implement the **FindObject\<ObjectType>** method. The **BaseObjectSpace** class' **FintObject\<ObjectType>(CriteriaOperator criteria)** method invokes a public virtual **FindObject(Type objectType, CriteriaOperator criteria, Boolean inTransaction)** method passing **true** as the _inTransaction_ parameter. So, to implement an object search, override the public virtual **BaseObjectSpace.FindObject** method.