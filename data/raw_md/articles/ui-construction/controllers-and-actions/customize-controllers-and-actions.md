---
uid: "112676"
seealso:
- linkId: "113484"
- linkId: "113016"
title: Customize Controllers and Actions
---
# Customize Controllers and Actions

To implement a new feature in the **XAF**, create a new [Controller](xref:112621). If the feature requires end-user interaction, add [Actions](xref:112622) to it. At the same time, you may need to customize a Controller or Action provided by the **XAF** or a third party. Most of [built-in Controllers](xref:113016) expose events you can handle to add your custom code.
Another approach is to inherit from the existing Controller and override its virtual methods. In some situations, it is easier and more effective to handle the Controller's events or the Action's events. In this topic, we will detail the situations in which each of these approaches to customize the provided features is more appropriate.

## Access Controller's Events and Properties
This approach to customizing a particular feature is more appropriate if several additional independent customizations of an Action's behavior or a Controller's behavior are required. For instance, two modules declare business objects that demand additional initialization when they are created via the **New** Action. In this instance, both of these modules should extend the **New** Action behavior independently. In this case, handling events is more appropriate than inheriting from a Controller.

> [!NOTE]
> In specific situations, you may need to handle a chain of events, rather than a single event.

You can access any [built-in Controller](xref:113016) from your custom Controller using the [Frame.GetController\<ControllerType>](xref:DevExpress.ExpressApp.Frame.GetController``1) method.

The following code demonstrates how to remove the Person item from the **New** Action's items list, to prohibit end-users from creating Person objects. A new Controller is created for this purpose.  In its **OnActivated** method, the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) is accessed to subscribe to its [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) event. This event is fired when generating the **New** Action's items list. In the **CollectDescendantTypes** event handler, the **Person** item is removed from this list. The **OnDectivated** method unsubscribes the **CollectDescendantTypes** event.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
using DevExpress.Persistent.BaseImpl;
// ...
public class CustomizeNewActionWindowController : ViewController {
    protected override void OnActivated(){
        base.OnActivated();
        NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
        if (controller != null) {
            controller.CollectDescendantTypes += NewObjectViewController_CollectDescendantTypes;
        }
    }
    private void NewObjectViewController_CollectDescendantTypes(
        object sender, CollectTypesEventArgs e) {
        foreach (Type type in e.Types) {
            if (type.Name == nameof(Person)) { e.Types.Remove(type); break; }
        }
    }
    protected override void OnDeactivated() {
        NewObjectViewController controller = Frame.GetController<NewObjectViewController>();
        if (controller != null) {
            controller.CollectDescendantTypes -= NewObjectViewController_CollectDescendantTypes;
        }
        base.OnDeactivated();
    }
}
```
***

## Inherit From a Controller
When building an **XAF** application, you may face the following task: a Controller provides a useful feature, but you need to slightly customize it. This customization does not depend on any conditions, so you will not need to modify the customizations in another module. In this instance, the best technique is to inherit from the required Controller and override its virtual methods. You may need to customize a particular Action as well. In this instance, since Actions are contained in Controllers, you will also need to inherit from the Action's Controller and override its virtual methods.

All of the Controllers that do not have descendants are instantiated for a [](xref:DevExpress.ExpressApp.Frame). Also, since a descendant Controller inherits the base Controller's Actions, it generally does not make sense to create several descendants of a Controller within modules that might be used together in an **XAF** application. In this situation, all of these descendants will be instantiated, and there will be several copies of the base Controller's Actions available. This situation causes an exception because Actions must have unique IDs. Thus, it is better to create only one descendant of the base Controller and perform all the customizations in it. If required, however, you can have several descendant Controllers, but in this instance you will need to manually disable inherited Actions in the Controllers' code.

> [!IMPORTANT]
> * Take a special note on selecting an appropriate built-in Controller type when creating its descendant. In most cases, creating a descendant of a built-in Controller requires selecting the last descendant in the inheritance chain. For example, if a Controller has WinForms or ASP.NET Core Blazor-specific descendants (such as the [](xref:DevExpress.ExpressApp.Win.SystemModule.WinModificationsController) or [](xref:DevExpress.ExpressApp.Blazor.SystemModule.BlazorModificationsController) descendants of the [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) class), it is necessary to create their descendants rather than a descendant of the parent class. Otherwise, both the built-in Controller and your descendant will be activated, and duplicate Actions will be displayed, as mentioned above.
> 	
> 	However, remember that [](xref:DevExpress.ExpressApp.ViewController) and [](xref:DevExpress.ExpressApp.WindowController) are basic Controllers. They do not provide any particular features and are designed for developing new Controllers. Therefore, you can inherit from these parent Controllers to create new Controllers in your UI-specific module projects. If your solution does not contain these projects, add a Controller to an [application project](xref:118045). Your newly implemented items will not conflict with any other of **ViewController**’s and **WindowController**'s children.
> * Do not change the [ViewController.TargetObjectType](xref:DevExpress.ExpressApp.ViewController.TargetObjectType), [ViewController.TargetViewType](xref:DevExpress.ExpressApp.ViewController.TargetViewType), [ViewController.TargetViewId](xref:DevExpress.ExpressApp.ViewController.TargetViewId) or [ViewController.TargetViewNesting](xref:DevExpress.ExpressApp.ViewController.TargetViewNesting) property values when inheriting a built-in Controller. Otherwise, you will lose the functionality of the inherited Controller in other Views that do not match the conditions specified by these properties.

When inheriting from a Controller, the [Application Model](xref:112580) will contain information on both the base and inherited Controllers. In the **ActionDesign** | **Controllers** node, the new Controller will contain Actions declared in it. The inherited Actions will be displayed under the base Controller's node.

<!--TODO: can we provide a similar example for Blazor here? -->