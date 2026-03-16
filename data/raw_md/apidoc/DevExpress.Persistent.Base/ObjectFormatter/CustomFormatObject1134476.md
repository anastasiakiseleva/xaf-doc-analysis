---
uid: DevExpress.Persistent.Base.ObjectFormatter.CustomFormatObject
name: CustomFormatObject
type: Event
summary: Occurs when the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method is called. Allows you to perform the custom processing of the string passed to the **Format** method.
syntax:
  content: public static event EventHandler<CustomFormatObjectEventArgs> CustomFormatObject
seealso:
- linkId: DevExpress.Persistent.Base.ObjectFormatter.Format*
- linkId: DevExpress.Persistent.Base.ObjectFormatter.CustomGetValue
---
The **Format** method replaces format items in a string with the property values of an object. If its formatting behavior does not suit you, handle this event. The string to be formatted is passed as the event handler's [CustomFormatObjectEventArgs.FormatString](xref:DevExpress.Persistent.Base.CustomFormatObjectEventArgs.FormatString) parameter. The object to be used to replace format items is passed as the event handler's [CustomFormatObjectEventArgs.Object](xref:DevExpress.Persistent.Base.CustomFormatObjectEventArgs.Object) parameter. After you have processed the string, pass the result to the handler's **CustomFormatObjectEventArgs.Result** parameter. Set the handler's **CustomFormatObjectEventArgs.Handled** parameter to **true**, to indicate that you have completely processed the passed string. Otherwise, the changes you have made will be discarded and the **Format** method will perform the default processing of the string.