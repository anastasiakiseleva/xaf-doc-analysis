---
uid: DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.GetStartupNavigationItem
name: GetStartupNavigationItem()
type: Method
summary: Returns the **ShowNavigationItem** Action's item to be chosen when starting up the application.
syntax:
  content: public virtual ChoiceActionItem GetStartupNavigationItem()
  return:
    type: DevExpress.ExpressApp.Actions.ChoiceActionItem
    description: A **ChoiceActionItem** object representing the item in the navigation control to be chosen when loading the main window.
seealso: []
---
This method returns the item which is set for the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node's [IModelRootNavigationItems.StartupNavigationItem](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.StartupNavigationItem) property. If nothing is set for this property, the first visible and enabled item from the first first-level navigation item of the **ShowNavigationItem** Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection is returned.

> [!NOTE]
> This method is used by the **WinShowStartupNavigationItemController** and **WebShowStartupNavigationItemController** to get a navigation item and emulate clicking it.