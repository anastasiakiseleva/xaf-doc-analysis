---
uid: DevExpress.ExpressApp.LoggingOffEventArgs
name: LoggingOffEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.LoggingOff](xref:DevExpress.ExpressApp.XafApplication.LoggingOff) event.
syntax:
  content: 'public class LoggingOffEventArgs : CancelEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.LoggingOffEventArgs._members
  altText: LoggingOffEventArgs Members
---
The **LoggingOff** event occurs when a user clicks the **Log Off** button. If the log off process has been initiated by a user (via the [LogoffController.LogoffAction](xref:DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction)), the [LoggingOffEventArgs.CanCancel](xref:DevExpress.ExpressApp.LoggingOffEventArgs.CanCancel) property returns **true**, and you can cancel the process by setting the **LoggingOff** event handler's **Cancel** parameter to **true**.