---
uid: DevExpress.ExpressApp.XafApplication.LogonFailed
name: LogonFailed
type: Event
summary: Occurs when the logon fails.
syntax:
  content: public event EventHandler<LogonFailedEventArgs> LogonFailed
seealso: []
---
Handle this event to process the exception that failed the logon. This exception is available via the handler's [LogonFailedEventArgs.Exception](xref:DevExpress.ExpressApp.LogonFailedEventArgs.Exception) parameter. You can also access the current logon parameters via the handler's [LogonFailedEventArgs.LogonParameters](xref:DevExpress.ExpressApp.LogonFailedEventArgs.LogonParameters) parameter.

To avoid throwing the exception, set the handler's **Handled** parameter to **true**.