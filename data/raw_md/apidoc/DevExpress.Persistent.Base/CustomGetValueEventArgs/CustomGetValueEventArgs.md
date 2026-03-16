---
uid: DevExpress.Persistent.Base.CustomGetValueEventArgs
name: CustomGetValueEventArgs
type: Class
summary: Arguments passed to the [ObjectFormatter.CustomGetValue](xref:DevExpress.Persistent.Base.ObjectFormatter.CustomGetValue) event.
syntax:
  content: 'public class CustomGetValueEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.Persistent.Base.CustomGetValueEventArgs._members
  altText: CustomGetValueEventArgs Members
---
The **CustomGetValueEventArgs** class declares properties specific to the [ObjectFormatter.CustomGetValue](xref:DevExpress.Persistent.Base.ObjectFormatter.CustomGetValue) event. This event is designed to supply a custom value that will replace the format item in the string processed by the [ObjectFormatter.Format](xref:DevExpress.Persistent.Base.ObjectFormatter.Format*) method.

This class is inherited from the **HandledEventArgs** class. So, you can set the handler's **Handled** parameter to **true**. In this instance, if you have not provided a custom value, the format item will be removed from the reulting string.