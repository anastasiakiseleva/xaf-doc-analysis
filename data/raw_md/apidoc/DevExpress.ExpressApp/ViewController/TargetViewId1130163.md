---
uid: DevExpress.ExpressApp.ViewController.TargetViewId
name: TargetViewId
type: Property
summary: Specifies the identifier of the [View](xref:112611) for which the View Controller is activated, or a semicolon-separated list of identifiers if a View Controller targets multiple Views.
syntax:
  content: |-
    [DefaultValue("Any")]
    public string TargetViewId { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string value that is a View identifier or a semicolon-separated list of View identifiers.
seealso:
- linkId: DevExpress.ExpressApp.ViewController.TargetObjectType
- linkId: DevExpress.ExpressApp.ViewController.TargetViewNesting
- linkId: DevExpress.ExpressApp.ViewController.TargetViewType
- linkId: "113103"
---
By default, the **TargetViewId** property is set to "Any" (the [ActionBase.AnyCaption](xref:DevExpress.ExpressApp.Actions.ActionBase.AnyCaption) constant value) which means that the View Controller is activated for any View. You can specify the identifier of a View to enable View Controller activation for a specific View. You can also specify multiple target Views by separating their identifiers by a semicolon (;). The Controller will be activated for each listed View. The **TargetViewId** value is passed to the [Application Model](xref:112580)'s [IModelViewController.TargetViewId](xref:DevExpress.ExpressApp.Model.IModelViewController.TargetViewId) property.

The example below demonstrates how to add a @DevExpress.ExpressApp.Actions.SimpleAction to the *Department_ListView* [List View](xref:112611#list-view) only.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
// ...
public class AddSimpleActionController : ViewController {
    public AddSimpleActionController() {
        TargetViewId = "Department_ListView";
        SimpleAction departmentAction = new SimpleAction(this, "DepartmentAction", PredefinedCategory.Edit);
    }
}
```
***