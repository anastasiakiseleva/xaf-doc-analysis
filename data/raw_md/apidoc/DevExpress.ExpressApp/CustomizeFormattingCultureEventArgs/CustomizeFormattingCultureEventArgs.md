---
uid: DevExpress.ExpressApp.CustomizeFormattingCultureEventArgs
name: CustomizeFormattingCultureEventArgs
type: Class
summary: Arguments passed to the [XafApplication.CustomizeFormattingCulture](xref:DevExpress.ExpressApp.XafApplication.CustomizeFormattingCulture) event.
syntax:
  content: 'public class CustomizeFormattingCultureEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.CustomizeFormattingCultureEventArgs._members
  altText: CustomizeFormattingCultureEventArgs Members
---
The **CustomizeFormattingCulture** event occurs after a formatting culture has been set internally. Handle this event to set the required formatting culture for the Thread.CurrentThread.CurrentCulture object.