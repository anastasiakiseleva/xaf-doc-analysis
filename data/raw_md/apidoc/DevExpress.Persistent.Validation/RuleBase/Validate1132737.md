---
uid: DevExpress.Persistent.Validation.RuleBase.Validate(System.Object)
name: Validate(Object)
type: Method
summary: Checks that a particular object satisfies the [Validation Rule](xref:113008).
syntax:
  content: public RuleValidationResult Validate(object target)
  parameters:
  - id: target
    type: System.Object
    description: The object to check.
  return:
    type: DevExpress.Persistent.Validation.RuleValidationResult
    description: A [](xref:DevExpress.Persistent.Validation.RuleValidationResult) object which represents the results of checking the specified object via the Validation Rule.
seealso: []
---
This method contains the logic that checks whether the _target_ object is valid. The method returns a [](xref:DevExpress.Persistent.Validation.RuleValidationResult) object. Its [RuleValidationResult.State](xref:DevExpress.Persistent.Validation.RuleValidationResult.State) property indicates whether a checked object satisfied the Validation Rule. The [RuleValidationResult.ErrorMessage](xref:DevExpress.Persistent.Validation.RuleValidationResult.ErrorMessage) property specifies the exception text, in case the Validation Rule was not satisfied.