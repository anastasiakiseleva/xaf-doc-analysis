---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.WriteValue
name: WriteValue()
type: Method
summary: Sets the value that is specified in the current Property Editor's control for the bound property.
syntax:
  content: public void WriteValue()
seealso: []
---
This method writes the value that is set for the current Property Editor's control to the related property (see [PropertyEditor.PropertyName](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyName)). After that method, the [PropertyEditor.PropertyValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.PropertyValue) property is set to the [PropertyEditor.ControlValue](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValue) property value.

You can  modify the process of saving the control's value to the property using the following events: [PropertyEditor.ValueStoring](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStoring), [PropertyEditor.ControlValueChanged](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValueChanged) and [PropertyEditor.ValueStored](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored).

The **WriteValue** method is not called in the Windows Forms Property Editors because they support **Binding** (see System.Windows.Forms.Binding in MSDN). However, the [PropertyEditor.ValueStoring](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStoring), [PropertyEditor.ControlValueChanged](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ControlValueChanged) and [PropertyEditor.ValueStored](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored) events are additionally raised. So, when implementing a descendant of the [](xref:DevExpress.ExpressApp.Editors.PropertyEditor) class that supports binding, call the **OnValueStoring** and **OnValueStored** methods where required, so that you can subscribe the corresponding events. If you implement a Property Editor and do not use Binding, override the **WriteValueCore** method if you need to perform additional actions, except setting the **PropertyValue** to the **ControlValue**. In this instance, you do not have to be concerned with raising the corresponding events.