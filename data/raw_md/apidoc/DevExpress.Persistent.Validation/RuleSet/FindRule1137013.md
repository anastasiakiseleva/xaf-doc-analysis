---
uid: DevExpress.Persistent.Validation.RuleSet.FindRule(System.String)
name: FindRule(String)
type: Method
summary: Returns a rule by its ID.
syntax:
  content: public IRule FindRule(string id)
  parameters:
  - id: id
    type: System.String
    description: The string identifier of the rule to search.
  return:
    type: DevExpress.Persistent.Validation.IRule
    description: The [](xref:DevExpress.Persistent.Validation.IRule) object that is the rule whose ID is equal to the parameter.
seealso: []
---
Note that `null` is a valid ID value. The rules without ID will be unsearchable by this method.