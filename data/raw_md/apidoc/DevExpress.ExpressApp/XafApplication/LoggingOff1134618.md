---
uid: DevExpress.ExpressApp.XafApplication.LoggingOff
name: LoggingOff
type: Event
summary: Occurs when a user clicks the **Log Off** button.
syntax:
  content: public event EventHandler<LoggingOffEventArgs> LoggingOff
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LoggedOff
- linkId: DevExpress.ExpressApp.XafApplication.LoggedOn
- linkId: DevExpress.ExpressApp.XafApplication.LoggingOn
---
Handle this event to execute custom code before a user has logged off. If the log off process has been initiated by a user (via the Log Off [LogoffController.LogoffAction](xref:DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction)), the [LoggingOffEventArgs.CanCancel](xref:DevExpress.ExpressApp.LoggingOffEventArgs.CanCancel) property returns `true`, and you can cancel the process by setting the handler's `Cancel` parameter to `true`.
