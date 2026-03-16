---
uid: DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.ResetRulesCache
name: ResetRulesCache()
type: Method
summary: Resets the cache of the rules collected by the Appearance Controller at the current moment.
syntax:
  content: public void ResetRulesCache()
seealso: []
---
So that the Appearance Controller doesn't collect rules each time the conditional appearance is refreshed for a target UI element, it caches them. The rules are collected for a particular UI element when the conditional appearance is applied for the first time. Then, each time the conditional appearance is refreshed for this element, the rules from the cache are applied. If you add a rule dynamically, using the [AppearanceController.CollectAppearanceRules](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.CollectAppearanceRules) event, we recommend that you first call the **ResetRulesCache** method to reset the cache, then add the rule and finally, call the [AppearanceController.Refresh](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController.Refresh) method to apply the rule.