---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController
name: ShowNavigationItemController
type: Class
summary: A [](xref:DevExpress.ExpressApp.WindowController) descendant that contains the **ShowNavigationItem** [Action](xref:112622).
syntax:
  content: 'public class ShowNavigationItemController : WindowController, IModelExtender, IShowViewParametersCustomizer'
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController._members
  altText: ShowNavigationItemController Members
- linkId: "112920"
- linkId: "113198"
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/XAF-How-to-show-the-number-of-list-view-items-in-the-navigation-control
  altText: How to show the number of List View items in the Navigation Control
---
The **`ShowNavigationItemController`** is a part of the [Navigation System](xref:113198). This Controller displays the **ShowNavigationItem** Action.
ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor ShowNavigationItem Action, DevExpress](~/images/xaf-blazor-navigation-action-devexpress.png)
Windows Forms
:   ![|XAF Windows Forms ShowNavigationItem Action, DevExpress](~/images/shownavigationitemaction_win115933.png)

For details on the **ShowNavigationItem** Action, refer to the following topic: [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction).

To customize the default behavior of the **ShowNavigationItem** Action, you can inherit from this Controller or subscribe to its events. In addition, you can access the Action to modify its behavior.

If you need to inherit from the `ShowNavigationItemController`, the following protected virtual methods are available for overriding:

{|
|-

! Method
! When is it called?
! Description
|-

| `HasRights`
| Invoked as a result of calling the `InitializeItems` method when populating the **Navigation**'s Items collection.
| Determines whether the application's [Security System](xref:113366) grants permission to read the object(s) of the passed item's View. If a **Views** | **View** node describing the item's View cannot be found, this method returns `true`. The items for which this method returns `false`, are disabled by the [ShowNavigationItemController.SynchronizeItemsWithSecurity](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.SynchronizeItemsWithSecurity) method.
|-

| `InitializeItems`
| Called after the **ShowNavigationItemController** is activated.
| * Raises the [ShowNavigationItemController.CustomInitializeItems](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomInitializeItems) event.
* Creates [](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem) objects and initializes them using information from the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems) node. Marks the ChoiceActionItem as a start-up item if the corresponding **NavigationItem** node is set for the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node's [IModelRootNavigationItems.StartupNavigationItem](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.StartupNavigationItem) property.
* Invokes the `OnItemsInitialized` method to raise the [ShowNavigationItemController.ItemsInitialized](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ItemsInitialized) event.
* Calls the [ShowNavigationItemController.GetStartupNavigationItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.GetStartupNavigationItem) method to mark one of the **ShowNavigationItem** Action's items as a start-up item, if none of the items are marked as yet.
* Sets the **ShowNavigationItem** Action's [SingleChoiceAction.SelectedItem](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.SelectedItem) property to the item that is marked as a start-up item. This item will be selected when the navigation control is shown for the first time.
|-

| `OnItemsInitialized`
| Called after the **ShowNavigationItem** Action's Items collection is populated via the `InitializeItems` method.
| Raises the [ShowNavigationItemController.ItemsInitialized](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ItemsInitialized) event.
|-

| `ShowNavigationItem`
| Called by the **ShowNavigationItem** Action's [SingleChoiceAction.Execute](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction.Execute) event handler.
| * Raises the [ShowNavigationItemController.CustomShowNavigationItem](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.CustomShowNavigationItem) event.
* Creates a View using information of the passed Item's [ChoiceActionItem.Data](xref:DevExpress.ExpressApp.Actions.ChoiceActionItem.Data) property cast as [](xref:DevExpress.ExpressApp.ViewShortcut) if the `Handled` parameter of the `CustomShowNavigationItem` event handler is not set to `false`.
|}

Public members are described individually in the documentation.

To ascertain whether the Controller is active, use the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) property (see [How to: Detect a Lookup List View in Code](xref:112908)). If you need to know the reason for its deactivation or activation at runtime, use the [DiagnosticInfo Action](xref:112818).

Information on the `ShowNavigationItemController` and its **ShowNavigationItem** Action is available in the [Application Model](xref:112580)'s **ActionDesign** node. To access it, use the [Model Editor](xref:112582).