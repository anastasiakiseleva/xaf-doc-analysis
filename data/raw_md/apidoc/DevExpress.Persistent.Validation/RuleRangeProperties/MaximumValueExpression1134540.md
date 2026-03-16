---
uid: DevExpress.Persistent.Validation.RuleRangeProperties.MaximumValueExpression
name: MaximumValueExpression
type: Property
summary: Specifies the expression whose value is treated as the maximum allowed property value.
syntax:
  content: |-
    [RulePropertiesIndex(5)]
    public string MaximumValueExpression { get; set; }
  parameters: []
  return:
    type: System.String
    description: The string representation of an [expression](xref:4928) whose value represents the right end point of the range that contains the target property's value.
seealso: []
---
This property value is considered when a rule has been constructed using the _mode_ constructor parameter set to [ParametersMode.Expression](xref:DevExpress.Persistent.Validation.ParametersMode.Expression).