---
uid: DevExpress.ExpressApp.IObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
name: FindObject(Type, CriteriaOperator, Boolean)
type: Method
summary: Searches for the first object that matches the specified criteria and is of the specified type.
syntax:
  content: object FindObject(Type objectType, CriteriaOperator criteria, bool inTransaction)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object which represents the type of objects to search for.
  - id: criteria
    type: DevExpress.Data.Filtering.CriteriaOperator
    description: A [](xref:DevExpress.Data.Filtering.CriteriaOperator) descendant which represents the criteria for matching persistent objects.
  - id: inTransaction
    type: System.Boolean
    description: '**true**, if the filter takes unsaved changes into account; otherwise, **false**.'
  return:
    type: System.Object
    description: An object which represents the first persistent object which matches the specified criteria. `null` if there is no persistent object which matches the criteria.
seealso:
- linkId: DevExpress.ExpressApp.EFCore.EFCoreObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
  altText: EFCoreObjectSpace.FindObject(Type,CriteriaOperator,Boolean)
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace.FindObject(System.Type,DevExpress.Data.Filtering.CriteriaOperator,System.Boolean)
  altText: XPObjectSpace.FindObject(Type,CriteriaOperator,Boolean)
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
        Person person = (Person)objectSpace.FindObject(typeof(Person), personCriteria, true);
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
***

When implementing the [](xref:DevExpress.ExpressApp.IObjectSpace) interface in the [](xref:DevExpress.ExpressApp.BaseObjectSpace) class' descendant, you should override the **FindObject(Type objectType, CriteriaOperator criteria, bool inTransaction)** method. All other **FindObject** method overloads call this method.
