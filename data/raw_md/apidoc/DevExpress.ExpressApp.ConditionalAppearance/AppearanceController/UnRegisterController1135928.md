---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.UnRegisterController(DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance)
name: UnRegisterController(ISupportRefreshItemsAppearance)
type: Method
summary: Removes a Controller from the list of registered Controllers.
syntax:
  content: public void UnRegisterController(ISupportRefreshItemsAppearance controller)
  parameters:
  - id: controller
    type: DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance
    description: A Controller implementing the **ISupportRefreshItemsAppearance** interface.
seealso: []
---
When the Controller you registered in the Appearance Controller is deactivated, remove it from the list of registered Controllers using the **UnRegisterController** method. Pass this Controller as the _controller_ parameter.

To determine when you need to register a Controller, refer to the [AppearanceController.RegisterController](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.RegisterController(DevExpress.ExpressApp.ConditionalAppearance.ISupportRefreshItemsAppearance)) method description.