---
uid: DevExpress.Persistent.Validation.RuleSet.NeedToValidateAggregatedRulesInNestedObjectSpace
name: NeedToValidateAggregatedRulesInNestedObjectSpace
type: Property
summary: Specifies whether or not the [RuleSet.NeedToValidateRule](xref:DevExpress.Persistent.Validation.RuleSet.NeedToValidateRule*) method will return **true** when a rule with an assigned [IRuleSupportsCollectionAggregatesProperties.TargetCollectionAggregate](xref:DevExpress.Persistent.Validation.IRuleSupportsCollectionAggregatesProperties.TargetCollectionAggregate) property and an object from nested Object Space are passed.
syntax:
  content: |-
    [DefaultValue(false)]
    public static bool NeedToValidateAggregatedRulesInNestedObjectSpace { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the **NeedToValidateRule** method will return **true** when a rule with an assigned **TargetCollectionAggregate** property and an object from nested Object Space are passed; otherwise - **false**.'
seealso: []
---
