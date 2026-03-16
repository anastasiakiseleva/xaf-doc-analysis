---
uid: DevExpress.Persistent.Validation.RuleSet.EnableRulePropertyValueCache
name: EnableRulePropertyValueCache
type: Field
summary: Specifies if the Validation Module caches Rule values.
syntax:
  content: public static bool EnableRulePropertyValueCache
  return:
    type: System.Boolean
    description: '`true` if the Validation Module caches Rule values. If `false`, the Validation Module loads Rule values from the Application Model.'
seealso: []
---

Do not enable this property if your Application Model has specific Rule values stored in the [user differences](xref:112580#application-model-layers) layer (individual user settings).

The default `EnableRulePropertyValueCache` field value is `true` if the @DevExpress.ExpressApp.FrameworkSettingsCompatibilityMode property value references XAF version 23.1 or higher. Otherwise, the default `EnableRulePropertyValueCache` field value is `false`.