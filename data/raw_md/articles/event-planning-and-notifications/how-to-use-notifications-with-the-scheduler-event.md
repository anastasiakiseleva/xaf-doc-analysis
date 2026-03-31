---
uid: "113687"
seealso:
- linkId: "113689"
- linkId: "113696"
- linkId: "404214"
title: 'How to: Use Notifications with the Scheduler Event'
---
# How to: Use Notifications with the Scheduler Event

This topic demonstrates how to use the [Notifications](xref:113688) and [Scheduler](xref:112812) Modules together with the `Event` class from the [business class library](xref:112571). You can use the same technique with a custom `Event` descendant.

> [!NOTE]
> [!include[Watch_Video](~/templates/watch_video111195.md)] [DevExpress XAF: Notifications](https://www.youtube.com/watch?v=l6XbnPEUPCU).
>
> Although the video demonstrates an older XAF version, the scenario remains the same.

To enable notifications, add the Notifications module to your application as described in the following topic: [](xref:404940).

The **`Event`** business class has the `Reminder` property. It is hidden to preserve the `Event` Detail View layouts in existing applications. Adjust the **Event_DetailView** layout to make this property visible. For more information, refer to the following topic: [View Items Layout Customization](xref:112817).

If you use a custom `Event` descendant, you should make the `Reminder` property visible in the descendant's Detail View too.

With notifications enabled, users can set reminders for each `Event` so that XAF displays a pop-up window before an event starts. You can specify the time between the reminder and the event's **Start Date/Time** in the `Reminder` property of the `Event` class.

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor, Reminders, DevExpress](~/images/xaf-blazor-appointment-reminder-devexpress.png)

Windows Forms
:   ![XAF Windows Forms, Reminders, DevExpress](~/images/howto_reminders_4117564.png)
> [!TIP]
> If the `Reminder` property is set to "0 minutes", the Notifications window appears at the event's start time.

Run the application and create a new `Event` in the past (the **Start Date/Time** should be earlier than the current time). Select "5 minutes" in the **Reminder** drop-down. Save the event and the **Reminder** window will be shown in less than 10 seconds.

ASP.NET Core Blazor
:   ![|XAF ASP.NET Core Blazor, Notification Window, DevExpress](~/images/howto_reminders_5117565.png)

Windows Forms
:   ![XAF Windows Forms, Notification Window, DevExpress](~/images/xaf-winforms-notification-window-devexpress.png)