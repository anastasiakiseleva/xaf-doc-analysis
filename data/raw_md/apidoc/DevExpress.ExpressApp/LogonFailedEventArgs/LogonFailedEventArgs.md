---
uid: DevExpress.ExpressApp.LogonFailedEventArgs
name: LogonFailedEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.LogonFailed](xref:DevExpress.ExpressApp.XafApplication.LogonFailed) event.
syntax:
  content: 'public class LogonFailedEventArgs : HandledEventArgs'
seealso:
- linkId: DevExpress.ExpressApp.LogonFailedEventArgs._members
  altText: LogonFailedEventArgs Members
---
The **LogonFailedEventArgs** class declares properties specific to the [XafApplication.LogonFailed](xref:DevExpress.ExpressApp.XafApplication.LogonFailed) event. This event is designed to process the exception that failed at the logon to the application. Use the [LogonFailedEventArgs.LogonParameters](xref:DevExpress.ExpressApp.LogonFailedEventArgs.LogonParameters) and [LogonFailedEventArgs.Exception](xref:DevExpress.ExpressApp.LogonFailedEventArgs.Exception) properties to specify the logon parameters and the exception that was raised when logging with these parameters.