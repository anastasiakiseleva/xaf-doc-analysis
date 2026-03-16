---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute.SkipNullOrEmptyValues
name: SkipNullOrEmptyValues
type: Property
summary: Specifies whether the current rule is checked for the properties that are set to `null`, an empty string (for string type propeties) or a minimal date (for DateTime type properties).
syntax:
  content: public bool SkipNullOrEmptyValues { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if null-like values are not checked by the current rule; otherwise, **false**.'
seealso: []
---
When defining a rule, you can specify whether to consider the properties that are set to null, an empty string (for string type propeties) or a minimal date (for DateTime type properties) when checking the rule. To set the required behavior for a rule that is defined via a validation attribute, use the named _SkipNullOrEmptyValues_ parameter.

# [C#](#tab/tabid-csharp)

```csharp
[RuleUniqueValue(DefaultContexts.Save, SkipNullOrEmptyValues = false)]
public string UniqueValue { 
   //...
}
```
***

By default, **SkipNullOrEmptyValues** is set to **false** in the **RuleRequiredField** rule; in the remaning validation rules, it is set to **true**.

The **SkipNullOrEmptyValues** behavior specified for a validation rule in code is set for the **SkipNullOrEmptyValues** property of the Application Model's [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) node. So, you can change this behavior directly in the [Model Editor](xref:112582).