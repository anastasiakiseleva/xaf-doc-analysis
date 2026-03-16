---
uid: DevExpress.ExpressApp.XafApplication.LoggingOn
name: LoggingOn
type: Event
summary: Occurs when the **Logon** button on the logon Window is clicked.
syntax:
  content: public event EventHandler<LogonEventArgs> LoggingOn
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LoggedOn
- linkId: DevExpress.ExpressApp.XafApplication.LoggingOff
- linkId: DevExpress.ExpressApp.XafApplication.LoggedOff
---
Handle this event to execute custom code before logon is peformed. Use the handler's [LogonEventArgs.LogonParameters](xref:DevExpress.ExpressApp.LogonEventArgs.LogonParameters) parameter to specify the current logon parameters.