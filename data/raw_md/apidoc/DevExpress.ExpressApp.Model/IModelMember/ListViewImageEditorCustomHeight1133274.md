---
uid: DevExpress.ExpressApp.Model.IModelMember.ListViewImageEditorCustomHeight
name: ListViewImageEditorCustomHeight
type: Property
summary: Specifies the height of inplace Image Property Editors in List Views, when displaying the property.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    int ListViewImageEditorCustomHeight { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the height of inplace Image Property Editors in List Views, when displaying the property.
seealso:
- linkId: "112792"
---
This property is considered for image type properties, if the [IModelMember.ListViewImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMember.ListViewImageEditorMode) property is set to [ImageEditorMode.PictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.PictureEdit).

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.