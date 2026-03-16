---
uid: DevExpress.Persistent.Validation.RuleRangeAttribute.TargetCollectionAggregate
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
When applied to collection properties, the **RuleRange** can use aggregate functions. When a value is assigned to the **TargetCollectionAggregate** property,  the validation rule does not check the collection property's elements. Instead, it checks the specified aggregate function.