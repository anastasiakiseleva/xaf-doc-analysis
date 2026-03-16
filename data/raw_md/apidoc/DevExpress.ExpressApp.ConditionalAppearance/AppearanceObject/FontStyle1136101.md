---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.FontStyle
name: FontStyle
type: Property
summary: Specifies a font style for the target UI element.
syntax:
  content: public DXFontStyle? FontStyle { get; set; }
  parameters: []
  return:
    type: System.Nullable{DevExpress.Drawing.DXFontStyle}
    description: An enumeration value that specifies a font style.
seealso: []
---
If there are conditional appearance rules that apply a font style within the rules appropriate for the target UI element, the `AppearanceObject`'s `FontStyle` property returns the font style specified by the rule with the higher priority (see [IAppearance.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Priority)). If there are no rules that apply a font style, the `FontStyle` property returns `null`.