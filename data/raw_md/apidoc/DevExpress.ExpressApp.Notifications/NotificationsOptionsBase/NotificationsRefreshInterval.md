---
uid: DevExpress.ExpressApp.Notifications.NotificationsOptionsBase.NotificationsRefreshInterval
name: NotificationsRefreshInterval
type: Property
summary: Specifies how often XAF refreshes notifications.
syntax:
  content: public TimeSpan NotificationsRefreshInterval { get; set; }
  parameters: []
  return:
    type: System.TimeSpan
    defaultValue: 5 minutes
    description: A @System.TimeSpan value that specifies the time that passes before XAF refreshes notifications again.
seealso: []
---

The following example demonstrates how to specify this property:

# [ASP.NET Core Blazor](#tab/tabid-blazor)

[!include[blazor-notifications-options](~/templates/blazor-notifications-options.md)]

# [Windows Forms](#tab/tabid-win)
[!include[winforms-notifications-options](~/templates/winforms-notifications-options.md)]
***