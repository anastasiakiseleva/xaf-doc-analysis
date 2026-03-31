---
uid: "113103"
seealso:
- linkId: "112908"
- linkId: "112728"
- linkId: "403709"
- linkId: "402155"
- linkId: "402157"
- linkId: "402158"
- linkId: "402159"
- linkId: "402154"
- linkId: "112612#access-and-customize-view-items-in-code"
title: Define the Scope of Controllers and Actions
---
# Define the Scope of Controllers and Actions

This topic describes how to set conditions for activating Controllers and their Actions.

## Specify the Scope of Controllers

### Activate or Deactivate a Controller

If you implement a [Controller](xref:112621) that executes code in the [Controller.Activated](xref:DevExpress.ExpressApp.Controller.Activated) event handler or in the `OnActivated` and `OnViewControlsCreated` methods, you may have to define the conditions when this code is executed. For example, you may need to define that a Controller that customized a Grid Editor should be active for List Views only. To do this, change the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property's value directly or use one of Controller's properties listed in this topic.

The `Controller.Active` property also affects the visibility of all Actions declared in this Controller (if a Controller is inactive, all of its Actions are also inactive). To hide a single Action, you can use the [](xref:DevExpress.ExpressApp.Actions.ActionBase) class's properties (see [Change the Scope of Actions](#change-the-scope-of-actions)).

The following members help you specify the required conditions for Controller activation:

| Member | Description |
|---|---|
| [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) | Provides access to a collection of reason/value pairs used to activate or deactivate a Controller or determine its active state. The Controller is active when all items in this collection have the `true` value. You can add an item with a value that contains a conditional expression, so the Controller is deactivated when this expression returns `false`. |
| [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) | Specifies the type of objects a View should display to activate a View Controller. |
| [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId) | Specifies the ID of the targeted View where a Controller should be active. |
| [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType) | Specifies the type of the targeted View where a Controller should be active. |
| [ViewController.TargetViewNesting](xref:DevExpress.ExpressApp.ViewController.TargetViewNesting) | Specifies whether the targeted View where a Controller should be active is root, nested, or any. |
| [WindowController.TargetWindowType](xref:DevExpress.ExpressApp.WindowController.TargetWindowType) | Specifies the kind of the Window where a Window Controller should activate. |

### Activate a Controller for Particular Views and Objects

You can inherit your Controller from [](xref:DevExpress.ExpressApp.ViewController`1) or [](xref:DevExpress.ExpressApp.ObjectViewController`2) and use the generic parameters to control views and types where a View Controller should become active.
The example below demonstrates how to activate a Controller only for the `Person` Detail View.

# [C#](#tab/tabid-csharp)

```csharp
public class ViewController1 : ObjectViewController<DetailView, Person> {
    protected override void OnActivated() {
        base.OnActivated();
        Person person = this.ViewCurrentObject;
        DetailView detailView = this.View;
        // ....
    }
}
```
***

> [!NOTE]
> The [ObjectViewController`2.ViewCurrentObject](xref:DevExpress.ExpressApp.ObjectViewController`2.ViewCurrentObject) and [ObjectViewController`2.View](xref:DevExpress.ExpressApp.ObjectViewController`2.View) property types change depending on types passed as generic parameters. This may be useful when you want to avoid casting the View Controller's View to [](xref:DevExpress.ExpressApp.ListView) or [](xref:DevExpress.ExpressApp.DetailView). The Visual Studio Designer does not work for Controllers inherited from generic types.

## Change the Scope of Actions

When you implement an [Action](xref:112622), you may want to display it in a particular form. For example, your application should display a **CancelAppointment** Action only in the Views of an `Appointment` object. You may deactivate either the Action's Controller or the Action itself.

### Deactivate an Action's Controller

In most cases, you can turn off (deactivate) a [Controller](xref:112621) that declares an Action to hide this Action. If you deactivate a Controller, all its Actions become invisible. Refer to the [Specify the Scope of Controllers](#specify-the-scope-of-controllers) section to learn how to do this.

### Deactivate an Action Itself

You can also define target [Views](xref:112611) and [Windows](xref:112608) for each Action individually. To do this, use the following properties:

| Member | Description |
|---|---|
| [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) | Provides access to a collection of key/value pairs that determine or change the Action's active state. The resulting state determines the Action's visibility. |
| [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) | Provides access to a collection of key/value pairs that determine an Action's enabled/disabled state. A disabled Action is grayed out in the UI and a user cannot execute it. |
| [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) | Specifies a criteria to enable an Action. |
| [ActionBase.TargetObjectsCriteriaMode](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteriaMode) | Specifies whether all the currently selected objects meet the `TargetObjectsCriteria` criteria to enable an Action. |
| [ActionBase.TargetObjectType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectType) | Specifies the type of the object(s) that the current View should display to activate an Action. |
| [ActionBase.TargetViewId](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewId) | Specifies the ID of the targeted View where an Action should be active. |
| [ActionBase.TargetViewNesting](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewNesting) | Specifies whether the View where an Action should be active is root, nested, or any. |
| [ActionBase.TargetViewType](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetViewType) | Specifies the type of the targeted View where an Action should be active. |
| [ActionBase.SelectionDependencyType](xref:DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType) | Specifies a context to enable an Action. |

These properties control whether an Action is visible in certain Views and Windows. Refer to the [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) topic to learn other ways to control visibility state (for example, hide an Action depending on a Business Object's property value).

## Activate a Controller or Action for Multiple Business Objects or Views

To make a single `ViewController` or `Action` available in Views of different Business Object types simultaneously, consider one of the following solutions:

- Set the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType) property in code to an interface or their base class type that is implemented or inherited by all these business types respectively.
- Specify several View identifiers (separated by semicolon `;`) in the [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId) property.
- Manage the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) or [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) properties manually depending on required conditions.

