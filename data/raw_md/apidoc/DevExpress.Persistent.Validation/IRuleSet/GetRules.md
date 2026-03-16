---
uid: DevExpress.Persistent.Validation.IRuleSet.GetRules(System.Type,DevExpress.Persistent.Validation.ContextIdentifiers)
name: GetRules(Type, ContextIdentifiers)
type: Method
summary: Returns a list of rules for the given type and validation contexts.
syntax:
  content: ReadOnlyCollection<IRule> GetRules(Type targetType, ContextIdentifiers contextIDs)
  parameters:
  - id: targetType
    type: System.Type
    description: A type of object for which rules will be collected.
  - id: contextIDs
    type: DevExpress.Persistent.Validation.ContextIdentifiers
    description: The [](xref:DevExpress.Persistent.Validation.ContextIdentifiers) object, which is a set of validation contexts for which rules will be collected. Default contexts are stored in the [](xref:DevExpress.Persistent.Validation.DefaultContexts) enumeration.
  return:
    type: System.Collections.ObjectModel.ReadOnlyCollection{DevExpress.Persistent.Validation.IRule}
    description: The list of rules that satisfy both conditions given in parameters.
seealso: []
---
