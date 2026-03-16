---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.FontStyle
name: FontStyle
type: Property
summary: Specifies the font style of [AppearanceAttribute.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute.TargetItems) affected by the conditional appearance rule generated from this attribute instance.
syntax:
  content: public DXFontStyle FontStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.Drawing.DXFontStyle
    description: An enumeration value that specifies the font style of target items affected by the conditional appearance rule.
seealso:
- linkId: "113286"
---
The following UI elements can change their font style:

* Data cells in a `GridListEditor` (the font style of the displayed text)
* Nodes in a `TreeListEditor` (the font style of the displayed text)
* Property Editors inherited from the [](xref:DevExpress.ExpressApp.Win.Editors.DXPropertyEditor) type (the font style of the displayed text)
* [](xref:DevExpress.ExpressApp.Editors.StaticText) (the font style of the displayed text)
* Layout Items, Layout Groups, and Tabbed Layout Groups (the font style of the caption)

You can find many examples in the [Declare Conditional Appearance Rules in Code](xref:113371) topic. See these examples in the **Feature Center** demo installed with the XAF in the _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]_ folder, or refer to the [Feature Center demo online](https://demos.devexpress.com/XAF/FeatureCenter/ActionAppearanceControlObject_ListView/).
