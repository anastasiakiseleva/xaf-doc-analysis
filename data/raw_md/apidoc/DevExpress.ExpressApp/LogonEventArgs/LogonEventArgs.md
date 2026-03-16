---
uid: DevExpress.ExpressApp.LogonEventArgs
name: LogonEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.LoggingOn](xref:DevExpress.ExpressApp.XafApplication.LoggingOn) and [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) events.
syntax:
  content: 'public class LogonEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.LogonEventArgs._members
  altText: LogonEventArgs Members
---
The **LogonEventArgs** class declares the [LogonEventArgs.LogonParameters](xref:DevExpress.ExpressApp.LogonEventArgs.LogonParameters) property specific to the [XafApplication.LoggingOn](xref:DevExpress.ExpressApp.XafApplication.LoggingOn) and [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) events. These events are designed to execute custom code before and after clicking the Logon button on a logon Window. The **LogonParameters** property allows accessing the current logon parameters.