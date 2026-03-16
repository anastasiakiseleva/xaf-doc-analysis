---
uid: DevExpress.ExpressApp.XafApplication.LoggedOn
name: LoggedOn
type: Event
summary: Occurs after an end-user has logged on.
syntax:
  content: public event EventHandler<LogonEventArgs> LoggedOn
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.LoggingOn
- linkId: DevExpress.ExpressApp.XafApplication.LoggingOff
- linkId: DevExpress.ExpressApp.XafApplication.LoggedOff
---
Handle this event to execute custom code after a logon has been performed, the [](xref:DevExpress.ExpressApp.SecuritySystem) object is initialized, the logon parameters have been saved and user model differences are loaded.

For an example, see [](xref:113696).

> [!NOTE]
> Exceptions that occur within the **LoggedOn** event handler are not handled by [](xref:DevExpress.ExpressApp.XafApplication) automatically, because it is too late to cancel a logon when this event occurs.  So, it is recommended that you wrap your handler code into [try-catch](https://learn.microsoft.com/en-us/dotnet/articles/csharp/language-reference/keywords/try-catch) blocks.
