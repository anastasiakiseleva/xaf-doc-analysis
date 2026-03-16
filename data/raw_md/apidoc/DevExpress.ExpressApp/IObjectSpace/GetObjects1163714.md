---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjects(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Collections.Generic.IList{DevExpress.Xpo.SortProperty},System.Boolean)
name: GetObjects(Type, CriteriaOperator, IList<SortProperty>, Boolean)
type: Method
summary: Returns a sorted **IList** collection of objects of the specified type, retrieved to the current Object Space and filtered according to the specified criteria.
syntax:
  content: IList GetObjects(Type type, CriteriaOperator criteria, IList<SortProperty> sorting, bool inTransaction)
  parameters:
  - id: type
    type: System.Type
    description: The type of objects that are retrieved.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) which specifies the criteria for object selection.
  - id: sorting
    type: System.Collections.Generic.IList{DevExpress.Xpo.SortProperty}
    description: An **IList\<**[](xref:DevExpress.Xpo.SortProperty)**>** object that specifies sorting.
  - id: inTransaction
    type: System.Boolean
    description: '**true**, if the filter takes unsaved changes into account; otherwise, **false**. Has effect in XPO only.'
  return:
    type: System.Collections.IList
    description: A [](xref:System.Collections.IList) collection that contains the persistent objects of the specified type. Only objects that satisfy the specified criteria will be retrieved to this collection.
seealso:
- linkId: "113707"
- linkId: "113711"
---
The following example uses a [Parametrized Action](xref:DevExpress.ExpressApp.Actions.ParametrizedAction) to search for a **Person** by **LastName**, and then assigns the deferred task with the nearest due date to that person.

# [C#](#tab/tabid-csharp)

```csharp
using System.Collections;
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
        Person person = objectSpace.FirstOrDefault<Person>(p => p.LastName.Contains(personParamValue));
        if(person != null) {
            List<SortProperty> sorting = new List<SortProperty>();
            sorting.Add(new SortProperty("DueDate", SortingDirection.Descending));
            CriteriaOperator taskCriteria = CriteriaOperator.Parse("[Status] = ?", TaskStatus.Deferred);
            IList tasks = objectSpace.GetObjects(
                typeof(MainDemo.Module.BusinessObjects.DemoTask), taskCriteria, sorting, false);
            if(tasks.Count > 0) {
                MainDemo.Module.BusinessObjects.DemoTask task = (MainDemo.Module.BusinessObjects.DemoTask)tasks[0];
                task.AssignedTo = person;
            }
        }
    }
}
```
***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjects** method. It's implemented in the **BaseObjectSpace** class. To get the specified objects, the **BaseObjectSpace.GetObjects(Type type, CriteriaOperator criteria, bool inTransaction)** method invokes a protected virtual **CreateCollection** method that does nothing and returns null. So, you should override the **CreateCollection** method in your descendant.

