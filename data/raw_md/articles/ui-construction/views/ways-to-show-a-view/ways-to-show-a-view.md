---
uid: "112803"
seealso:
- linkId: "113664"
- linkId: "113708"
- linkId: "112623"
- linkId: "112916"
title: Ways to Show a View
owner: Ekaterina Kiseleva
---
# Ways to Show a View

Typically, [Views](xref:112611) are displayed in response to user input, for example, when a menu item is clicked. This topic lists ways to create and show a View.

## Show a View from the Navigation Control
The [navigation system](xref:113198) is visualized by the navigation control, which lists all available Views and allows you to activate the required View. The navigation structure defines the Views order and hierarchy.

### Add a View to the Navigation Control in Code

The simplest way to add a List View to the navigation is to apply the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) to the [business class](xref:113664). As a result, XAF adds a new navigation item to the `Default` group.

# [C#](#tab/tabid-csharp)

```csharp
[DefaultClassOptions]
public class Contact {
    //...
}
```
***

You can also use the [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) for the same purpose. The difference is that this attribute allows you to specify the navigation group, while the `DefaultClassOptions` attribute always adds an item to the **Default** group.

# [C#](#tab/tabid-csharp)

```csharp
[NavigationItem("Management")]
public class TestPerson : BaseObject {
    //...
}
```
***

You can use `DefaultClassOptions` and `NavigationItem` attributes to show List Views only. The next section explains how to show other View types.

### Add a View to the Navigation Control in the Designer

You can use the [Model Editor](xref:112582) to add a List View, Detail View, or Dashboard View to the navigation. The **NavigationItems** node defines the tree-like structure of navigation items using [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) child nodes. Create a new **NavigationItem** node within the existing hierarchy and set the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) property to the target List View to show this View from navigation.

![Tutorial_EF_Lesson4_4](~/images/tutorial_ef_lesson4_4115464.png)

To show a Detail View from navigation, you should additionally specify the [IModelNavigationItem.ObjectKey](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.ObjectKey) property value.

A complete example is available in the [Add an Item to the Navigation Control](xref:402131) tutorial.

## Show a View Using an Action
You can show a specific View when a user clicks a custom [Action](xref:112622). Technically, the navigation system is also an Action (see [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction)). When you show a View from navigation, this View is created automatically. However, when you use a custom Action, you will require one of the following methods to create a View object.

* [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*) - to create a [](xref:DevExpress.ExpressApp.ListView).
* [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*) - to create a [](xref:DevExpress.ExpressApp.DetailView).
* [XafApplication.CreateDashboardView](xref:DevExpress.ExpressApp.XafApplication.CreateDashboardView(DevExpress.ExpressApp.IObjectSpace,System.String,System.Boolean)) - to create a [](xref:DevExpress.ExpressApp.DashboardView).

The View can be shown before an Action execution (for example, to collect user input required to proceed), and after the execution (for example, to display certain resulting data).

### Show a View Before an Action's Execute Event Occurs

If you are required to show a View before an Action is executed, use the [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) Action. In this Action type, the [PopupWindowShowAction.CustomizePopupWindowParams](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.CustomizePopupWindowParams) event is triggered first. Then, the pop-up window is displayed. Finally, the [PopupWindowShowAction.Execute](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction.Execute) event is raised when the **OK** button is clicked in the pop-up. You can handle the `CustomizePopupWindowParams` event to create and configure the displayed View.

# [C#](#tab/tabid-csharp)

```csharp
private void popupWindowShowAction1_CustomizePopupWindowParams(
    object sender, CustomizePopupWindowParamsEventArgs e) {
    e.View = Application.CreateListView(typeof(Note), true);
}
```
***

The complete example for the List View is available in the following topic: [](xref:402158). For an example of how to create and show a Detail View, refer to the [How to: Create and Show a Detail View of the Selected Object in a Popup Window](xref:118760) topic.

### Show a View After an Action is Executed

In this case, you can use one of the following Action types.

* [](xref:DevExpress.ExpressApp.Actions.SimpleAction)
* [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction)
* [](xref:DevExpress.ExpressApp.Actions.ParametrizedAction)

