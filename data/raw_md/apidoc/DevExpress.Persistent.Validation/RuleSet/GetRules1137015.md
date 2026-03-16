---
uid: DevExpress.Persistent.Validation.RuleSet.GetRules(System.Collections.Generic.IEnumerable{System.Type})
name: GetRules(IEnumerable<Type>)
type: Method
summary: Returns a list of rules that belongs to the current [](xref:DevExpress.Persistent.Validation.RuleSet).
syntax:
  content: public ReadOnlyCollection<IRule> GetRules(IEnumerable<Type> targetTypesForDelayedCollectRules)
  parameters:
  - id: targetTypesForDelayedCollectRules
    type: System.Collections.Generic.IEnumerable{System.Type}
    description: The list of [](xref:System.Type) objects, rules for which will be collected.
  return:
    type: System.Collections.ObjectModel.ReadOnlyCollection{DevExpress.Persistent.Validation.IRule}
    description: The list of [](xref:DevExpress.Persistent.Validation.IRule) objects for the types defined in a **targetTypesForDelayedCollectRules** parameter.
seealso: []
---
