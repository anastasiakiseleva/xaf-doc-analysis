---
uid: DevExpress.Persistent.Validation.RuleSet.CustomIsEmptyValue
name: CustomIsEmptyValue
type: Event
summary: Occurs when the `RuleSet.IsEmptyValue` method is executed to determine whether or not the property value is considered empty.
syntax:
  content: public static event EventHandler<CustomIsEmptyValueEventArgs> CustomIsEmptyValue
seealso: []
---
Note that the event occurs at the validation process of each rule to determine whether a property value should be considered empty.

Handle this event to determine when the [](xref:DevExpress.Persistent.Validation.RuleRequiredFieldAttribute) validation rule considers that its target property has a value. Access the handler's [CustomIsEmptyValueEventArgs.TargetObject](xref:DevExpress.Persistent.Validation.CustomIsEmptyValueEventArgs.TargetObject), [CustomIsEmptyValueEventArgs.PropertyName](xref:DevExpress.Persistent.Validation.CustomIsEmptyValueEventArgs.PropertyName) and [CustomIsEmptyValueEventArgs.PropertyValue](xref:DevExpress.Persistent.Validation.CustomIsEmptyValueEventArgs.PropertyValue) parameters to implement the custom validation logic. Pass the validation result via the handler's [CustomIsEmptyValueEventArgs.IsEmpty](xref:DevExpress.Persistent.Validation.CustomIsEmptyValueEventArgs.IsEmpty) parameter and set the **Handled** parameter to **true**.

[!include[](~/templates/validation-rule-set-event-note.md)]
