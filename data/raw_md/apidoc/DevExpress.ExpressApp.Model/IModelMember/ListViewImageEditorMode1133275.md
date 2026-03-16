---
uid: DevExpress.ExpressApp.Model.IModelMember.ListViewImageEditorMode
name: ListViewImageEditorMode
type: Property
summary: Specifies the inplace editor used to display the current property in List Views.
syntax:
  content: |-
    [DefaultValue(ImageEditorMode.PictureEdit)]
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    ImageEditorMode ListViewImageEditorMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.ImageEditorMode
    description: An [](xref:DevExpress.Persistent.Base.ImageEditorMode) enumeration value specifying the inplace editor used to display the current property in List Views.
seealso:
- linkId: "112792"
---
This property is considered for image type properties. By default, this property is set to the [ImageEditorMode.DropDownPictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.DropDownPictureEdit).

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.