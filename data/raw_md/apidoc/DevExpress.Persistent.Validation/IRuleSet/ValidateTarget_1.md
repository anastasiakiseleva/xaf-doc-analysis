---
uid: DevExpress.Persistent.Validation.IRuleSet.ValidateTarget(DevExpress.ExpressApp.IObjectSpace,System.Object,DevExpress.Persistent.Validation.ContextIdentifiers)
name: ValidateTarget(IObjectSpace, Object, ContextIdentifiers)
type: Method
summary: Silently validates an object (without raising the [RuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.IRuleSet.ValidationCompleted) event and throwing the [](xref:DevExpress.Persistent.Validation.ValidationException)) and returns a result.
syntax:
  content: RuleSetValidationResult ValidateTarget(IObjectSpace targetObjectSpace, object target, ContextIdentifiers contextIDs)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: target
    type: System.Object
    description: An object for which to check the [](xref:DevExpress.Persistent.Validation.RuleSet).
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The set of validation contexts. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  return:
    type: DevExpress.Persistent.Validation.RuleSetValidationResult
    description: The validation result. If all rules are satisfied, the `RuleSetValidationResult.IsValid` property returns `true`; otherwise, it returns `false`
seealso: []
---
