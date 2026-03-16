---
uid: DevExpress.ExpressApp.Validation.ValidationModule.RuleSetInitialized
name: RuleSetInitialized
type: Event
summary: Occurs after the [](xref:DevExpress.Persistent.Validation.RuleSet) object assigned to the `DevExpress.Persistent.Validation.Validator.RuleSet` property has been initialized via the [ValidationModule.InitializeRuleSet](xref:DevExpress.ExpressApp.Validation.ValidationModule.InitializeRuleSet) method.
syntax:
  content: public event EventHandler<RuleSetInitializedEventArgs> RuleSetInitialized
seealso: []
---
Handle this event to subscribe to the [](xref:DevExpress.Persistent.Validation.RuleSet) object's events, such as the [RuleSet.CustomValidateRule](xref:DevExpress.Persistent.Validation.RuleSet.CustomValidateRule) event.