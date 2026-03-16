---
uid: DevExpress.Persistent.Validation.RuleObjectExistsAttribute.LooksFor
name: LooksFor
type: Property
summary: Specifies the type of objects to be looked for.
syntax:
  content: public Type LooksFor { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A type of the objects to be tested.
seealso: []
---
By default, this property is set to the attribute's target class.

> [!NOTE]
> When defining the [](xref:DevExpress.Persistent.Validation.RuleObjectExistsAttribute) in code, the value for the **LooksFor** property is passed as a named parameter. This means that you do not have to specify it. However, when specifying, use the following format: `LooksFor = typeof(Person)`.