---
uid: DevExpress.ExpressApp.View.ObjectSpace
name: ObjectSpace
type: Property
summary: Provides access to the object space within which a [](xref:DevExpress.ExpressApp.View) was created.
syntax:
  content: public virtual IObjectSpace ObjectSpace { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) object representing the current View's Object Space.
seealso: []
---
An Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)) represents an instrument that allows managing a cache with persistent objects that are currently used in a View. Via an Object Space, a particular objects set is retrieved from the database to a data set. This allows making changes to objects within this data set, and canceling changes. This does not influence the general database. Use this property to access the current View's Object Space.



> [!NOTE]
> Do not use a root View's Object Space for the creation of another root View in it. Instead, create a new Object Space via the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method for the new root View.

> [!NOTE]
> The **ObjectSpace** property is not supposed to be used in scenarios where a large amount of data is processed, created or deleted. Instead, use an independent Object Space which is not used by a View. Such an Object Space can be instantiated via the [XafApplication.CreateObjectSpace](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method.

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
using MainDemo.Module.BusinessObjects;
// ...
public class AssignTasksController : ObjectViewController<ListView, DemoTask> {
    public AssignTasksController() {
        ParametrizedAction assignTasksAction = new ParametrizedAction(
            this, "AssignTasks", PredefinedCategory.Edit, typeof(string));
        assignTasksAction.Execute += AssignTasksAction_Execute;
    }
    private void AssignTasksAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        IObjectSpace objectSpace = View.ObjectSpace;
        string personParamValue = e.ParameterCurrentValue as string;
        Person person = objectSpace.FirstOrDefault<Person>(p => p.LastName.Contains(personParamValue));
        if(person != null) {
            CriteriaOperator taskCriteria = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred);
            IList<DemoTask> tasks = objectSpace.GetObjects<DemoTask>(taskCriteria);
            foreach(DemoTask task in tasks) {
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
Imports MainDemo.Module.BusinessObjects

Public Class AssignTasksController
    Inherits ObjectViewController(Of ListView, DemoTask)
    Public Sub New()
        Dim assignTasksAction As New ParametrizedAction(Me, "AssignTasks", PredefinedCategory.Edit, GetType(String))
        AddHandler assignTasksAction.Execute, AddressOf AssignTasksAction_Execute
    End Sub
    Private Sub AssignTasksAction_Execute(ByVal sender As Object, ByVal e As ParametrizedActionExecuteEventArgs)
        Dim objectSpace As IObjectSpace = View.ObjectSpace
        Dim personParamValue As String = TryCast(e.ParameterCurrentValue, String)
        Dim person As Person = objectSpace.FirstOrDefault(Function (p as Person) p.LastName.Contains(personParamValue))
        If person IsNot Nothing Then
            Dim taskCriteria As CriteriaOperator = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred)
            Dim tasks As IList(Of DemoTask) = objectSpace.GetObjects(Of DemoTask)(taskCriteria)
            For Each task As DemoTask In tasks
                task.AssignedTo = person
            Next task
        End If
    End Sub
End Class

```

***