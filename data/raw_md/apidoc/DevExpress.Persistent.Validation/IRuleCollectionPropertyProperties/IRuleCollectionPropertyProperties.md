---
uid: DevExpress.Persistent.Validation.IRuleCollectionPropertyProperties
name: IRuleCollectionPropertyProperties
type: Interface
summary: Declares members implemented by classes which represent properties of [Validation Rules](xref:113008) that support [collection validation](xref:113217), exported to the [Application Model](xref:112580).
syntax:
  content: |-
    [DomainComponent]
    [GenerateMessageTemplatesModel("RuleCollectionProperty")]
    public interface IRuleCollectionPropertyProperties : IRuleBaseProperties
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleCollectionPropertyProperties._members
  altText: IRuleCollectionPropertyProperties Members
- linkId: "113008"
---
When implementing a custom Validation Rules Properties class, it is generally easier to inherit from the [](xref:DevExpress.Persistent.Validation.RuleBaseProperties) class or one of its descendants, instead of implementing the **IRuleCollectionPropertyProperties** interface. To see an example of implementing a custom Validation Rule Properties class, refer to the [Implement Custom Rules](xref:113051) topic.