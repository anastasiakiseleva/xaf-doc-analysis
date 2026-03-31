---
uid: "112728"
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.Active
  altText: ActionBase.Active
- linkId: DevExpress.ExpressApp.Actions.ActionBase.Enabled
  altText: ActionBase.Enabled
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem.Active
  altText: ChoiceActionItem.Active
- linkId: DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled
  altText: ChoiceActionItem.Enabled
- linkId: DevExpress.ExpressApp.Controller.Active
  altText: Controller.Active
- linkId: "113103"
- linkId: "403709"
- linkId: "113141"
- linkId: "113142"
- linkId: "113484"
- linkId: "112676"
title: 'Hide or Disable an Action (Button, Menu Item) in Code'
---
# Hide or Disable an Action (Button, Menu Item) in Code
 
This topic describes how to hide or disable [Action](xref:112622) UI elements in code. You can also use other ways to hide/disable Actions that can be more suited to your scenario. See the following topic for details: [Ways to Hide or Disable an Action](xref:403709).

The image below shows examples of toolbar buttons you can remove or disable:

![|Hide (disable) an Action Button on the Toolbar](~/images/remove-action-button-from-toolbar.png)

The buttons in the image above are XAF [Actions](xref:112622). Each Action belongs to a [Controller](xref:112621). 

To customize Controllers in XAF applications, you can inherit Controllers or get their instances in other Controllers. For more information, refer to the following topic: [](xref:112676).

Follow the steps below to remove or disable an Action from another Controller:

1. Create a new Controller. Choose the Controller's base class type depending on the target scope: [](xref:113103).

1. Override the [Controller](xref:112621)'s `OnActivated` method.

1. Determine the target Action's Controller class name to manage the Action. For more information on how to find an Action's Controller, refer to the following topic: [](xref:113484).

1. Use the `Frame.GetController` method or the `Frame.Controllers` property to access the Action's Controller.

1. Use the `Actions` property of the Controller class (`YourController.Actions["YourActionId"]`) or built-in Controller properties (for example, `NewObjectViewController.NewObjectAction`) to access an Action.
    
    When `ActionAttribute` defines an Action, `ObjectMethodActionsViewController` generates the Action at runtime. XAF uses the following pattern to create the Action's ID:
`<short name of the container class> + <name of the method marked with ActionAttribute>` (for example, `Task.MarkCompleted`).

1. To remove an Action, call the @DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean) method of the Action's @DevExpress.ExpressApp.Actions.ActionBase.Active property and pass `False` as the second parameter.

    To disable an Action, call the @DevExpress.ExpressApp.Utils.BoolList.SetItemValue(System.String,System.Boolean) method of the Action's @DevExpress.ExpressApp.Actions.ActionBase.Enabled property and pass `False` as the second parameter.

The following Controller hides the **FullTextSearch** Action in the `Paycheck` List View:
 
```csharp{14-18,25-26}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

public class HideFullTextSearchController : ViewController {
    public HideFullTextSearchController() {
        TargetViewId = "Paycheck_ListView";
    }

    private FilterController filterController;
    const string deactivateReason = "HiddenInPaycheck";

    protected override void OnActivated() {
        base.OnActivated();
        filterController = Frame.GetController<FilterController>();
        if (filterController != null) {
            filterController.FullTextFilterAction.Active.SetItemValue(deactivateReason, false);
            // The line below disables the Action button
            // filterController.FullTextFilterAction.Enabled.SetItemValue(deactivateReason, false);
        }
    }
    
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if(filterController != null) {
            filterController.FullTextFilterAction.Active.RemoveItem(deactivateReason);
            filterController = null;
        }
    }
}
``` 

To undo these changes when the `Paycheck` List View is closed, the Controller removes its custom item from the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) list in the `OnDeactivated` method. This is necessary because XAF uses the same `FilterController` instance for every View of the current Window (Frame). For additional information, refer to the following topic: [](xref:112621).

Additional links that relate to this topic:

* The **Managing availability of Controllers and Actions** section of the following topic: [Best practices of creating reusable XAF modules by example of a View Variants module extension](https://community.devexpress.com/blogs/xaf/archive/2011/07/04/best-practices-of-creating-reusable-xaf-modules-by-example-of-a-view-variants-module-extension.aspx)

* [Determine Why an Action, Controller or Editor is Inactive](xref:112818)
