---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMaskType
name: EditMaskType
type: Property
summary: Specifies the edit mask type of a value in the current Property Editor.
syntax:
  content: |-
    [ModelBrowsable(typeof(EditMaskTypeVisibilityCalculator))]
    EditMaskType EditMaskType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Editors.EditMaskType
    description: An [](xref:DevExpress.ExpressApp.Editors.EditMaskType) enumeration value specifying the edit mask type of a value in the current Property Editor.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.EditMask
---
The default value is taken from [IModelRegisteredPropertyEditor.DefaultEditMaskType](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultEditMaskType).
> [!NOTE]
> Not all built-in Property Editors support mask editing (see [Data Types Supported by built-in Editors](xref:113014)).