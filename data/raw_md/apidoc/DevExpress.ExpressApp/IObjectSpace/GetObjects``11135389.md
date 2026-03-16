---
uid: DevExpress.ExpressApp.IObjectSpace.GetObjects``1(DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: GetObjects<T>(CriteriaOperator, Boolean)
type: Method
summary: Returns an **IList** collection of objects via the current Object Space.
syntax:
  content: IList<T> GetObjects<T>(CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) which specifies the criteria for object selection.
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
                objectSpace.GetObjects<MainDemo.Module.BusinessObjects.DemoTask>(taskCriteria, false);
            foreach(MainDemo.Module.BusinessObjects.DemoTask task in tasks) {
                task.AssignedTo = person;
            }
        }
    }
}
```
***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class's descendant, don't implement the **GetObjects\<T>** method. It's implemented in the **BaseObjectSpace** class. To get the specified objects, the **BaseObjectSpace.GetObjects\<T>(CriteriaOperator criteria, bool inTransaction)** method invokes a generic protected virtual **CreateCollection** method that does nothing and returns null. So, you should override the generic **CreateCollection** method in your descendant.