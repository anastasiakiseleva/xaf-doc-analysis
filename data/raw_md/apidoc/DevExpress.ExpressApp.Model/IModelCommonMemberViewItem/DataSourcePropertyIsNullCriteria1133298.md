---
uid: DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourcePropertyIsNullCriteria
name: DataSourcePropertyIsNullCriteria
type: Property
summary: Specifies the criteria upon which a list of objects is formed in the current lookup Property Editor.
syntax:
  content: |-
    [CriteriaOptions("MemberInfo,Type,ModelMember.Type")]
    [ModelBrowsable(typeof(ListEditorsVisibilityCalculator))]
    string DataSourcePropertyIsNullCriteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the criteria upon which a list of objects is formed in the current lookup Property Editor.
seealso: []
---
This property is considered when the [IModelCommonMemberViewItem.DataSourcePropertyIsNullMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.DataSourcePropertyIsNullMode) property is set to [DataSourcePropertyIsNullMode.CustomCriteria](xref:DevExpress.Persistent.Base.DataSourcePropertyIsNullMode.CustomCriteria).