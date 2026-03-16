---
uid: "113690"
seealso:
- linkId: "113692"
- linkId: "113693"
- linkId: "113689"
- linkId: "113687"
- linkId: "113696"
title: Notifications Module Overview
owner: Ekaterina Kiseleva
---
# Notifications Module Overview

The Notifications module allows you to display reminders for [scheduler](xref:112811) appointments or any custom business object. At the required time, a popup window appears automatically. In this window, a user can view, cancel, or delay alerts.

![XAF ASP.NET Core Blazor: notification alert window, DevExpress](~/images/notifications_alertwindow117584.png)

## Notifications Module Components

| Platform | Module |
| -------- | ------ |
| Platform-agnostic | [](xref:DevExpress.ExpressApp.Notifications.NotificationsModule) |
| ASP.NET Core Blazor | `NotificationsBlazorModule` |
| Windows Forms | `NotificationsWindowsFormsModule` |

## Notifications Module Capabilities

The module tracks changes in any business object that supports the [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) interface, such as `Event` objects that ship with the [Built-in Business Class Library](xref:112571) for Entity Framework Core and XPO. For more information refer to the following topic: [](xref:113687).

You can also implement the [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) interface in any custom business object as described in the following topic: [](xref:113689).

### How to Specify the Notification Refresh Frequency

ASP.NET Core Blazor
:   Use the @DevExpress.ExpressApp.Blazor.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Blazor.ApplicationBuilder.IBlazorApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Blazor.NotificationsOptions}) method to pass the new value to the [NotificationsOptionsBase.NotificationsRefreshInterval](xref:DevExpress.ExpressApp.Notifications.NotificationsOptionsBase.NotificationsRefreshInterval) property.

Windows Forms
:   Use the @DevExpress.ExpressApp.Win.ApplicationBuilder.NotificationsApplicationBuilderExtensions.AddNotifications(DevExpress.ExpressApp.ApplicationBuilder.IModuleBuilder{DevExpress.ExpressApp.Win.ApplicationBuilder.IWinApplicationBuilder},System.Action{DevExpress.ExpressApp.Notifications.Win.NotificationsOptions}) method to pass the new value to the [NotificationsOptionsBase.NotificationsRefreshInterval](xref:DevExpress.ExpressApp.Notifications.NotificationsOptionsBase.NotificationsRefreshInterval) property.
	
### Notifications

XAF invokes the [Notifications window](xref:113692) automatically at the required time.

> [!IMPORTANT]
> The `Event` business class has the `Reminder` property that is hidden to preserve the `Event` Detail View layouts in existing applications. However, this property should be visible if you intend to use event notifications. For more information on how to make the property visible, refer to the following topic: [](xref:113687).

To customize notification view parameters and notification list processing, handle the corresponding events:

* [NotificationsController.CustomizeNotificationViewParameters](xref:DevExpress.ExpressApp.Notifications.NotificationsController.CustomizeNotificationViewParameters)
* [NotificationsController.CustomProcessNotifications](xref:DevExpress.ExpressApp.Notifications.NotificationsController.CustomProcessNotifications)

The module adds the **Show Notifications** Action in the following locations:

* ASP.NET Core Blazor application's page header toolbar (top-right corner)
* Windows Forms application's status bar (bottom-right corner)

This action allows users to re-invoke the Notifications window to see the active or all notifications. The notifications count is displayed next to this Action or in the tooltip.

ASP.NET Core Blazor

:   ![|XAF Windows Forms, Show Postponed Notifications Action, DevExpress](~/images/xaf-notification-postponed-blazor-devexpress.png)
	
Windows Forms:

:   ![|XAF Windows Forms, Show Postponed Notifications Action, DevExpress](~/images/notifications_showpostponedwin117581.png)

> [!TIP]
> To place a custom Action near the **Show Notifications** Action, set the Action's category to "Notifications". For more information, refer to the following topics:
> * [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category)
> * [IModelAction.Category](xref:DevExpress.ExpressApp.Model.IModelAction.Category)

## Add the Notifications Module to Your Application

### Template Kit

You can add the Notifications module to your application when you use the [Template Kit](xref:405447) to create a new XAF solution. Select the module in the **Additional Modules** section.

### Existing Application

For step-by-step instructions of how to add the Notifications module to your application, refer to the following topic: [](xref:404940).