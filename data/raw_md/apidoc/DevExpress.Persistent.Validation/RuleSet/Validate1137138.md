---
uid: DevExpress.Persistent.Validation.RuleSet.Validate(DevExpress.ExpressApp.IObjectSpace,System.Object,DevExpress.Persistent.Validation.ContextIdentifiers,DevExpress.Persistent.Validation.ValidationFailedDelegate)
name: Validate(IObjectSpace, Object, ContextIdentifiers, ValidationFailedDelegate)
type: Method
summary: Validates an object against the **RuleSet**'s rules with the given validation contexts, returns a result and throws a [](xref:DevExpress.Persistent.Validation.ValidationException) if the validation fails.
syntax:
  content: public void Validate(IObjectSpace targetObjectSpace, object target, ContextIdentifiers contextIDs, ValidationFailedDelegate validationFailedDelegate)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: target
    type: System.Object
    description: An object to validate.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: A [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object which is a set of validation contexts, rules for which will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  - id: validationFailedDelegate
    type: DevExpress.Persistent.Validation.ValidationFailedDelegate
    description: A method to call if the validation fails.
seealso: []
---
This method raises the [RuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.RuleSet.ValidationCompleted) and the [RuleSet.RuleValidated](xref:DevExpress.Persistent.Validation.RuleSet.RuleValidated) events.