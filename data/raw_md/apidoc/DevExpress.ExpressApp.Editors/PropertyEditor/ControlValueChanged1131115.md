---
uid: DevExpress.ExpressApp.Editors.PropertyEditor.ControlValueChanged
name: ControlValueChanged
type: Event
summary: Occurs after the underlying control's value has been changed.
syntax:
  content: public event EventHandler ControlValueChanged
seealso: []
---
Handle this event to perform custom actions with the newly set control value. XAF handles the `ControlValueChanged` event of all Property Editors to promptly react to control value changes - for example, to enable the **Save** action.

`PropertyEditor` descendants use the `OnControlValueChanged` method to raise the `ControlValueChanged` event. In custom Property Editors, call the `OnControlValueChanged` method after the control value changes, as shown in the following examples:

* [](xref:402189)
* [](xref:112679)