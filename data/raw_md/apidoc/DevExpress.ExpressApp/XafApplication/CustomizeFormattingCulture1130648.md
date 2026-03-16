---
uid: DevExpress.ExpressApp.XafApplication.CustomizeFormattingCulture
name: CustomizeFormattingCulture
type: Event
summary: Occurs after a formatting culture has been set internally.
syntax:
  content: public event EventHandler<CustomizeFormattingCultureEventArgs> CustomizeFormattingCulture
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CustomizeLanguage
- linkId: "112595"
---
In XAF applications, formatting options for information like currency, numbers, and dates are not related to the application's language. The formatting options that are set in the current user's operating system or passed by the Internet browser are used. Handle this event to set the required formatting culture for the [Thread.CurrentCulture](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.currentculture#System_Threading_Thread_CurrentCulture) object. To get the culture currently set, use the handler's [CustomizeFormattingCultureEventArgs.FormattingCulture](xref:DevExpress.ExpressApp.CustomizeFormattingCultureEventArgs.FormattingCulture) property. In addition, you can get the language which is set in the user's operating system or passed by the Internet browser. For this purpose, use the handler's [CustomizeFormattingCultureEventArgs.UserLanguageName](xref:DevExpress.ExpressApp.CustomizeFormattingCultureEventArgs.UserLanguageName) property. To get the language which is currently set for the [](xref:DevExpress.ExpressApp.Model.IModelApplication) node's [IModelApplication.PreferredLanguage](xref:DevExpress.ExpressApp.Model.IModelApplication.PreferredLanguage) property, use the handler's [CustomizeFormattingCultureEventArgs.PreferredLanguageName](xref:DevExpress.ExpressApp.CustomizeFormattingCultureEventArgs.PreferredLanguageName) property.

To see an example of handling this event, refer to the [Culture-Specific Formatting](xref:113299) topic.
