---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat.ResetBackColor
name: ResetBackColor()
type: Method
summary: Resets a UI element's background color, if it has been changed by a [conditional appearance rule](xref:113286).
syntax:
  content: void ResetBackColor()
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor
---
The UI elements that implement the **IAppearanceFormat** interface can be formatted (highlighted) by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. For instance, a background color can be changed via the [IAppearanceFormat.BackColor](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.BackColor) property. At the same time, you can reset the applied background color to a default one, if required. For instance, handle the [AppearanceController.AppearanceApplied](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.AppearanceApplied) event, access the required item using the [ApplyAppearanceEventArgs.Item](xref:DevExpress.ExpressApp.ConditionalAppearance.ApplyAppearanceEventArgs.Item) parameter and reset the background color by casting the item to the **IAppearanceFormat** interface and using the **ResetBackColor** method.