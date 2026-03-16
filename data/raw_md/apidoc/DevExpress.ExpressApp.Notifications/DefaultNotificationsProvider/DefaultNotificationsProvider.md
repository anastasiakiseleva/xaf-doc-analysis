---
uid: DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider
name: DefaultNotificationsProvider
type: Class
summary: A [Notifications Provider](xref:113693) that collects notifications from business objects that support the [](xref:DevExpress.Persistent.Base.General.ISupportNotifications) interface. Types that have descendants are ignored to avoid duplicate notifications.
syntax:
  content: 'public class DefaultNotificationsProvider : INotificationsProvider, IDisposable, IObjectSpacesCache'
seealso:
- linkId: DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider._members
  altText: DefaultNotificationsProvider Members
---
To get a **DefaultNotificationsProvider** instance, use the [NotificationsModule.DefaultNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.DefaultNotificationsProvider) property. An example is provided in the [How to: Show Notifications to a Specific User](xref:113696) topic.

You can create a custom provider by implementing the [](xref:DevExpress.Persistent.Base.General.INotificationsProvider) interface or inheriting the **DefaultNotificationsProvider** or [](xref:DevExpress.ExpressApp.Scheduler.NotificationsProvider). To register a provider, use the [NotificationsService.RegisterNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsService.RegisterNotificationsProvider(DevExpress.Persistent.Base.General.INotificationsProvider)) method.

> [!TIP]
> You can use [DefaultNotificationsProvider.NotificationTypesInfo](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider.NotificationTypesInfo) property to customize the list of business object types supported by [](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider).