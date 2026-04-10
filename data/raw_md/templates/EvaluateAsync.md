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
***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]