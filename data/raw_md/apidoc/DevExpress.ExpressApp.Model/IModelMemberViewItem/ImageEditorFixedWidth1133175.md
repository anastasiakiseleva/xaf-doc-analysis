---
uid: DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorFixedWidth
name: ImageEditorFixedWidth
type: Property
summary: Specifies the fixed width of the current Property Editor.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    int ImageEditorFixedWidth { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the fixed width of the current Property Editor.
seealso:
- linkId: "112792"
---
This property is considered for image type properties, if the [IModelMemberViewItem.ImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorMode) property is set to [ImageEditorMode.PictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.PictureEdit).

This property is initially set to the [IModelMember.DetailViewImageEditorFixedWidth](xref:DevExpress.ExpressApp.Model.IModelMember.DetailViewImageEditorFixedWidth) of the [](xref:DevExpress.ExpressApp.Model.IModelMember) node that corresponds to the current Property Editor.

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.

![ImageEditorFixedWidth property in Model Editor](~/images/ImageEditorFixedWidth_img.png)