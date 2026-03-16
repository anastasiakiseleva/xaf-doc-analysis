---
uid: DevExpress.Persistent.Validation.IRuleSupportsCollectionAggregatesProperties
name: IRuleSupportsCollectionAggregatesProperties
type: Interface
summary: Declares members implemented by classes which represent properties of [Validation Rules](xref:113008) that support [collection validation using aggregate funcitons](xref:113217), exported to the [Application Model](xref:112580).
syntax:
  content: |-
    [DomainComponent]
    public interface IRuleSupportsCollectionAggregatesProperties : IRulePropertyValueProperties, IRuleCollectionPropertyProperties, IRuleBaseProperties
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleSupportsCollectionAggregatesProperties._members
  altText: IRuleSupportsCollectionAggregatesProperties Members
- linkId: "113008"
---
When implementing a custom Validation Rules Properties class, it is generally easier to inherit from the [](xref:DevExpress.Persistent.Validation.RuleRangeProperties) or [](xref:DevExpress.Persistent.Validation.RuleValueComparisonProperties) class, instead of implementing the **IRuleSupportsCollectionAggregatesProperties** interface. To see an example of implementing a custom Validation Rule Properties class, refer to the [Implement Custom Rules](xref:113051) topic.