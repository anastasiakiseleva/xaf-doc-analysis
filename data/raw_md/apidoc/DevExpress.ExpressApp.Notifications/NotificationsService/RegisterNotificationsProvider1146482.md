---
uid: DevExpress.ExpressApp.Notifications.NotificationsService.RegisterNotificationsProvider(DevExpress.Persistent.Base.General.INotificationsProvider)
name: RegisterNotificationsProvider(INotificationsProvider)
type: Method
summary: Registers the specified [Notifications Provider](xref:113693)
syntax:
  content: public void RegisterNotificationsProvider(INotificationsProvider notificationProvider)
  parameters:
  - id: notificationProvider
    type: DevExpress.Persistent.Base.General.INotificationsProvider
    description: An [](xref:DevExpress.Persistent.Base.General.INotificationsProvider) object to register.
seealso: []
---
Types that are handled by the passed provider ([INotificationsProvider.NotificationTypesInfo](xref:DevExpress.Persistent.Base.General.INotificationsProvider.NotificationTypesInfo)) are excluded from the [DefaultNotificationsProvider.NotificationTypesInfo](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider.NotificationTypesInfo) list to avoid conflicts with the [NotificationsModule.DefaultNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.DefaultNotificationsProvider).

To unregister a provider, use the [NotificationsService.UnregisterNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsService.UnregisterNotificationsProvider(DevExpress.Persistent.Base.General.INotificationsProvider)) method.