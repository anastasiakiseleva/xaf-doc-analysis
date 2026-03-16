---
uid: DevExpress.Persistent.Validation.IValidator.RuleSet
name: RuleSet
type: Property
summary: Returns an object that contains all Validation Rules declared in an XAF application.
syntax:
  content: IRuleSet RuleSet { get; }
  parameters: []
  return:
    type: DevExpress.Persistent.Validation.IRuleSet
    description: An object that implements an `IRuleSet` interface.
seealso:
- linkId: DevExpress.Persistent.Validation.IRuleSet
---

The object returned by this property contains all Validation Rules declared in an application. The `IRuleSet` object's methods allow you to trigger validation programmatically. To learn how to do this, refer to the following topic: <xref:113010>.