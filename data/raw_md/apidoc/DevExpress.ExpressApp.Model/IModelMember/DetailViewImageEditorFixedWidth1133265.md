---
uid: DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorFixedWidth
name: DetailViewImageEditorFixedWidth
type: Property
summary: Specifies the fixed width of Image Property Editors in Detail Views when displaying the property.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    int DetailViewImageEditorFixedWidth { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the fixed width of Image Property Editors in Detail Views when displaying the property.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorFixedHeight
---
This property is considered for image type properties, if the [IModelMember.DetailViewImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorMode) property is set to [ImageEditorMode.PictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.PictureEdit).

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.