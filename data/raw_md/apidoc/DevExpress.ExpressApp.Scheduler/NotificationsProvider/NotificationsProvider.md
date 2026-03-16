---
uid: DevExpress.ExpressApp.Scheduler.NotificationsProvider
name: NotificationsProvider
type: Class
summary: A [Notifications Provider](xref:113693) that collects notifications from the **Event** class from the [Business Classes Library](xref:112571) (both for Entity Framework and XPO).
syntax:
  content: 'public class NotificationsProvider : IDisposable, ISchedulerNotificationsProvider, INotificationsProvider, IObjectSpacesCache'
seealso:
- linkId: DevExpress.ExpressApp.Scheduler.NotificationsProvider._members
  altText: NotificationsProvider Members
---
To get a `NotificationsProvider` instance, use the [SchedulerModuleBase.NotificationsProvider](xref:DevExpress.ExpressApp.Scheduler.SchedulerModuleBase.NotificationsProvider) property. In XAF ASP.NET Core Blazor applications, you can access `ISchedulerNotificationsProvider` through [Dependency Injection](xref:404402).

To create a custom provider, you can implement the [](xref:DevExpress.Persistent.Base.General.INotificationsProvider) interface or inherit either `NotificationsProvider` or [](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider). To register a provider, use the [NotificationsService.RegisterNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsService.RegisterNotificationsProvider(DevExpress.Persistent.Base.General.INotificationsProvider)) method.