---
uid: DevExpress.Persistent.Validation.RuleValueComparisonProperties
name: RuleValueComparisonProperties
type: Class
summary: Represent the **RuleValueComparison** [Validation Rules](xref:113008)' properties exported to the [Application Model](xref:112580).
syntax:
  content: |-
    [DomainComponent]
    [RulePropertiesIndexed]
    public class RuleValueComparisonProperties : RulePropertyValueProperties, IRuleValueComparisonProperties, IRulePropertyValueProperties, IRuleCollectionPropertyProperties, IRuleBaseProperties, IRuleSupportsCollectionAggregatesProperties
seealso:
- linkId: DevExpress.Persistent.Validation.RuleValueComparisonProperties._members
  altText: RuleValueComparisonProperties Members
---
Information on the Validation Rules declared in the application is saved to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) node. Each rule has a corresponding node. These nodes expose properties specifying values for the rules' properties.

The properties that must be exposed to the Application Model are specified via a rule's [RuleBase.Properties](xref:DevExpress.Persistent.Validation.RuleBase.Properties) property. This property returns a [](xref:DevExpress.Persistent.Validation.RuleBaseProperties) descendant.

When implementing a custom Validation Rule, you may need to implement a cusom Properties class inherited from **RuleBaseProperties**. For details, refer to the [Implement Custom Rules](xref:113051) topic.