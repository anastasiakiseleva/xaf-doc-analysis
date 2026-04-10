The following Controller contains the Action that deletes completed tasks:

**File**: _MySolution.Module\Controllers\TaskViewController.cs_.
# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Data.Filtering;
using DevExpress.Persistent.Base.General;
using System.Collections.Generic;
// ...
public class TaskViewController : ObjectViewController<ListView, Task> {
    public TaskViewController() {
        SimpleAction deleteCompletedTasksAction = 
            new SimpleAction(this, "Delete completed tasks", PredefinedCategory.Edit);
        deleteCompletedTasksAction.Execute += DeleteCompletedTasksAction_Execute;
    }
    private void DeleteCompletedTasksAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        CriteriaOperator completedTasksCriteria = 
            CriteriaOperator.FromLambda<Task>(t => t.Status == TaskStatus.Completed);
        IList<Task> completedTasks = ObjectSpace.GetObjects<Task>(completedTasksCriteria);
        ObjectSpace.Delete(completedTasks);
        ObjectSpace.CommitChanges();
    }
}
```
***
