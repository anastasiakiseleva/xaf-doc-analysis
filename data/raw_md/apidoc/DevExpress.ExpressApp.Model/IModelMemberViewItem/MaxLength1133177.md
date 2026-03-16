---
uid: DevExpress.ExpressApp.Model.IModelMemberViewItem.MaxLength
name: MaxLength
type: Property
summary: Specifies the maximum number of characters that users can type in the Property Editor.
syntax:
  content: |-
    [ModelBrowsable(typeof(ListEditorsVisibilityCalculator))]
    int MaxLength { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: The maximum number of characters that users can type in the Property Editor.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelMember.Size
---
You can also specify the [IModelMember.Size](xref:DevExpress.ExpressApp.Model.IModelMember.Size) property. This property affects all Property Editors of the specific member.