Handle the Action's `Execute` event, access the [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) argument and pass the View to the [ShowViewParameters.CreatedView](xref:DevExpress.ExpressApp.ShowViewParameters.CreatedView) property.

# [C#](#tab/tabid-csharp)

```csharp
private void simpleAction1_Execute(object sender, SimpleActionExecuteEventArgs e) {
    IObjectSpace objectSpace = Application.CreateObjectSpace(typeof(Person));
    e.ShowViewParameters.CreatedView = Application.CreateListView(objectSpace, typeof(Person), true);
}
```
***

The [](xref:DevExpress.ExpressApp.ShowViewParameters) object also allows you to configure other parameters of the displayed View, such as the target window type, template type, and associated Controllers. For example, you can specify that the View passed to the [ShowViewParameters.CreatedView](xref:DevExpress.ExpressApp.ShowViewParameters.CreatedView) property should be shown in a pop-up window. Refer to the **ShowViewParameters** class description for additional information.

If you want to display a simple text notification on Action execution, use the [ShowViewStrategyBase.ShowMessage](xref:DevExpress.ExpressApp.ShowViewStrategyBase.ShowMessage*) method.

> [!NOTE]
> The **PopupWindowShowAction** also passes the [ShowViewParameters.CreatedView](xref:DevExpress.ExpressApp.ShowViewParameters.CreatedView) parameter to its `Execute` event handler. A View passed to this property will be shown when the **DialogOK** Action is executed in the pop-up window.

To learn more about using these Actions, refer to the following topics:
- [](xref:402159)
- [](xref:402155)

## Show a View from a Custom Context
The most convenient and recommended way to show a View is to use an Action. However, in certain rare scenarios, you may be required to show a View that is not associated with any Action. In this instance, create a View using the [XafApplication.CreateListView](xref:DevExpress.ExpressApp.XafApplication.CreateListView*), [XafApplication.CreateDetailView](xref:DevExpress.ExpressApp.XafApplication.CreateDetailView*), or [XafApplication.CreateDashboardView](xref:DevExpress.ExpressApp.XafApplication.CreateDashboardView(DevExpress.ExpressApp.IObjectSpace,System.String,System.Boolean)) method. Then, you can pass the created View object to one of the following methods.

* [Frame.SetView](xref:DevExpress.ExpressApp.Frame.SetView*) - to show the View within the current [Frame](xref:112608).
* [ShowViewStrategyBase.ShowViewInPopupWindow](xref:DevExpress.ExpressApp.ShowViewStrategyBase.ShowViewInPopupWindow(DevExpress.ExpressApp.View,System.Action,System.Action,System.String,System.String,DevExpress.ExpressApp.Frame,System.Action{DevExpress.ExpressApp.ShowViewParameters})) - to show the View in a pop-up dialog with **OK** and **Cancel** buttons.
* ShowViewStrategyBase.ShowViewFromCommonView - to show the View when you click a navigation item or a List View row. In [SDI](xref:DevExpress.ExpressApp.UIType.SingleWindowSDI) mode, XAF displays the View in the same Frame. Otherwise, XAF opens a new tab or window.

## Non-Persistent View Specifics
Views of [non-persistent](xref:116516) objects can be shown using the same techniques. However, you should manually supply data for these views before showing them. See the following topics to view examples:

* [How to: Display a List of Non-Persistent Objects in a Popup Dialog](xref:113167)
* [How to: Display a Non-Persistent Object's Detail View from the Navigation](xref:113471)
* [How to: Display a Non-Persistent Object's List View from the Navigation](xref:114052)

## Show a Custom non-XAF Form
You can design a custom form or user control in Visual Studio and add it to your XAF application. In most cases, you can create a [Controller](xref:112621) and show the form on an [Action](xref:112622)'s `Execute` event.

For more information, refer to the following help topics:
* [How to: Show a Custom Windows Form](xref:118222)
* [How to: Show a Custom Window with an Embedded XAF View](xref:118165)
* [How to: Show a Custom Data-Bound Control in an XAF View (WinForms)](xref:114159)
* [](xref:113610)
* [Ways to Show a Confirmation Dialog](xref:118240)
