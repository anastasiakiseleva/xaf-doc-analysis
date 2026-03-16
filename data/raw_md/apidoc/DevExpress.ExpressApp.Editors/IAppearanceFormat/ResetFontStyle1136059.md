---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat.ResetFontStyle
name: ResetFontStyle()
type: Method
summary: Resets a UI element's font style, if it has been changed by a [conditional appearance rule](xref:113286).
syntax:
  content: void ResetFontStyle()
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontStyle
---
The UI elements that implement the **IAppearanceFormat** interface can be formatted (highlighted) by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. For instance, a font style can be changed via the [IAppearanceFormat.FontStyle](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.FontStyle) property. At the same time, you can reset the applied font style to a default one, if required. For instance, handle the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event, access the required item using the [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item) parameter and reset the font style by casting the item to the **IAppearanceFormat** interface and using the **ResetFontStyle** method.