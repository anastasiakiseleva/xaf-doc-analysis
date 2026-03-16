---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat.FontColor
name: FontColor
type: Property
summary: Specifies the font color of a UI element.
syntax:
  content: Color FontColor { get; set; }
  parameters: []
  return:
    type: System.Drawing.Color
    description: A **System.Drawing.Color** object that specifies the font color.
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontColor
---
The UI elements that implement the **IAppearanceFormat** interface can be formatted (highlighted) by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. The font color is changed via the **FontColor** property.