## Examples of Controller Scope Configuration

The following controller activates in nested `Paycheck` List Views:

```csharp
using DevExpress.ExpressApp;

public class ViewController1 : ViewController {
    public ViewController1() {
        TargetObjectType = typeof(Paycheck);
        TargetViewType = ViewType.ListView;
        TargetViewNesting = Nesting.Nested;
    }
}

// Alternatively, you can write the controller above as:
public class ViewControllerAlternative : ObjectViewController<ListView, Paycheck> {
    public ViewControllerAlternative() {
        TargetViewNesting = Nesting.Nested;
    }
}
```

The next controller activates in Root Views for a set of Business Object types:

```csharp
using DevExpress.ExpressApp;

public class ViewController1 : ViewController {
    public ViewController1() {
        TargetViewNesting = Nesting.Root;
    }
    protected override void OnViewChanged() {
        base.OnViewChanged();
        var viewObjectType = View?.ObjectTypeInfo?.Type;
        Active["Only for Employee and Paycheck objects"] =
            viewObjectType == typeof(Employee) || viewObjectType == typeof(Paycheck);
    }
}
```

You can add multiple activation criteria of arbitrary complexity:

```csharp
using DevExpress.ExpressApp;

public class ViewController1 : ViewController {
    protected override void OnViewChanged() {
        base.OnViewChanged();
        if(View is null)
            return;
        Active["Only for nested views"] = !View.IsRoot;
        Active["Not for lookup list views"] =
            Frame.Context != TemplateContext.LookupControl && Frame.Context != TemplateContext.LookupWindow;
        Active["Not for inline edit or split views"] = !(View is ListView listView && (listView.AllowEdit || listView.Model.MasterDetailMode == MasterDetailMode.ListViewAndDetailView));
        Active["Only for specific types"] = CanActivateForType(View.ObjectTypeInfo?.Type);
        Active["Active in specific views only"] = CanActivateForViewId(View.Id);
    }
    private bool CanActivateForType(Type businessObjectType) { /*...*/ }
    private bool CanActivateForViewId(string viewId) { /*...*/ }
}
```

## Examples of Action Scope Configuration

To define Action scope, you can use simple static rules or dynamic rules based on the properties of the selected objects. The following example demonstrates an Action that can deactivate users. This Action is enabled if the following conditions are met:

- The current View is a root View for `ApplicationUser`.
- At least one of the selected objects in a List View or the current object in a Detail View must be an active user (`CriteriaOperator.FromLambda<ApplicationUser>(user => user.IsActive).ToString()`).
- The selection cannot include Administrator users.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Data.Filtering;

public class DeactivateUsersController : ViewController {
    SimpleAction deactivateUserAction;
    public DeactivateUsersController() {
        deactivateUserAction = new SimpleAction(this, "DeactivateUser", DevExpress.Persistent.Base.PredefinedCategory.Edit) {
            SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects,
            TargetObjectsCriteria = CriteriaOperator.FromLambda<ApplicationUser>(user => user.IsActive).ToString(),
            TargetObjectsCriteriaMode = TargetObjectsCriteriaMode.TrueAtLeastForOne,
            TargetViewNesting = Nesting.Root,
            TargetObjectType = typeof(ApplicationUser),
            TargetViewType = ViewType.Any,
        };
        deactivateUserAction.Execute += DeactivateUserAction_Execute;
    }
    private void UpdateActionState() {
        // Update action visibility dynamically based on the currently selected objects
        var selectedUsers = deactivateUserAction.SelectionContext?.SelectedObjects?.OfType<ApplicationUser>()
            ?? Array.Empty<ApplicationUser>();
        bool adminUsersSelected = selectedUsers.Any(user => user.Roles.Any(role => role.IsAdministrative));
        deactivateUserAction.Enabled["Cannot deactivate Administrator users"] = !adminUsersSelected;
    }


    private void DeactivateUserAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        var selectedUsers = deactivateUserAction.SelectionContext?.SelectedObjects?.OfType<ApplicationUser>()
            ?? Array.Empty<ApplicationUser>();
        foreach (var user in selectedUsers) {
            user.IsActive = false;
        }
        ObjectSpace.CommitChanges();
    }
    protected override void OnActivated() {
        base.OnActivated();
        UpdateActionState();
        View.CurrentObjectChanged += View_CurrentObjectChanged;
        if (View is ListView listView) {
            listView.SelectionChanged += ListView_SelectionChanged;
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if (View is not null) {
            View.CurrentObjectChanged -= View_CurrentObjectChanged;
            if (View is ListView listView) {
                listView.SelectionChanged -= ListView_SelectionChanged;
            }
        }
    }
    private void ListView_SelectionChanged(object sender, EventArgs e) => UpdateActionState();
    private void View_CurrentObjectChanged(object sender, EventArgs e) => UpdateActionState();
}
```

> [!TIP]
> For more information on how to determine a user's permissions, refer to the following topic: [](xref:403824).