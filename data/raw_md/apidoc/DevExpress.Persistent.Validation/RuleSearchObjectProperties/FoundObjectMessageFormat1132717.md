---
uid: DevExpress.Persistent.Validation.RuleSearchObjectProperties.FoundObjectMessageFormat
name: FoundObjectMessageFormat
type: Property
summary: Specifies the format for the list of found objects.
syntax:
  content: |-
    [RulePropertiesIndex(2)]
    public string FoundObjectMessageFormat { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string representing the format for the list of found objects.
seealso: []
---
When the [Validation Rule](xref:113008) is inverted ([RuleBaseProperties.InvertResult](xref:DevExpress.Persistent.Validation.RuleBaseProperties.InvertResult) is set to **true**), it will be broken when objects that satisfy the [RuleBaseProperties.TargetCriteria](xref:DevExpress.Persistent.Validation.RuleBaseProperties.TargetCriteria) are found. In this instance, a list of found objects is displayed in the Validation Error window, if the [RuleBaseProperties.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseProperties.CustomMessageTemplate) is not specified.