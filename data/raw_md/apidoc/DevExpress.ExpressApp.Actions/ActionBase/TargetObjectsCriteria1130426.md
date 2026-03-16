---
uid: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria
name: TargetObjectsCriteria
type: Property
summary: Specifies a logical expression (criteria) for enabling an [Action](xref:112622).
syntax:
  content: |-
    [DefaultValue(null)]
    public string TargetObjectsCriteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value representing a logical expression (criteria).
seealso:
- linkId: "113052"
- linkId: "113103"
---
This property allows defining for what objects an Action will be enabled or disabled. A disabled Action is visible in the UI, but it is grayed out and cannot be executed. Specify a logical expression built in accordance with the [Criteria Language Syntax](xref:4928) there, and the Action will be enabled only for objects that fit this expression. The Action should be added in a [View Controller](xref:112621) - Actions created in other Controller types are not affected by this property.

> [!NOTE]
> The **TargetObjectsCriteria** property has an effect only if the [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) property is set to **RequireSingleObject** or **RequireMultipleObjects**. The manner in which an Action's enabled state is calculated when several objects are selected is determined by the [ActionBase.TargetObjectsCriteriaMode](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteriaMode) property.

You can set the value of the **TargetObjectsCriteria** property in code, in the Controller's designer or in the [Model Editor](xref:112830). This value will be saved to the [IModelAction.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Model.IModelAction.TargetObjectsCriteria) property of the Application Model's [!include[Node_Action](~/templates/node_action111373.md)] node. The following image demonstrates how the **TargetObjectsCriteria** property is specified in the Model Editor:

![WaysToBuildCriteria](~/images/waystobuildcriteria116081.png)

This criteria expression uses the **LocalDateTimeToday** [function criteria operator](xref:113307). The following Controller demonstrates how to specify the **TargetObjectsCriteria** property in code. This Controller enables the Action when the selected **Task**'s **DueDate** property value is less than or equal to the system's date and time:

# [C#](#tab/tabid-csharp)

```csharp
public class MyController : ViewController {
    public MyController() {
        TargetObjectType = typeof(Task);
        SimpleAction myAction = new SimpleAction(this, "MyAction", DevExpress.Persistent.Base.PredefinedCategory.Unspecified);
        myAction.SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects;
        myAction.TargetObjectsCriteria = "DueDate <= LocalDateTimeToday()";
    }
}
```
***

The **TargetObjectsCriteria** property is appropriate for Actions displayed only for specific business object types. If an Action is displayed for a type that does not have properties specified in the **TargetObjectsCriteria** expression, an exception will be thrown. That is why if you wish to define the **TargetObjectsCriteria** for an Action that can be displayed for multiple types (e.g., for one of the built-in actions), do this dynamically in code when a View of the required type is displayed, and clear the passed value when this View is closed:

# [C#](#tab/tabid-csharp)

```csharp
public class MyController : ViewController {
    public MyController() {
        TargetObjectType = typeof(Department);
    }
    DeleteObjectsViewController deleteController;
    protected override void OnActivated() {
        base.OnActivated();
        deleteController = Frame.GetController<DeleteObjectsViewController>();
        if (deleteController != null) {
            deleteController.DeleteAction.TargetObjectsCriteria = "Contacts.Count = 0";
            deleteController.DeleteAction.TargetObjectsCriteriaMode = TargetObjectsCriteriaMode.TrueForAll;
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if (deleteController != null) {
            deleteController.DeleteAction.TargetObjectsCriteria = null;
            deleteController.DeleteAction.TargetObjectsCriteriaMode = default(TargetObjectsCriteriaMode);
            deleteController = null;
        }
    }
}
```
***