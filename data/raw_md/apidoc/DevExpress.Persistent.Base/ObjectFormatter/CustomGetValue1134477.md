---
uid: DevExpress.Persistent.Base.ObjectFormatter.CustomGetValue
name: CustomGetValue
type: Event
summary: Occurs when the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method processes a format item. Allows you to provide a custom value that will replace the format item in the resulting string.
syntax:
  content: public static event EventHandler<CustomGetValueEventArgs> CustomGetValue
seealso:
- linkId: DevExpress.Persistent.Base.ObjectFormatter.Format*
- linkId: DevExpress.Persistent.Base.ObjectFormatter.CustomFormatObject
---
When the **Format** method processes a format item, it retrieves the required property value, and replaces the format item with it. If you need to replace a specific format item with a custom value, handle this event. Pass the custom value to the handler's **CustomGetValueEventArgs.Value** parameter. Set the handler's **CustomGetValueEventArgs.Handled** parameter to **true**, to indicate that you have supplied the custom value. Otherwise, the **Format** will handle the retrieval of the property's value.