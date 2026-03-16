---
uid: DevExpress.ExpressApp.MessageOptions.Duration
name: Duration
type: Property
summary: Specifies the duration of the WinForms [Alert](xref:5395) and ASP.NET Core Blazor notification in milliseconds.
syntax:
  content: public int Duration { get; set; }
  parameters: []
  return:
    type: System.Int32
    description: An integer that specifies the duration of the WinForms **Alert** and ASP.NET Core Blazor notification (in milliseconds).
seealso: []
---
A notification message window is closed when this duration ends or when a user clicks the message.

This property has no effect in the following cases:
- in WinForms applications with [Flyout](xref:114568) or [Toast](xref:17020) notifications;
- in Blazor applications on mobile devices.

The default value is `3000`. If the **Duration** is set to `int.MaxValue`, the notification does not close automatically. 

- **In ASP.NET Core Blazor applications:** if the **Duration** is less than `0`, the default value is used. Also, if a user hovers the mouse pointer over a notification message window, the window does not close despite the **Duration** value.
- **In WinForms applications:** if the **Duration** is less than `0`, the notification message closes immediately.
