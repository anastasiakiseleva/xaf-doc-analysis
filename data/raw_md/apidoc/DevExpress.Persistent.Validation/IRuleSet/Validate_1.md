---
uid: DevExpress.Persistent.Validation.IRuleSet.Validate(DevExpress.ExpressApp.IObjectSpace,System.Object,DevExpress.Persistent.Validation.ContextIdentifiers)
name: Validate(IObjectSpace, Object, ContextIdentifiers)
type: Method
summary: Validates an object against the `IRuleSet`'s rules with the given validation contexts. Throws a [](xref:DevExpress.Persistent.Validation.ValidationException) if the validation fails.
syntax:
  content: void Validate(IObjectSpace targetObjectSpace, object target, ContextIdentifiers contextIDs)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used to load objects being validated by a rule.
  - id: target
    type: System.Object
    description: An object to validate.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object, which is a set of validation contexts for which rules will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
seealso: []
---

This method raises the [IRuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.IRuleSet.ValidationCompleted) event.