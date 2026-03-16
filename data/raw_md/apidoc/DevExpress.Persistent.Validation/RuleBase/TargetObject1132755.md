---
uid: DevExpress.Persistent.Validation.RuleBase.TargetObject
name: TargetObject
type: Property
summary: Specifies the object currently being validated by the [Validation Rule](xref:113008).
syntax:
  content: public object TargetObject { get; }
  parameters: []
  return:
    type: System.Object
    description: An object currently being validated by the Validation Rule.
seealso: []
---
This property returns the object that is currently being validated by the [RuleBase.Validate](xref:DevExpress.Persistent.Validation.RuleBase.Validate(System.Object)) method. After the object is validated, this property is set to `null`.