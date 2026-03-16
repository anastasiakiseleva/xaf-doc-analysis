---
uid: DevExpress.Persistent.Validation.IRuleBaseProperties
name: IRuleBaseProperties
type: Interface
summary: Declares members implemented by classes which represent [Validation Rules](xref:113008)' properties exported to the [Application Model](xref:112580).
syntax:
  content: |-
    [DomainComponent]
    [GenerateMessageTemplatesModel("RuleBase")]
    public interface IRuleBaseProperties
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleBaseProperties._members
  altText: IRuleBaseProperties Members
- linkId: "113008"
---
When implementing a custom Validation Rules Properties class, it is generally easier to inherit from the [](xref:DevExpress.Persistent.Validation.RuleBaseProperties) class or one of its descendants, instead of implementing the **IRuleBaseProperties** interface. To see an example of implementing a custom Validation Rule Properties class, refer to the [Implement Custom Rules](xref:113051) topic.