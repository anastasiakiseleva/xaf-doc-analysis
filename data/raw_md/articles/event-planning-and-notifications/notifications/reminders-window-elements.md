---
uid: "113692"
seealso:
- linkId: "113689"
- linkId: "113687"
- linkId: "113696"
title: Notifications Window Elements
---
# Notifications Window Elements

This topic describes the UI and functionality of the Notifications window that ships with the [Notifications Module](xref:113690). The window is a pop-up dialog that XAF invokes each time it has to send a notification to the user.

ASP.NET Core Blazor

:   ![XAF ASP.NET Core Blazor Notifications Window, DevExpress](~/images/notifications_alertwindow117584.png)

Windows Forms
:   ![XAF Windows Forms Notifications Window, DevExpress](~/images/xaf-notifications-window-winforms-devexpress.png)

The Notifications window contains the **NotificationsObject_DetailView** Detail View. You can [adjust the layout](xref:112817) for this view in the [Model Editor](xref:112582).

The Detail View contains a nested **NotificationsObject_Notifications_ListView** List View that displays the notification list. If you click a record in the list, XAF invokes the Detail View of the associated business object (for example, `Event`).

## Actions

Buttons available in the Notifications window are [Actions](xref:112622) supplied by `NotificationsDialogViewController`.

| Action | Description | Controller |
|---|---|---|
| **DismissAll** | Dismisses all active notifications. This Action is hidden. To display it, set the [NotificationsModule.ShowDismissAllAction](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.ShowDismissAllAction) property to `true`. | `NotificationsDialogViewController` |
| **Dismiss** | Dismisses selected notification(s). | `NotificationsDialogViewController` |
| **Refresh** | Refreshes the notifications list. This Action is hidden. To display it, set the [NotificationsModule.ShowRefreshAction](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.ShowRefreshAction) property to `true`. | `NotificationsDialogViewController` |
| **Snooze** | Re-schedules the selected notification(s) for the time span chosen in the **Snooze time** Lookup Property Editor. | `NotificationsDialogViewController` |
| **SnoozeList** | Supplies a list of predefined snooze time span values. In ASP.NET Core Blazor, replaces the **Snooze** Action. | `SnoozeListActionController` |

## Combo Boxes

In XAF Windows Forms applications, the **Snooze time** combo box contains predefined time span values. Use it to specify the delay in the **Snooze** Action.

The **Notifications State** combo box specifies a filter applied to visible notifications:
* Active
* Postponed
* All

## Checkboxes

The **Show Notifications Window** checkbox controls whether XAF invokes the Notifications window automatically. If you uncheck it, the window does not appear, but XAF still updates the notifications count next to the **Show Notifications** Action.

To manually invoke the Notifications window, click **Show Notifications**.

> [!NOTE]
> In XAF ASP.NET Core Blazor applications, the checkbox is hidden.

To control the Notifications window visibility in code, use the  [NotificationsOptionsBase.ShowNotificationsWindow](xref:DevExpress.ExpressApp.Notifications.NotificationsOptionsBase.ShowNotificationsWindow) property.

> [!TIP]
> To learn how to localize the Notifications window, refer to the following topic: [](xref:113691).