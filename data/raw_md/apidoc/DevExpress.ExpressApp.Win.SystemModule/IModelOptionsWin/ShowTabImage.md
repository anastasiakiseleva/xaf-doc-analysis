---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.ShowTabImage
name: ShowTabImage
type: Property
summary: Specifies whether a business object's icon should be displayed in a tab in a WinForms application with the TabbedMDI [UI type](xref:DevExpress.ExpressApp.UIType).
syntax:
  content: |-
    [DefaultValue(true)]
    [ModelBrowsable(typeof(ShowTabImageOptionModelVisibilityCalculator))]
    bool ShowTabImage { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: "**true**, if a business object's icon should be displayed in a tab in a WinForms application with the TabbedMDI UI type; otherwise, **false**."
seealso: []
---
The following image demonstrates the WinForms UI with the disabled and enabled **ShowTabImage** option:

![ShowTabImage](~/images/ShowTabImage.png)