---
uid: DevExpress.ExpressApp.Validation.RuleSetInitializedEventArgs
name: RuleSetInitializedEventArgs
type: Class
summary: Arguments passed to the [ValidationModule.RuleSetInitialized](xref:DevExpress.ExpressApp.Validation.ValidationModule.RuleSetInitialized) event.
syntax:
  content: 'public class RuleSetInitializedEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Validation.RuleSetInitializedEventArgs._members
  altText: RuleSetInitializedEventArgs Members
---

The `RuleSetInitialized` event occurs after the `DevExpress.Persistent.Validation.Validator.RuleSet` has been initialized by the [ValidationModule.InitializeRuleSet](xref:DevExpress.ExpressApp.Validation.ValidationModule.InitializeRuleSet) method. Handle this event to subscribe to the [](xref:DevExpress.Persistent.Validation.RuleSet) object's events such as the [RuleSet.CustomValidateRule](xref:DevExpress.Persistent.Validation.RuleSet.CustomValidateRule) event.