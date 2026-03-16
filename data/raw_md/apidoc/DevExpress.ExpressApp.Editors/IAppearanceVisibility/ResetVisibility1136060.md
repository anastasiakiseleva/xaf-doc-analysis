---
uid: DevExpress.ExpressApp.Editors.IAppearanceVisibility.ResetVisibility
name: ResetVisibility()
type: Method
summary: Resets a UI element's visibility state, if it has been changed by a [conditional appearance rule](xref:113286).
syntax:
  content: void ResetVisibility()
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Visibility
---
The UI elements that implement the **IAppearanceVisibility** interface can be made visible/invisible by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. At the same time, you can reset the applied visibility state to a default value, if required. For instance, handle the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event, access the required item using the [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item) parameter and reset the enabled state by casting the item to the **IAppearanceVisibility** interface and using the **ResetVisibility** method.