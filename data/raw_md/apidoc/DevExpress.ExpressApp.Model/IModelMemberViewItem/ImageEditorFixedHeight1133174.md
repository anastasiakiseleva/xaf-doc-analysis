---
uid: DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorFixedHeight
name: ImageEditorFixedHeight
type: Property
summary: Specifies the fixed height of the current Property Editor.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    int ImageEditorFixedHeight { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the fixed height of the current Property Editor.
seealso:
- linkId: "112792"
---
This property is considered for image type properties, if the [IModelMemberViewItem.ImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorMode) property is set to [ImageEditorMode.PictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.PictureEdit).

This property is initially set to the [IModelMember.DetailViewImageEditorFixedHeight](xref:DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorFixedHeight) of the [](xref:DevExpress.ExpressApp.Model.IModelMember) node that corresponds to the current Property Editor.

For more details, refer to the following class description: [](xref:DevExpress.Persistent.Base.ImageEditorAttribute).

![ImageEditorFixedHeight property in Model Editor](~/images/ImageEditorFixedHeight_img.png)