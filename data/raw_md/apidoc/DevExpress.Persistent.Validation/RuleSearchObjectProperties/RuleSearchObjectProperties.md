---
uid: DevExpress.Persistent.Validation.RuleSearchObjectProperties
name: RuleSearchObjectProperties
type: Class
summary: Serves as the base class for classes which represent object searching [Validation Rules](xref:113008)' properties exported to the [Application Model](xref:112580).
syntax:
  content: |-
    [DomainComponent]
    [RulePropertiesIndexed]
    public class RuleSearchObjectProperties : RuleBaseProperties, IRuleSearchObjectProperties, IRuleCollectionPropertyProperties, IRuleBaseProperties
seealso:
- linkId: DevExpress.Persistent.Validation.RuleSearchObjectProperties._members
  altText: RuleSearchObjectProperties Members
---
Information on the Validation Rules declared in the application is saved to the [Application Model](xref:112580)'s [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) node. Each rule has a corresponding node. These nodes expose properties specifying values for the rules' properties.

The properties that must be exposed to the Application Model are specified via a rule's [RuleBase.Properties](xref:DevExpress.Persistent.Validation.RuleBase.Properties) property. This property returns a [](xref:DevExpress.Persistent.Validation.RuleBaseProperties) descendant.

When implementing a custom Validation Rule, you may need to implement a custom Properties class inherited from the **RuleBaseProperties**. For details, refer to the [Implement Custom Rules](xref:113051) topic.