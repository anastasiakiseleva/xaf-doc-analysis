---
uid: DevExpress.ExpressApp.ObjectChangedEventArgs.NewValue
name: NewValue
type: Property
summary: Specifies the new value of a changed property.
syntax:
  content: public object NewValue { get; }
  parameters: []
  return:
    type: System.Object
    description: The new value of a changed property.
seealso: []
---
The [IObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.IObjectSpace.ObjectChanged) event can be triggered when an end-user starts modifying any property value in UI. In this instance, the event is triggered, but the [ObjectChangedEventArgs.OldValue](xref:DevExpress.ExpressApp.ObjectChangedEventArgs.OldValue) and **NewValue** properties are equal. This is the designed behavior. So, if you want to execute a custom activity when a property value change occurs, preliminarily, check the equality of these properties.