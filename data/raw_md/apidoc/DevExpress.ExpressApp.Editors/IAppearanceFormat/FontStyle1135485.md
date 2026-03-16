---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat.FontStyle
name: FontStyle
type: Property
summary: Specifies the font style of a UI element.
syntax:
  content: DXFontStyle FontStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.Drawing.DXFontStyle
    description: An enumeration value that specifies the font style.
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontStyle
---
The UI elements that implement the **IAppearanceFormat** interface can be formatted (highlighted) by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. The font style is changed via the **FontStyle** property.