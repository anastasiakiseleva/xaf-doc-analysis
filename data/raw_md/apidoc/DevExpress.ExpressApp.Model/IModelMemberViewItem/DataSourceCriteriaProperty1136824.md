---
uid: DevExpress.ExpressApp.Model.IModelMemberViewItem.DataSourceCriteriaProperty
name: DataSourceCriteriaProperty
type: Property
summary: Specifies the name of the property of the [](xref:DevExpress.Data.Filtering.CriteriaOperator) type, whose value is used to filter a Lookup Property Editor displayed for the current property.
syntax:
  content: |-
    [CriteriaOptions("Type,ModelMember.Type")]
    string DataSourceCriteriaProperty { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the name of the property holding the CriteriaOperator which is used to filter a Lookup Property Editor displayed for the current property.
seealso: []
---
This property is considered for Property Editors that display a reference property.

For details, refer to the [](xref:DevExpress.Persistent.Base.DataSourceCriteriaPropertyAttribute) class description.