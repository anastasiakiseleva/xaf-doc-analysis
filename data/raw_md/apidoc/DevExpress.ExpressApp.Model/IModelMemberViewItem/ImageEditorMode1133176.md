---
uid: DevExpress.ExpressApp.Model.IModelMemberViewItem.ImageEditorMode
name: ImageEditorMode
type: Property
summary: Specifies the repository item used to display the current property in List Views.
syntax:
  content: |-
    [ModelBrowsable(typeof(ImagePropertyEditorCalculator))]
    ImageEditorMode ImageEditorMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.ImageEditorMode
    description: An [](xref:DevExpress.Persistent.Base.ImageEditorMode) enumeration value specifying the repository item used to display the current property in List Views.
seealso:
- linkId: "112792"
---
This property is considered for columns that correspond to image type properties. By default, this property is set to the [IModelMember.ListViewImageEditorMode](xref:DevExpress.ExpressApp.Model.IModelMember.ListViewImageEditorMode) of the [](xref:DevExpress.ExpressApp.Model.IModelMember) node that corresponds to the current column.

For details, refer to the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) class description.