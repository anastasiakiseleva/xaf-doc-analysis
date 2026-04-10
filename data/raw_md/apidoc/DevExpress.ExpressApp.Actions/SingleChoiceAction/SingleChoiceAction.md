---
uid: DevExpress.ExpressApp.Actions.SingleChoiceAction
name: SingleChoiceAction
type: Class
summary: A class that implements a Single Choice Action.
syntax:
  content: 'public class SingleChoiceAction : ChoiceActionBase'
seealso:
- linkId: DevExpress.ExpressApp.Actions.SingleChoiceAction._members
  altText: SingleChoiceAction Members
---
The `SingleChoiceAction` class inherits both the basic functionality of [Actions](xref:112622) from the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class, and the functionality of Choice Actions - from the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase) class. 

Single Choice Actions are used to execute custom code when a user selects an item from the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection. You can populate this collection at design time via the **Properties** window. Select the **Items** property and click the ellipsis button provided for it. In the invoked **ChoiceActionItems Collection Editor**, add items and specify their settings.

Each item within the [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection can contain child items as well. So, you can form a tree of items for a Single Choice Action.

![|Action Option Selection in XAF ASP.NET Core Blazor List View, DevExpress](~/images/btutorial_ef_lesson5_3listview.png)

You can specify the type of a Single Choice Action's items: they can represent either modes or operations. To do this, use the [SingleChoiceAction.ItemType](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.ItemType) property.

### Add a Single Choice Action

You can add a  Single Choice Action to a [Controller](xref:112621) as described in the following topic: [](xref:402159).

[!include[coderush-templates-actions-controllers](~/templates/coderush-templates-actions-controllers.md)]

### Run Custom Code in Single Choice Actions

To provide custom code to be executed when users select a single item within the Items collection, handle the [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event. To access the selected item, use the handler's [SingleChoiceActionExecuteEventArgs.SelectedChoiceActionItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceActionExecuteEventArgs.SelectedChoiceActionItem) parameter.

## Example

The following code snippet implements a single choice action that allows users to filter a current list view.

The single choice action's items (of the _Department_ type) are retrieved from a data source. When a single choice action item is selected, the current list view displays employees assigned to the selected department.

# [C#](#tab/tabid-csharp)
 
```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using MainDemo.Module.BusinessObjects;

namespace MainDemo.Module {
    public class DepartmentFilterController : ObjectViewController<ListView, Employee> {
        SingleChoiceAction departmentFilterAction;
        public DepartmentFilterController() {
            departmentFilterAction = new SingleChoiceAction(this, "DepartmentFilter", "Filters");
            departmentFilterAction.Caption = "Department";
            departmentFilterAction.Execute += departmentFilterAction_Execute;
        }
        protected override void OnActivated() {
            base.OnActivated();
            departmentFilterAction.Items.Clear();
            foreach (Department department in ObjectSpace.GetObjects<Department>()) {
                departmentFilterAction.Items.Add(new ChoiceActionItem(department.Title, department.Oid));
            }
        }
        void departmentFilterAction_Execute(object sender, SingleChoiceActionExecuteEventArgs e) {
            View.CollectionSource.Criteria["DepartmentFilter"] = new BinaryOperator("Department.Oid", e.SelectedChoiceActionItem.Data);
        }
    }
}
```
***