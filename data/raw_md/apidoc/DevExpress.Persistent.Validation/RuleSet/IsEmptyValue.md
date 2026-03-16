---
uid: DevExpress.Persistent.Validation.RuleSet.IsEmptyValue(System.Object,System.String,System.Object,System.IServiceProvider)
name: IsEmptyValue(Object, String, Object, IServiceProvider)
type: Method
summary: Determines whether or not the validation rule's target property value is considered empty.
syntax:
  content: public static bool IsEmptyValue(object targetObject, string propertyName, object propertyValue, IServiceProvider serviceProvider)
  parameters:
  - id: targetObject
    type: System.Object
    description: An object which is the validation rule's target object.
  - id: propertyName
    type: System.String
    description: A string which is the name of the validation rule's target property.
  - id: propertyValue
    type: System.Object
    description: An object which is the validation rule's target property value.
  - id: serviceProvider
    type: System.IServiceProvider
    description: An object that implements the `IServiceProvider` interface.
  return:
    type: System.Boolean
    description: '**true**, if the value is considered empty; otherwise - **false**.'
seealso: []
---

By default, empty values are:

* a _null_ value;
* a zero length string;
* a DateTime value equal to DateTime.MinValue;
* an [](xref:DevExpress.Persistent.Validation.IEmptyCheckable) value with the [IEmptyCheckable.IsEmpty](xref:DevExpress.Persistent.Validation.IEmptyCheckable.IsEmpty) property set to **true**.

Handle the [RuleSet.CustomIsEmptyValue](xref:DevExpress.Persistent.Validation.RuleSet.CustomIsEmptyValue) event to customize this method behavior.