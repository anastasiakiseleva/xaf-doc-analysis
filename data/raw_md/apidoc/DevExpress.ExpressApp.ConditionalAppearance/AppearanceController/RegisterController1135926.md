---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RegisterController(DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance)
name: RegisterController(ISupportRefreshItemsAppearance)
type: Method
summary: Registers a Controller to refresh the conditional appearance of its UI elements in common scenarios.
syntax:
  content: public void RegisterController(ISupportRefreshItemsAppearance controller)
  parameters:
  - id: controller
    type: DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance
    description: A Controller implementing the **ISupportRefreshItemsAppearance** interface.
seealso: []
---
While any Controller can call the [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method when required, there are scenarios common to different UI element types when their conditional appearance must be refreshed. These scenarios are the following:

* [BaseObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ObjectChanged)
* [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed)
* [View.SelectionChanged](xref:DevExpress.ExpressApp.View.SelectionChanged)
* [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged)

To refresh the required UI elements in the listed scenarios, do the following:

* Introduce a View Controller that implements the **ISupportRefreshItemsAppearance** interface.
* In the **ISupportRefreshItemsAppearance.RefreshViewItemsAppearance** method, call the [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method for the required UI elements, passing them as the _item_ parameter.
* Register your Controller in the Appearance Controller by calling the **RegisterController** method and passing your Controller as the _controller_ parameter.

The Appearance Controller calls the **ISupportRefreshItemsAppearance.RefreshViewItemsAppearance** method of the registered Controllers in the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method.  This method is invoked in the common scenarios listed above and when the Appearance Controller is activated. In addition, a registered Controller's **ISupportRefreshItemsAppearance.RefreshViewItemsAppearance** method is called immediately after registration if this Controller is currently active.

Currently, the following built-in Controllers are registered:

* **ActionAppearanceController**
    
    Refreshes the conditional appearance of the Actions activated for the current View.
* **DetailViewItemAppearanceController**
    
    Refreshes the conditional appearance of the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) contained in the current Detail View. In addition to the common scenarios listed above, this Controller calls the [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method when items are added and when their controls are created.
* **DetailViewLayoutItemAppearanceController**
    
    Refreshes the conditional appearance of the layout items, groups and tabs contained in the current Detail View. In addition to the common scenarios listed above, this Controller calls the [AppearanceController.RefreshItemAppearance](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RefreshItemAppearance*) method when items, groups and tabs are created.

When the registered Controller is deactivated, remove it from the list of registered Controllers using the [AppearanceController.UnRegisterController](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.UnRegisterController(DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance)) method.