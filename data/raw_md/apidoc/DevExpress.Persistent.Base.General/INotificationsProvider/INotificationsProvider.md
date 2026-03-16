---
uid: DevExpress.Persistent.Base.General.INotificationsProvider
name: INotificationsProvider
type: Interface
summary: Declares members implemented by [Notifications Providers](xref:113693).
syntax:
  content: public interface INotificationsProvider
seealso:
- linkId: DevExpress.Persistent.Base.General.INotificationsProvider._members
  altText: INotificationsProvider Members
---
You can create a custom provider by implementing the **INotificationsProvider** interface. To register a provider, use the [NotificationsService.RegisterNotificationsProvider](xref:DevExpress.ExpressApp.Notifications.NotificationsService.RegisterNotificationsProvider(DevExpress.Persistent.Base.General.INotificationsProvider)) method.