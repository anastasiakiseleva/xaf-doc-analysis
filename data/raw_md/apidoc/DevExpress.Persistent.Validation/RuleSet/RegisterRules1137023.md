---
uid: DevExpress.Persistent.Validation.RuleSet.RegisterRules(DevExpress.ExpressApp.DC.ITypeInfo)
name: RegisterRules(ITypeInfo)
type: Method
summary: Adds validation rules of the class given as a parameter to the [](xref:DevExpress.Persistent.Validation.RuleSet).
syntax:
  content: public void RegisterRules(ITypeInfo targetType)
  parameters:
  - id: targetType
    type: DevExpress.ExpressApp.DC.ITypeInfo
    description: Type, for which the corresponding class will be scanned for validation rules.
seealso: []
---
The class given as a parameter will be searched for [](xref:DevExpress.Persistent.Validation.RuleBaseAttribute), its descendants and [](xref:DevExpress.Persistent.Validation.CodeRuleAttribute). Validation rules acquired from these attributes will be added to the [](xref:DevExpress.Persistent.Validation.RuleSet).