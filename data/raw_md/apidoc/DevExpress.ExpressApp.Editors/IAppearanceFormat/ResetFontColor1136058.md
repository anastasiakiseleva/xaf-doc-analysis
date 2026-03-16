---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat.ResetFontColor
name: ResetFontColor()
type: Method
summary: Resets a UI element's font color, if it has been changed by a [conditional appearance rule](xref:113286).
syntax:
  content: void ResetFontColor()
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontColor
---
The UI elements that implement the **IAppearanceFormat** interface can be formatted (highlighted) by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. For instance, a font color can be changed via the [IAppearanceFormat.FontColor](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.FontColor) property. At the same time, you can reset the applied font color to a default one, if required. For instance, handle the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event, access the required item using the [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item) parameter and reset the font color by casting the item to the **IAppearanceFormat** interface and using the **ResetFontColor** method.