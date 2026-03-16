---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction
name: NewObjectAction
type: Property
summary: Stores settings for the **New** Action.
syntax:
  content: public SingleChoiceAction NewObjectAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) object that is the **New** Action.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectActionItemListMode
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/t326296/how-to-remove-or-hide-the-base-class-from-the-new-action-s-items-list
  altText: How to remove or hide the base class from the New Action's items list
---
The **New** Action allows users to create new objects of one of the predefined types.

### Contents of the Items collection

Available object types come from the Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection.

A Controller populates the `Items` collection in the `UpdateActionState` method. The following platform-specific controllers (`NewObjectViewController` descendants) override this method in slightly different ways: `WinNewObjectViewController` and `BlazorNewObjectViewController`. This means that you can expect different sets of objects available in the New Action on different platforms.

In general, the following objects can be elements in the `Items` collection:

* The current [View](xref:112611)'s object type (see [ObjectView.ObjectTypeInfo](xref:DevExpress.ExpressApp.ObjectView.ObjectTypeInfo)) and its descendants.

  Use the [NewObjectActionItemListMode](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectActionItemListMode) property to further specify which objects from this group populate the `Items` list.

* The types from the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) node. XAF automatically populates this node with business classes that use the [](xref:DevExpress.Persistent.Base.CreatableItemAttribute) or [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute). You can also add a class to this node in the [Model Editor](xref:112582).

In a Windows Forms application, the Controller populates the **New** Action's `Items` collection with all of the types above.

![|WinNewObjectViewController_New|](~/images/winnewobjectviewcontroller_new115926.png)

In an ASP.NET Core Blazor application, the Controller populates the **New** Action's `Items` collection only with the objects of the current [View](xref:112611)'s object type and its descendants.

![BlazorNewObjectViewController_NewAction](~/images/blazornewobjectviewcontroller_newaction.png)

Information on the **New** and **Quick create** Actions is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).

### Modification of the Items collection

You can modify the `Items` collection of the **New** Action by using one of the following techniques:

| Controller / Class | Handle Event / Override Method | Details |
| --- | --- | --- |
| `NewObjectViewController` or its descendants | [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) event | Fires when XAF extends the list with the current View's object type and its descendants. |
| `NewObjectViewController` | [NewObjectViewController.CollectCreatableItemTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectCreatableItemTypes) event | Fires when XAF adds types listed in the **CreatableItems** node. |
| Descendant(s) of `WinNewObjectViewController` or `BlazorNewObjectViewController` | `NewObjectViewController.UpdateActionState` method | XAF calls this method after it populates the collection with the types listed above. |

### Visibility

The **New** Action is active (visible) under the following conditions:

* The current View is root (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)) or the current View is the "Many" part of the One-to-Many relationship.
* The [IModelView.AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew) property returns `true`.
* The `Items` collection contains at least one active item.

An item can be missing in the `Items` collection if the Session-specific constructor is missing in the XPO class. An item can be invisible if the applied [Security System](xref:113366) prohibits creating objects of the corresponding type.

[!include[new-action-hidden-in-many-to-many-collection](~/templates/new-action-hidden-in-many-to-many-collection.md)]

To see why the **New** Action is not active, use the [DiagnosticInfo](xref:112818) Action. If you need to change the Action's "active" or "enabled" state in code, use its [ActionBase.Active](xref:DevExpress.ExpressApp.Actions.ActionBase.Active) or [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) properties.

### UI Control: Standard Button or Dropdown List

The application can display the `NewObjectAction` as a standard button or a drop-down control. The type of the control depends on the value of the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick) property and the contents of the Action's `Items` collection.

If you set the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick) property to `true`, the application always renders the Action as a drop-down control. You can execute the required action only from the drop-down.

If you set the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick) property to `false`, the application takes into account the contents of the `Items` collection and renders the Action as:

* A default button (if the collection contains a single active item)
* A drop-down control (if the collection contains several active items)

You can change the value of the [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.ShowItemsOnClick) property in the [Model Editor](xref:112582). Go to the **ActionDesign | Actions | New** node and edit the `ShowItemsOnClick` property in the **Behavior** section.

### Example

You can access and modify the **New** Action in code. For example, the code below accesses the `NewObjectAction` and adds it to the [Quick Access Toolbar](xref:2496):

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;

// ...
public class NewObjectActionController : WindowController {
    protected override void OnActivated() {
        base.OnActivated();
        NewObjectViewController newObjectViewController = Window.GetController<NewObjectViewController>();
        if(newObjectViewController != null) {
            newObjectViewController.NewObjectAction.QuickAccess = true;
        }
    }
}
```
***

