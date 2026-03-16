---
uid: DevExpress.ExpressApp.Model.IModelMember.GroupInterval
name: GroupInterval
type: Property
summary: Specifies the default group interval for the current property.
syntax:
  content: |-
    [ModelBrowsable(typeof(DateTimePropertyOnlyCalculator))]
    GroupInterval GroupInterval { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.GroupInterval
    description: A [](xref:DevExpress.ExpressApp.Model.GroupInterval) enumeration value which specifies the default group interval.
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelColumn.GroupInterval
---
This property is considered for DateTime properties. When the **GroupInterval** is specified, the groups are not created for each unique value, but for specific value ranges.