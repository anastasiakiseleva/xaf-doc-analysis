---
uid: DevExpress.Persistent.Validation.RuleValueComparisonAttribute.TargetCollectionAggregate
name: TargetCollectionAggregate
type: Property
summary: Specifies the aggregate function to be checked by the current rule.
syntax:
  content: public Aggregate TargetCollectionAggregate { get; set; }
  parameters: []
  return:
    type: DevExpress.Data.Filtering.Aggregate
    description: A **Devexpress.Data.Filtering.Aggregate** enumeration value which specifies the aggregate function to be checked by the current rule.
seealso:
- linkId: "113008"
---
When applied to collection properties, the **RuleValueComparison** can use aggregate functions. When a value is assigned to the **TargetCollectionAggregate** property,  the validation rule checks the specified aggregate function.

[!include[RuleValueComparison_CollectionNote](~/templates/rulevaluecomparison_collectionnote111284.md)]