---
uid: DevExpress.Persistent.Validation.IRuleBaseProperties.TargetContextIDs
name: TargetContextIDs
type: Property
summary: Specifies the [Contexts](xref:113008) for checking the current Validation Rule.
syntax:
  content: |-
    [Required]
    string TargetContextIDs { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing a list of identifiers of the contexts when the current rule should be checked.
seealso:
- linkId: DevExpress.Persistent.Validation.RuleBaseAttribute.TargetContextIDs
---
This property has the **RulePropertiesRequired** attribute applied. So, the corresponding property of the [Application Model](xref:112580) cannot be empty.