---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction
name: ShowNavigationItemAction
type: Property
summary: Allows access to the [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController)'s **ShowNavigationItem** Action.
syntax:
  content: public SingleChoiceAction ShowNavigationItemAction { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SingleChoiceAction
    description: A [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) object representing the **ShowNavigationItem** Action.
seealso: []
---
The **ShowNavigationItem** Action is intended to navigate between predefined Views. Its [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property is set to "ViewsNavigation".

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor ShowNavigationItem Action, DevExpress](~/images/xaf-blazor-navigation-action-devexpress.png)
Windows Forms
:   ![|XAF Windows Forms ShowNavigationItem Action, DevExpress](~/images/shownavigationitemaction_win115933.png)

As you can see in the images, there are child navigation items and first-level navigation items, where the child items are contained.

Navigation items are the elements of the **ShowNavigationItem** Action's `Items` collection (see [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items)). This collection has a tree-like structure. Typically, first-level collection items are navigation groups, and lower-level items are navigation items. The `Items` collection is generated using information from the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node. This node has **IModelNavigationItem** child nodes.

![ShowNavigationITemAction_NavigationItemsNode](~/images/shownavigationitemaction_navigationitemsnode115931.png)

The **NavigationItem** nodes have the [IModelNavigationItem.View](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem.View) property. This property should be set to the View that will be displayed when clicking the corresponding navigation item in the navigation control. To add a node to the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node, apply the [](xref:DevExpress.Persistent.Base.DefaultClassOptionsAttribute) or [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) to a business class. In addition, you can add a **NavigationItem** node manually, using the [Model Editor](xref:112582).

> [!NOTE]
> You can generate a new **NavigationItem** node in code, using the [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.SystemModule.NavigationItemNodeGenerator) node generator.

To modify the **ShowNavigationItem** Action's `Items` collection, use one of the following techniques:

* To generate this collection in a custom manner, handle the [ShowNavigationItemController.CustomInitializeItems](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomInitializeItems) event.
* To modify this collection after it has been populated, handle the [ShowNavigationItemController.ItemsInitialized](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ItemsInitialized) event.
* To modify the View to be shown when a user clicks a particular navigation item, override the **ShowNavigationItem** method in the `ShowNavigationItemController` descendant, or handle the [ShowNavigationItemController.CustomShowNavigationItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomShowNavigationItem) event.
* To disable or deactivate a particular item, use its [ChoiceActionItem.Enabled](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Enabled) and [ChoiceActionItem.Active](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Active) properties. To ascertain why an item is currently disabled or deactivated, use the [DiagnosticInfo](xref:112818) Action.

In SDI [UI Types](xref:DevExpress.ExpressApp.UIType), the **ShowNavigationItem** Action is automatically executed after the main Window has been loaded. The View shown corresponds to the navigation item returned by the [ShowNavigationItemController.GetStartupNavigationItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.GetStartupNavigationItem) method. The Action execution is performed by the  `WinShowStartupNavigationItemController` in Windows Forms applications and by `ProcessViewShortcutController` in Blazor applications.

You can organize a keyboard approach for navigating between the navigation control's items in Windows Forms applications. For this purpose, use the **NavigationItem** node's `Shortcut` property. Moreover, you can hide the navigation control and use keyboard shortcuts only. In addition, navigation items can be represented by images. For this purpose, set appropriate images for the [IModelBaseChoiceActionItem.ImageName](xref:DevExpress.ExpressApp.Model.IModelBaseChoiceActionItem.ImageName) property of the [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) node.

You can replace the navigation control that presents the **ShowNavigationItem** Action with another one. For instance, you can choose using a TreeList control. To learn how to do this, refer to the [Navigation System](xref:113198) topic. If you want to use another control, implement a custom [Action Container](xref:112610).

Information on the **ShowNavigationItem** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).