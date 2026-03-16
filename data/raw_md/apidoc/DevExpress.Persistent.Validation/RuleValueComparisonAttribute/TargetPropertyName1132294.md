---
uid: DevExpress.Persistent.Validation.RuleValueComparisonAttribute.TargetPropertyName
name: TargetPropertyName
type: Property
summary: Specifies the target collection's element property that must be checked by the current rule.
syntax:
  content: public string TargetPropertyName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string holding the name of the target collection's element property that must be checked by the current rule.
seealso:
- linkId: "113008"
---
Built-in validation rules can be applied to a collection property involved in a relationship (marked with the  **Association** attribute). In this instance, a validation rule ensures that each collection element is valid. An element's property that must be checked is specified via the **TargetPropertyName** named parameter.