---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsPalette.Palette
name: Palette
type: Property
summary: Specifies the palette used by a WinForms application's current SVG [skin](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsSkin.Skin).
syntax:
  content: |-
    [DataSourceProperty("Palettes", new string[]{})]
    [ModelBrowsable(typeof(PaletteOptionModelVisibilityCalculator))]
    string Palette { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the palette used by a WinForms application's current SVG skin.
seealso: []
---
You can change this property value in the [Model Editor](xref:112582). The property is available if an SVG skin is selected for a WinForms Application.

![WinForms-IModelApplicationOptionsPalette-Palette](~/images/WinForms-IModelApplicationOptionsPalette-Palette.png)

In [LightStyle](xref:DevExpress.ExpressApp.Win.WinApplication.UseLightStyle), XAF displays new WinForms [runtime skin selectors](xref:2399) for end-users.
