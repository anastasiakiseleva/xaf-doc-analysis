---
uid: DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorCustomHeight
name: ImageEditorCustomHeight
type: Property
summary: Specifies the height of inplace Image Property Editors.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    int ImageEditorCustomHeight { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer value specifying the height of inplace Image Property Editors.
seealso:
- linkId: "112792"
---
This property is considered for columns that correspond to image type properties, if the [IModelMemberViewItem.ImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorMode) property is set to [ImageEditorMode.PictureEdit](xref:DevExpress.Persistent.Base.ImageEditorMode.PictureEdit).

By default, this property is set to the [IModelMember.ListViewImageEditorCustomHeight](xref:DevExpress.ExpressApp.Model.IModelMember.ListViewImageEditorCustomHeight) property value of the [](xref:DevExpress.ExpressApp.Model.IModelMember) node corresponding to the current column.

For more details, refer to the following class description: [](xref:DevExpress.Persistent.Base.ImageEditorAttribute).

![ImageEditorFixedHeight property in Model Editor](~/images/ImageEditorCustomHeight_img.png)