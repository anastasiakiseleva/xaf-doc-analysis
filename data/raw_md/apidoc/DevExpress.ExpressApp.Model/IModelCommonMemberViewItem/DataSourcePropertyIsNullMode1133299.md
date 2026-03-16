---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourcePropertyIsNullMode
name: DataSourcePropertyIsNullMode
type: Property
summary: Specifies objects displayed in the current Lookup Property Editor, when the [IModelMemberViewItem.DataSourceProperty](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.DataSourceProperty) property is `null`.
syntax:
  content: |-
    [ModelBrowsable(typeof(ListEditorsVisibilityCalculator))]
    DataSourcePropertyIsNullMode DataSourcePropertyIsNullMode { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.DataSourcePropertyIsNullMode
    description: A [](xref:DevExpress.Persistent.Base.DataSourcePropertyIsNullMode) enumeration value specifying objects displayed in the current Lookup Property Editor, when the `DataSourceProperty` property is `null`.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourcePropertyIsNullCriteria
---
This property is considered when the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) is applied to the current Property Editor.