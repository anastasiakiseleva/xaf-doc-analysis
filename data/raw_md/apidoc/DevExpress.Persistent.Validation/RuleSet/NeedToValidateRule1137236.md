---
uid: DevExpress.Persistent.Validation.RuleSet.NeedToValidateRule(DevExpress.ExpressApp.IObjectSpace,DevExpress.Persistent.Validation.IRule,System.Object,System.String,System.String@)
name: NeedToValidateRule(IObjectSpace, IRule, Object, String, out String)
type: Method
summary: Checks if the rule is marked to be validated.
syntax:
  content: public static bool NeedToValidateRule(IObjectSpace targetObjectSpace, IRule rule, object target, string contextId, out string reason)
  parameters:
  - id: targetObjectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [](xref:DevExpress.ExpressApp.IObjectSpace) used by a validation target.
  - id: rule
    type: DevExpress.Persistent.Validation.IRule
    description: The [](xref:DevExpress.Persistent.Validation.IRule) object whose validation shall be checked.
  - id: target
    type: System.Object
    description: A rule's target object.
  - id: contextId
    type: System.String
    description: A [CustomNeedToValidateRuleEventArgs.ContextId](xref:DevExpress.Persistent.Validation.CustomNeedToValidateRuleEventArgs.ContextId) which is a validation context of the rule.
  - id: reason
    type: System.String
    description: Returns a reason to validate the rule or not.
  return:
    type: System.Boolean
    description: '**true**, if the rule will be validated; otherwise, **false**.'
seealso: []
---
