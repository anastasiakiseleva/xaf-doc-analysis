---
uid: DevExpress.Persistent.Validation.IRuleSet.GetRules(System.Object,DevExpress.Persistent.Validation.ContextIdentifiers)
name: GetRules(Object, ContextIdentifiers)
type: Method
summary: Returns a list of all rules for the given object and validation contexts.
syntax:
  content: ReadOnlyCollection<IRule> GetRules(object target, ContextIdentifiers contextIDs)
  parameters:
  - id: target
    type: System.Object
    description: An object for which to collect the rules.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object, which is a set of validation contexts for which rules will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  return:
    type: System.Collections.ObjectModel.ReadOnlyCollection{DevExpress.Persistent.Validation.IRule}
    description: The list of rules.
seealso: []
---
