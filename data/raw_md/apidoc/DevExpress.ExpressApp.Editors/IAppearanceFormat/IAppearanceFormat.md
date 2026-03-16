---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat
name: IAppearanceFormat
type: Interface
summary: Declares members implemented by the UI elements that can be formatted by a [conditional appearance rule](xref:113286).
syntax:
  content: 'public interface IAppearanceFormat : IAppearanceBase'
seealso:
- linkId: DevExpress.ExpressApp.Editors.IAppearanceFormat._members
  altText: IAppearanceFormat Members
- linkId: DevExpress.ExpressApp.Editors.IAppearanceEnabled
- linkId: DevExpress.ExpressApp.Editors.IAppearanceVisibility
---
The Conditional Appearance module allows you format (highlight) different UI elements when they are displayed under certain conditions. To allow the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) to format UI elements, they should implement the **IAppearanceFormat** interface. This interface exposes the [IAppearanceFormat.BackColor](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.BackColor), [IAppearanceFormat.FontColor](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.FontColor) and [IAppearanceFormat.FontStyle](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.FontStyle) properties, to get or set the appearance format, and the [IAppearanceFormat.ResetBackColor](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.ResetBackColor), [IAppearanceFormat.ResetFontColor](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.ResetFontColor) and [IAppearanceFormat.ResetFontStyle](xref:DevExpress.ExpressApp.Editors.IAppearanceFormat.ResetFontStyle) methods, to reset the appearance format to the required initial value.

This interface is already implemented by base classes representing built-in XAF [Detail View Items](xref:112612), Layout Items and auxiliary adapters that provide access to [List Editor](xref:113189) cells. Implement the **IAppearanceFormat** interface in a custom class representing a UI element so that this element can also be formatted by the AppearanceController.