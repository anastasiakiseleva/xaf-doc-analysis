---
uid: DevExpress.ExpressApp.Notifications.NotificationsOptionsBase.NotificationsStartDelay
name: NotificationsStartDelay
type: Property
summary: Specifies the delay after the application start and before the initial [Notifications window](xref:113692) display.
syntax:
  content: public TimeSpan NotificationsStartDelay { get; set; }
  parameters: []
  return:
    type: System.TimeSpan
    defaultValue: 5 seconds
    description: A @System.TimeSpan value that specifies the delay after the application starts and before the initial Notifications window is displayed.
seealso: []
---
The following example demonstrates how to specify this property:

# [ASP.NET Core Blazor](#tab/tabid-blazor)

[!include[blazor-notifications-options](~/templates/blazor-notifications-options.md)]

# [Windows Forms](#tab/tabid-win)
[!include[winforms-notifications-options](~/templates/winforms-notifications-options.md)]
***