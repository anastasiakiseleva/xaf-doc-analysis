---
uid: DevExpress.Persistent.Validation.IRuleSet.FindRule(System.String)
name: FindRule(String)
type: Method
summary: Returns a rule by its ID.
syntax:
  content: IRule FindRule(string id)
  parameters:
  - id: id
    type: System.String
    description: The string identifier of the rule to search.
  return:
    type: DevExpress.Persistent.Validation.IRule
    description: The [](xref:DevExpress.Persistent.Validation.IRule) object that is the rule whose ID is equal to the parameter.
seealso: []
---

Note that `null` is a valid ID value. Rules without an ID are unsearchable by this method.