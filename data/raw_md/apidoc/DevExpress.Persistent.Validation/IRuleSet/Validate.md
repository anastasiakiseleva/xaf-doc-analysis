---
uid: DevExpress.Persistent.Validation.IRuleSet.Validate(DevExpress.ExpressApp.IObjectSpace,System.Object,DevExpress.Persistent.Validation.ContextIdentifiers,DevExpress.Persistent.Validation.ValidationFailedDelegate)
name: Validate(IObjectSpace, Object, ContextIdentifiers, ValidationFailedDelegate)
type: Method
summary: Validates an object against the `IRuleSet`'s rules with the given validation contexts. If validation fails, the [](xref:DevExpress.Persistent.Validation.ValidationException) is thrown and the method passed as the `validationFailedDelegate` parameter is called.
syntax:
  content: void Validate(IObjectSpace targetObjectSpace, object target, ContextIdentifiers contextIDs, ValidationFailedDelegate validationFailedDelegate)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: target
    type: System.Object
    description: An object to validate.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: A [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object, which is a set of validation contexts for which rules will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  - id: validationFailedDelegate
    type: DevExpress.Persistent.Validation.ValidationFailedDelegate
    description: A method to call if the validation fails.
seealso: []
---

This method raises the [IRuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.IRuleSet.ValidationCompleted) event.