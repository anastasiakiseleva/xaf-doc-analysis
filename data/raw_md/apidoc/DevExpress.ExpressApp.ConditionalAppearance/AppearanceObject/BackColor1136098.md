---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceObject.BackColor
name: BackColor
type: Property
summary: Specifies a background color for the target UI element.
syntax:
  content: public Color? BackColor { get; set; }
  parameters: []
  return:
    type: System.Nullable{System.Drawing.Color}
    description: A `System.Drawing.Color` object that specifies a background color.
seealso: []
---
If there are conditional appearance rules that apply a background color within the rules appropriate for the target UI element, the `AppearanceObject`'s `BackColor` property returns the background color specified by the rule with the higher priority (see [IAppearance.Priority](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearance.Priority)). If there are no rules that apply a background color, the `BackColor` property returns `null`.