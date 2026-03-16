---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.FontColor
name: FontColor
type: Property
summary: Specifies a font color for the target UI element.
syntax:
  content: public Color? FontColor { get; set; }
  parameters: []
  return:
    type: System.Nullable{System.Drawing.Color}
    description: A `System.Drawing.Color` object that specifies a font color.
seealso: []
---
If there are conditional appearance rules that apply a font color within the rules appropriate for the target UI element, the `AppearanceObject`'s `FontColor` property returns the font color specified by the rule with the higher priority (see [IAppearance.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Priority)). If there are no rules that apply a font color, the `FontColor` property returns `null`.