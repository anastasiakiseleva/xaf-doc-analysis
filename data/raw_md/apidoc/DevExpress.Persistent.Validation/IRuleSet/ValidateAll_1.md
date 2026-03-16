---
uid: DevExpress.Persistent.Validation.IRuleSet.ValidateAll(DevExpress.ExpressApp.IObjectSpace,System.Collections.IEnumerable,DevExpress.Persistent.Validation.ContextIdentifiers)
name: ValidateAll(IObjectSpace, IEnumerable, ContextIdentifiers)
type: Method
summary: Validates multiple objects against `IRuleSet`'s rules with the given validation contexts. Throws a [](xref:DevExpress.Persistent.Validation.ValidationException) if the validation fails.
syntax:
  content: bool ValidateAll(IObjectSpace targetObjectSpace, IEnumerable targets, ContextIdentifiers contextIDs)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: The [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: targets
    type: System.Collections.IEnumerable
    description: The list of objects to check.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The set of validation contexts to check the rule. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  return:
    type: System.Boolean
    description: '`true` if validation passes; otherwise, `false`.'
seealso: []
---

This method raises the [IRuleSet.ValidationCompleted](xref:DevExpress.Persistent.Validation.IRuleSet.ValidationCompleted) event at the end of validation.