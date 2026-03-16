---
uid: DevExpress.ExpressApp.Model.IModelColumn.GroupInterval
name: GroupInterval
type: Property
summary: Specifies the group interval.
syntax:
  content: |-
    [DefaultValue(GroupInterval.None)]
    GroupInterval GroupInterval { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.GroupInterval
    description: A [](xref:DevExpress.ExpressApp.Model.GroupInterval) enumeration value specifying the group interval. The default is **GroupInterval.None**.
seealso: []
---
This property is considered for DateTime properties. When the **GroupInterval** is specified, the groups are not created for each DateTime unique value, but for specific value ranges.