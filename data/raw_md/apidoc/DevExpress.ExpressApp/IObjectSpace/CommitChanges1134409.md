---
uid: DevExpress.ExpressApp.IObjectSpace.CommitChanges
name: CommitChanges()
type: Method
summary: Saves all the changes made to the persistent objects belonging to the current Object Space to the database.
syntax:
  content: void CommitChanges()
seealso:
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaving
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectSaved
- linkId: DevExpress.ExpressApp.IObjectSpace.ObjectChanged
- linkId: DevExpress.ExpressApp.IObjectSpace.Delete*
---
When working with persistent objects, the changes that you make are not saved immediately. Each object change is tracked. To save all the tracked changes, the **CommitChanges** method is called. After calling this method, the track list is emptied and the [IObjectSpace.IsModified](xref:DevExpress.ExpressApp.IObjectSpace.IsModified) property is set to **false**.

In default scenarios, this method is automatically called. But all custom manipulations that you perform with persistent objects must be saved manually via this method.

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, override the **DoCommit** method. It is invoked by the [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges) method, in which the following events raised:

* [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing)
    
    Raised before committing the changes. It is intended to prevent the commit performed by the **CommitChanges** method.
* [IObjectSpace.CustomCommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges)
    
    Raised before committing the changes. It is intended to perform a custom commit instead of a default one.
* [IObjectSpace.Committed](xref:DevExpress.ExpressApp.IObjectSpace.Committed)
    
    Raised after committing the changes. It is intended to perform post actions after the commit.

In the **DoCommit** method, force saving changes using a container for in-memory objects (see [UnitOfWork.CommitChanges](xref:DevExpress.Xpo.UnitOfWork.CommitChanges) in XPO).

> [!NOTE]
> An Object Space object commits only the objects that were created with its help. Otherwise, an exception is raised.

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
public class AssignTasksController : ViewController {
    public AssignTasksController() {
        TargetObjectType = typeof(DemoTask);
        ParametrizedAction assignTasksAction = new ParametrizedAction(
            this, "AssignTasks", PredefinedCategory.Edit, typeof(string));
        assignTasksAction.Execute += AssignTasksAction_Execute;
    }
    private void AssignTasksAction_Execute(object sender, ParametrizedActionExecuteEventArgs e) {
        using(IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person))) {
            string personParamValue = e.ParameterCurrentValue as string;
            Person person = objectSpace.FirstOrDefault<Person>(p => p.LastName.Contains(personParamValue));
            if(person != null) {
                CriteriaOperator taskCriteria = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred);
                IList<DemoTask> tasks = objectSpace.GetObjects<DemoTask>(taskCriteria);
                foreach(DemoTask task in tasks) {
                    task.AssignedTo = person;
                }
                objectSpace.CommitChanges();
            }
        }
        View.Refresh(true);
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
    Inherits ViewController
    Public Sub New()
        TargetObjectType = GetType(DemoTask)
        Dim assignTasksAction As New ParametrizedAction(Me, "AssignTasks", PredefinedCategory.Edit, GetType(String))
        AddHandler assignTasksAction.Execute, AddressOf AssignTasksAction_Execute
    End Sub
    Private Sub AssignTasksAction_Execute(ByVal sender As Object, ByVal e As ParametrizedActionExecuteEventArgs)
        Using objectSpace As IObjectSpace = Application.CreateObjectSpace(GetType(Person))
            Dim personParamValue As String = TryCast(e.ParameterCurrentValue, String)
            Dim person As Person = objectSpace.FirstOrDefault(Function (p as Person) p.LastName.Contains(personParamValue))
            If person IsNot Nothing Then
                Dim taskCriteria As CriteriaOperator = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred)
                Dim tasks As IList(Of DemoTask) = objectSpace.GetObjects(Of DemoTask)(taskCriteria)
                For Each task As DemoTask In tasks
                    task.AssignedTo = person
                Next task
                objectSpace.CommitChanges()
            End If
        End Using
        View.Refresh(True)
    End Sub
End Class

```
***