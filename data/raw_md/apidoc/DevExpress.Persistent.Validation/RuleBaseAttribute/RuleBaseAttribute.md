---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute
name: RuleBaseAttribute
type: Class
summary: Represents a base class for [validation system](xref:113008) attributes.
syntax:
  content: 'public abstract class RuleBaseAttribute : Attribute, IRuleBaseAttribute, IRuleCollectionPropertyProperties, IRuleBaseProperties'
seealso:
- linkId: DevExpress.Persistent.Validation.RuleBaseAttribute._members
  altText: RuleBaseAttribute Members
- linkId: "113008"
---
In the **XAF**, to define a particular validation rule for a business class or its property, you can use built-in validation attributes. The **RuleBaseAttribute** represents a base class for all validation attributes. It provides properties that can be used in any descendent attribute. For details, refer to the class' member list.

[!include[RuleBaseAttribute-Properties-declaration](~/templates/RuleBaseAttribute-Properties-declaration.md)]

> [!NOTE]
> Alternatively, you can define validation rules in the [Application Model](xref:112580). See the [Validation Rules](xref:113008) topic, for details.
