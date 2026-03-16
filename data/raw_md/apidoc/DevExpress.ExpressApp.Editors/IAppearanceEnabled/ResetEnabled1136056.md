---
uid: DevExpress.ExpressApp.Editors.IAppearanceEnabled.ResetEnabled
name: ResetEnabled()
type: Method
summary: Resets a UI element's enabled state, if it has been changed by a [conditional appearance rule](xref:113286).
syntax:
  content: void ResetEnabled()
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.Enabled
---
The UI elements that implement the **IAppearanceEnabled** interface can be disabled/enabled by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. At the same time, you can reset the applied enabled state to a default value, if required. For instance, handle the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event, access the required item using the [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item) parameter and reset the enabled state by casting the item to the **IAppearanceEnabled** interface and using the **ResetEnabled** method.