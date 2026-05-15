The following code demonstrates how to use this method in a View Controller to evaluate contact's assigned tasks.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Xpo;
using System;
using System.Threading;
// ...
public class AsyncTasksCountController : ObjectViewController<DetailView, Contact> {
    public AsyncTasksCountController() : base() {
        SimpleAction EvaluateTasksCountAction = new SimpleAction(this, "Assigned tasks count", "Edit");
        EvaluateTasksCountAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        EvaluateTasksCountAction.Execute += EvaluateTasksCountAction_Execute;
    }
    async private void EvaluateTasksCountAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        Guid currentContactOid = ViewCurrentObject.Oid;
        XPObjectSpace taskObjectSpace = (XPObjectSpace)Application.CreateObjectSpace(typeof(DemoTask));
        object tasksCount =
            await taskObjectSpace.EvaluateAsync(
            typeof(DemoTask), CriteriaOperator.Parse("Count()"),
            CriteriaOperator.Parse(string.Format("[AssignedTo.Oid] = '{0}'", currentContactOid)),
            cancellationTokenSource.Token);
        if (tasksCount != null) {
            ViewCurrentObject.AssignedTasksCount = (int)tasksCount;
        }
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Data.Filtering
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Xpo
Imports System
Imports System.Threading
' ...
Public Class AsyncTasksCountController
	Inherits ObjectViewController(Of DetailView, Contact)
	Public Sub New()
		MyBase.New()
		Dim EvaluateTasksCountAction As New SimpleAction(Me, "Assigned tasks count", "Edit")
		EvaluateTasksCountAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject
		AddHandler EvaluateTasksCountAction.Execute, AddressOf EvaluateTasksCountAction_Execute
	End Sub
	Async Private Sub EvaluateTasksCountAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
		Dim cancellationTokenSource As New CancellationTokenSource()
		Dim currentContactOid As Guid = ViewCurrentObject.Oid
		Dim taskObjectSpace As XPObjectSpace = CType(Application.CreateObjectSpace(GetType(DemoTask)), XPObjectSpace)
		Dim tasksCount As Object = Await taskObjectSpace.EvaluateAsync(GetType(DemoTask), _
            CriteriaOperator.Parse("Count()"), _
            CriteriaOperator.Parse(String.Format("[AssignedTo.Oid] = '{0}'", currentContactOid)), _
            cancellationTokenSource.Token)
		If tasksCount IsNot Nothing Then
			ViewCurrentObject.AssignedTasksCount = DirectCast(tasksCount, Integer)
		End If
	End Sub
End Class

```

***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]