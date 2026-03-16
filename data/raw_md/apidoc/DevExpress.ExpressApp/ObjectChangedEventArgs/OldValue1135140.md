---
uid: DevExpress.ExpressApp.ObjectChangedEventArgs.OldValue
name: OldValue
type: Property
summary: Specifies the old value of a changed property.
syntax:
  content: public object OldValue { get; }
  parameters: []
  return:
    type: System.Object
    description: The old value of a changed property.
seealso: []
---
The [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) event can be triggered when an end-user starts modifying any property value in a UI. In this instance, the event is triggered, but the [ObjectChangedEventArgs.NewValue](xref:DevExpress.ExpressApp.ObjectChangedEventArgs.NewValue) and **OldValue** properties are equal. This is the designed behavior. So, if you want to execute a custom activity when a property value change occurs, check the equality of these properties preliminarily.