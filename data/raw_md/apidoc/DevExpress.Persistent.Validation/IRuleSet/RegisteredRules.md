---
uid: DevExpress.Persistent.Validation.IRuleSet.RegisteredRules
name: RegisteredRules
type: Property
summary: Adds validation rules of the class given as a parameter to the [](xref:DevExpress.Persistent.Validation.IRuleSet).
syntax:
  content: IList<IRule> RegisteredRules { get; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.Persistent.Validation.IRule}
    description: The type for which the corresponding class will be scanned for validation rules.
seealso: []
---

The class passed as a parameter will be searched for the [](xref:DevExpress.Persistent.Validation.RuleBaseAttribute), its descendants, and the [](xref:DevExpress.Persistent.Validation.CodeRuleAttribute). Validation rules acquired from these attributes will be added to the [](xref:DevExpress.Persistent.Validation.IRuleSet).