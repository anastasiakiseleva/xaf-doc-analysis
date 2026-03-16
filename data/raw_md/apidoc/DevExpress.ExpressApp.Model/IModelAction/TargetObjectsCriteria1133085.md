---
uid: DevExpress.ExpressApp.Model.IModelAction.TargetObjectsCriteria
name: TargetObjectsCriteria
type: Property
summary: Specifies the criteria that must be satisfied by the selected object(s) to make the current Action enabled.
syntax:
  content: |-
    [CriteriaOptions("TargetObjectType")]
    string TargetObjectsCriteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string specifying the criteria that must be satisfied by the selected object(s) to make the current Action enabled.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria
---
The [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) property is initialized based on this property value.

> [!NOTE]
> You can use [Function Criteria Operators](xref:113307) in the criteria assigned to this attribute. The common rules for writing a criteria are described in the [Ways to Build Criteria](xref:113052) topic.