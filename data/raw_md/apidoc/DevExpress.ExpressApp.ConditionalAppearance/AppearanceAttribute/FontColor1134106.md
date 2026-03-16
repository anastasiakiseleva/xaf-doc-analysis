---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontColor
name: FontColor
type: Property
summary: Specifies the font color of [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) affected by the conditional appearance rule generated from this attribute instance.
syntax:
  content: public string FontColor { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the font color of target items affected by the conditional appearance rule. A value should be recognizable by the [System.Drawing.ColorConverter](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.colorconverter) class.
seealso:
- linkId: "113286"
- linkId: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.AppearanceItemType
---
The following UI elements can change their font color:

* Data cells in a `GridListEditor` (the font color of the displayed text)
* Nodes in a `TreeListEditor` (the font color of the displayed text)
* Property Editors that are inherited from the [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) type (the font color of the displayed text)
* [](xref:DevExpress.ExpressApp.Editors.StaticText) (the font color of the displayed text)
* Layout Items, Layout Groups and Tabbed Layout Groups (the font color of the caption)

**Example 1**

[!include[ConditionalFormatting_CategoryColoredInListViewRule](~/templates/conditionalformatting_categorycoloredinlistviewrule11918.md)]

**Example 2**

[!include[ConditionalApearance_LayoutGroup](~/templates/conditionalapearance_layoutgroup11920.md)]

[!include[<`Appearance` attribute>](~/templates/main-demo-tip.md)]
