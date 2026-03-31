---
uid: "113693"
seealso:
- linkId: "113689"
- linkId: "113687"
- linkId: "113696"
title: Notifications Service and Notifications Providers
---
# Notifications Service and Notifications Providers

This topic describes the internal infrastructure of the [Notifications Module](xref:113690) and explains how to customize its default behavior.

[](xref:DevExpress.ExpressApp.Notifications.NotificationsService) is an object that the [](xref:DevExpress.ExpressApp.Notifications.NotificationsModule) uses to process notifications. To access the service, use the module's [NotificationsModule.NotificationsService](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.NotificationsService) property.

Notifications Providers collect notifications from [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) business objects. The following built-in Notification Providers are available:

| Platform | Provider | Description |
| --- | --- | --- |
| ASP.NET Core Blazor | `DevExpress.ExpressApp.Scheduler.Blazor.Notifications.SchedulerNotificationsProvider` | Collects notifications from Scheduler events. Implemented in the [Scheduler Module](xref:112811). |
| Windows Forms | [](xref:DevExpress.ExpressApp.Scheduler.NotificationsProvider) | Collects notifications from Scheduler events. Implemented in the [Scheduler Module](xref:112811). |
| All platforms | [](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider) | Collects notifications from any other `ISupportNotifications` objects. Types that have descendants are ignored. |

To create a custom provider, implement the [](xref:DevExpress.Persistent.Base.General.INotificationsProvider) interface or inherit one of the built-in providers.

To register a provider, use the [NotificationsService.RegisterNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsService.RegisterNotificationsProvider(DevExpress.Persistent.Base.General.INotificationsProvider)) method.

