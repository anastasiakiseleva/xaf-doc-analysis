---
uid: DevExpress.Persistent.Validation.IRuleBaseProperties.SkipNullOrEmptyValues
name: SkipNullOrEmptyValues
type: Property
summary: Specifies whether the [Validation Rule](xref:113008) is checked for the properties that are set to `null`, an empty string (for string type properties) or a minimal date (for DateTime type properties).
syntax:
  content: |-
    [DefaultValue(true)]
    bool SkipNullOrEmptyValues { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the Validation Rule is not checked; otherwise, **false**.'
seealso:
- linkId: DevExpress.Persistent.Validation.RuleBaseAttribute.SkipNullOrEmptyValues
---
