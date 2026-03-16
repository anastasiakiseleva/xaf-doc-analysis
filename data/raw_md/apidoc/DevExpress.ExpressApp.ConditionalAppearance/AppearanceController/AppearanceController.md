---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController
name: AppearanceController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that applies [conditional appearance rules](xref:113286) to specified UI elements.
syntax:
  content: 'public class AppearanceController : ObjectViewController'
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController._members
  altText: AppearanceController Members
---
The Appearance Controller provides members that apply conditional appearance rules to the specified UI elements. So, the [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method can be invoked from any View Controller to apply appropriate conditional appearance rules to the passed UI element (View Item, Layout Item or an Action). For instance, the **ListViewItemAppearanceController** invokes this method to apply the appropriate conditional appearance rules to the properties displayed in the current List View. However, there are common scenarios when a conditional appearance must be refreshed for UI elements of different types at the same time. For instance, when a View's current object is changed, the conditional appearance must be refreshed for Detail View Items, Layout Items and Actions. So, we introduced the **ISupportRefreshItemsAppearance** interface. The Controllers that support this interface implement the **RefreshViewItemsAppearance** method. In this method, they call the  Appearance Controller's **RefreshItemAppearance** method for each target UI element. To invoke the **ISupportRefreshItemsAppearance.RefreshViewItemsAppearance** method in common scenarios, these Controllers are registered in the Appearance Controller. This Controller's [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method calls the **ISupportRefreshItemsAppearance.RefreshViewItemsAppearance** method for all registered Controllers to refresh the conditional appearance for UI elements of difference types in a particular scenario.

To learn about the conditional appearance rule, refer to the [Conditional Appearance Module Overview](xref:113286) topic. To learn how to declare rules, refer to the [Declare Conditional Appearance Rules in the Application Model](xref:113372) and [Declare Conditional Appearance Rules in Code](xref:113371) topics.

You can influence the way the Appearance Controller collects and applies conditional appearance rules. For this purpose, handle the following events:

* [AppearanceController.CollectAppearanceRules](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CollectAppearanceRules)
* [AppearanceController.CustomApplyAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CustomApplyAppearance)
* [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied)

Refer to the [How to: Customize the Conditional Appearance Module Behavior](xref:113374) topic to see the examples of handling these events.