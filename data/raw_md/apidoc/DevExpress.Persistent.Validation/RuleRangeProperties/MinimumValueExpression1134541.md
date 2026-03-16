---
uid: DevExpress.Persistent.Validation.RuleRangeProperties.MinimumValueExpression
name: MinimumValueExpression
type: Property
summary: Specifies the expression whose value is treated as the minimum allowed property value.
syntax:
  content: |-
    [RulePropertiesIndex(4)]
    public string MinimumValueExpression { get; set; }
  parameters: []
  return:
    type: System.String
    description: The string representation of an [expression](xref:4928) whose value represents the left end point of the range that should contain the target property's value.
seealso: []
---
This property value is considered when a rule has been constructed using the _mode_ constructor parameter set to [ParametersMode.Expression](xref:DevExpress.Persistent.Validation.ParametersMode.Expression).