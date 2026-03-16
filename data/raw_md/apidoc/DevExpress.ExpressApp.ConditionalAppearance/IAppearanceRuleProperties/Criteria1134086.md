---
uid: DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.Criteria
name: Criteria
type: Property
summary: Specifies the criteria string used when determining whether [IAppearanceRuleProperties.TargetItems](xref:DevExpress.ExpressApp.ConditionalAppearance.IAppearanceRuleProperties.TargetItems) should be affected by the conditional appearance rule.
syntax:
  content: |-
    [CriteriaOptions("DeclaringType")]
    string Criteria { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing the criterion used when determining whether **TargetItems** should be affected by the conditional appearance rule.
seealso:
- linkId: "113307"
- linkId: "113286"
---
To learn how to declare string criteria, refer to the [Ways to Build Criteria](xref:113052) topic. To learn how to use Function Criteria Operators in string criteria, refer to the [Function Criteria Operators](xref:113307) topic.