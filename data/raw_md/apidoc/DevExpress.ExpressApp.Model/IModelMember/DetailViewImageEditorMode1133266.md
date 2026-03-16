---
uid: DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorMode
name: DetailViewImageEditorMode
type: Property
summary: Specifies the editor used to display the current property in Detail Views.
syntax:
  content: |-
    [DefaultValue(ImageEditorMode.PictureEdit)]
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    ImageEditorMode DetailViewImageEditorMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.ImageEditorMode
    description: An [](xref:DevExpress.Persistent.Base.ImageEditorMode) enumeration value specifying the editor used to display the current property in Detail Views.
seealso: []
---
This property is considered for image type properties.

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.