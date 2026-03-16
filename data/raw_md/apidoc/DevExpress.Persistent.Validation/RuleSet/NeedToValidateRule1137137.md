---
uid: DevExpress.Persistent.Validation.RuleSet.NeedToValidateRule(DevExpress.ExpressApp.IObjectSpace,DevExpress.Persistent.Validation.IRule,System.Object,System.String@)
name: NeedToValidateRule(IObjectSpace, IRule, Object, out String)
type: Method
summary: Checks if the rule is marked to be validated.
syntax:
  content: public static bool NeedToValidateRule(IObjectSpace targetObjectSpace, IRule rule, object target, out string reason)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used to load objects being validated by a rule.
  - id: rule
    type: DevExpress.Persistent.Validation.IRule
    description: A rule whose validation shall be checked.
  - id: target
    type: System.Object
    description: A rule's target object.
  - id: reason
    type: System.String
    description: Returns a string which is reason to validate the rule or not.
  return:
    type: System.Boolean
    description: '**true**, if the rule will be validated; otherwise, **false**.'
seealso: []
---
