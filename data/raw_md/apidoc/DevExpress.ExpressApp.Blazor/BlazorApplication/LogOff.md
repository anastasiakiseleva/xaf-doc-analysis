---
uid: DevExpress.ExpressApp.Blazor.BlazorApplication.LogOff
name: LogOff()
type: Method
summary: Performs the ASP.NET Core Blazor application logout.
syntax:
  content: public override void LogOff()
seealso: []
---
Triggers the following events:

- [XafApplication.LoggingOff](xref:DevExpress.ExpressApp.XafApplication.LoggingOff) - handle this event to cancel the log off process.
- [XafApplication.LoggedOff](xref:DevExpress.ExpressApp.XafApplication.LoggedOff) - handle this event to be notified when a user has logged off. 

The [](xref:DevExpress.ExpressApp.SystemModule.LogoffController) Controller uses this method.
