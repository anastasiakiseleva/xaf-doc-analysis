---
uid: DevExpress.ExpressApp.Validation.ModelValidationRulesNodeGenerator.GetRuleInfoString(DevExpress.Persistent.Validation.IRuleBaseProperties)
name: GetRuleInfoString(IRuleBaseProperties)
type: Method
summary: Returns a string that specifies the [](xref:DevExpress.Persistent.Validation.IRuleBaseProperties) object in a human-readable manner.
syntax:
  content: public static string GetRuleInfoString(IRuleBaseProperties ruleProperties)
  parameters:
  - id: ruleProperties
    type: DevExpress.Persistent.Validation.IRuleBaseProperties
    description: An **IRuleBaseProperties** object to be specified in a human-readable manner.
  return:
    type: System.String
    description: A string that specifies the **IRuleBaseProperties** object in a human-readable manner.
seealso: []
---
This method returns a string which includes the [IRuleBaseProperties.Id](xref:DevExpress.Persistent.Validation.IRuleBaseProperties.Id) value and the full name of the [IRuleBaseProperties.TargetType](xref:DevExpress.Persistent.Validation.IRuleBaseProperties.TargetType) type. Additionally, if the _ruleProperties_ object supports the **IRulePropertyValueProperties** interface, the **IRulePropertyValueProperties.TargetPropertyName** is included.