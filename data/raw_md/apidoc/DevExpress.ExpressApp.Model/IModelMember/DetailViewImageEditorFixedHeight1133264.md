---
uid: DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorFixedHeight
name: DetailViewImageEditorFixedHeight
type: Property
summary: Specifies the fixed height of Image Property Editors in Detail Views when displaying the property.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    int DetailViewImageEditorFixedHeight { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the fixed height of Image Property Editors in Detail Views when displaying the property.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorFixedWidth
---
This property is considered for image type properties, if the [IModelMember.DetailViewImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorMode) property is set to [ImageEditorMode.PictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.PictureEdit).

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.