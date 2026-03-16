---
uid: DevExpress.Persistent.Validation.RuleStringComparisonAttribute.IgnoreCase
name: IgnoreCase
type: Property
summary: Specifies whether to perfom a case-sensitive comparison.
syntax:
  content: public bool IgnoreCase { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if a case-insensitive comparison will be performed; otherwise, **false**.'
seealso: []
---
By default, this property is set to **false**.

> [!NOTE]
> When defining the [](xref:DevExpress.Persistent.Validation.RuleStringComparisonAttribute) in code, the value for the **IgnoreCase** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying, use the following format: `IgnoreCase = true`.