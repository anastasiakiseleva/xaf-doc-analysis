---
uid: DevExpress.Persistent.Validation.RuleBaseAttribute.InvertResult
name: InvertResult
type: Property
summary: Specifies whether the current rule should be inverted, to be checked.
syntax:
  content: public bool InvertResult { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if an inverted rule will be checked; otherwise, **false**.'
seealso: []
---
When defining a rule, you can specify its inverted behavior. When it is inverted, the rule will be satisfied under the conditions that are opposite to those when not inverted. For instance, while a RuleRange rule is satisfied when the target value is within a specified range, the same, but inverted rule will be satisfied when the target value is out of this range. To set the inverted behavior for a rule that is defined via a validation attribute, use the named _InvertResult_ parameter.

# [C#](#tab/tabid-csharp)

```csharp
[RuleRange("",DefaultContexts.Save, 45,35,InvertResult=true)]
public double Amount {
   //...
}
```
***

By default, **InvertResult** is set to **false**.

The inverted behavior specified for a validation rule in code is set for the **InvertResult** property of the [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) node. So, you can change this behavior directly in the Application Model.

> [!NOTE]
> When setting **InvertResult** to **true**, specify the [RuleBaseAttribute.CustomMessageTemplate](xref:DevExpress.Persistent.Validation.RuleBaseAttribute.CustomMessageTemplate) property. This is required, because default message templates are oriented on the **false** value of the **InvertedREsult** property.