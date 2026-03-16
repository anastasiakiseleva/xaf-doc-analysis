---
uid: DevExpress.ExpressApp.DC.IMemberInfo.IsAggregated
name: IsAggregated
type: Property
summary: Indicates whether the member references aggregated objects.
syntax:
  content: bool IsAggregated { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the member references aggregated objects; otherwise, **false**.'
seealso: []
---
Aggregated objects are considered a part of the owning object, and cannot exist separately. When an owner object is deleted, any aggregated objects owned by it are deleted as well.