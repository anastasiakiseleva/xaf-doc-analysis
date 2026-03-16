---
uid: DevExpress.Persistent.Validation.RuleObjectExistsAttribute.IncludeCurrentObject
name: IncludeCurrentObject
type: Property
summary: Specifies whether to check the current business object by this rule.
syntax:
  content: public bool IncludeCurrentObject { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the current object is included into the search scope; otherwise, **false**.'
seealso: []
---
By default, this property is set to **false**.

> [!NOTE]
> When defining the [](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute) in code, the value for the **IncludeCurrentObject** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying, use the following format: `IncludeCurrentObject = True`.