---
uid: DevExpress.ExpressApp.Editors.IAppearanceFormat.BackColor
name: BackColor
type: Property
summary: Specifies the background color of a UI element.
syntax:
  content: Color BackColor { get; set; }
  parameters: []
  return:
    type: System.Drawing.Color
    description: A **System.Drawing.Color** object that specifies the background color.
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.BackColor
---
The UI elements that implement the **IAppearanceFormat** interface can be formatted (highlighted) by the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController) according to conditional appearance rules. The background style is changed via the **BackColor** property.