---
uid: DevExpress.Persistent.Validation.IRule.Validate(System.Object)
name: Validate(Object)
type: Method
summary: Checks that a particular object satisfies the [Validation Rule](xref:113008).
syntax:
  content: RuleValidationResult Validate(object target)
  parameters:
  - id: target
    type: System.Object
    description: The object to check.
  return:
    type: DevExpress.Persistent.Validation.RuleValidationResult
    description: A [](xref:DevExpress.Persistent.Validation.RuleValidationResult) object which represents the results of checking the specified object via the Validation Rule.
seealso: []
---
When implementing the [](xref:DevExpress.Persistent.Validation.IRule) interface, this method should contain the logic that checks whether the _target_ object is valid. In the method's body, after checking the target object, instantiate a new [](xref:DevExpress.Persistent.Validation.RuleValidationResult) object and pass the validation results as the constructor's parameters. The instantiated object should be returned as the method's return value.