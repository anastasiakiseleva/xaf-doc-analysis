---
uid: DevExpress.Persistent.Base.CustomFormatObjectEventArgs
name: CustomFormatObjectEventArgs
type: Class
summary: Arguments passed to the [ObjectFormatter.CustomFormatObject](xref:DevExpress.Persistent.Base.ObjectFormatter.CustomFormatObject) event.
syntax:
  content: 'public class CustomFormatObjectEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.Persistent.Base.CustomFormatObjectEventArgs._members
  altText: CustomFormatObjectEventArgs Members
---
The **CustomFormatObjectEventArgs** class declares properties specific to the [ObjectFormatter.CustomFormatObject](xref:DevExpress.Persistent.Base.ObjectFormatter.CustomFormatObject) event. This event is designed to perform the custom processing of the strings passed to the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method.

This class is inherited from the **HandledEventArgs** class. So, you can set the handler's **Handled** parameter to **true**, to prevent the default processing of the string passed to the **Format** method.