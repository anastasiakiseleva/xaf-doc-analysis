---
uid: DevExpress.Persistent.Base.General.ISupportNotifications
name: ISupportNotifications
type: Interface
summary: Declares members of business objects that support the [Notifications Module](xref:113688) functionality.
syntax:
  content: public interface ISupportNotifications
seealso:
- linkId: DevExpress.Persistent.Base.General.ISupportNotifications._members
  altText: ISupportNotifications Members
- linkId: "113690"
---
Implement this interface in a business class if you need to display notifications associated with these class instances. Refer to the [How to: Use Notifications with a Custom Business Class (Implement ISupportNotifications) ](xref:113689) topic to see an example.

The built-in class that supports the **ISupportNotifications** is an **Event** provided by the [Built-in Business Class Library](xref:112571) for both Entity Framework and XPO.

> [!NOTE]
> Business object types that support **ISupportNotifications**, but have descendants, are ignored by the Notifications Module. This is done to avoid duplicate notifications for each type in the inheritance hierarchy. You can add required types manually using the [DefaultNotificationsProvider.NotificationTypesInfo](xref:DevExpress.ExpressApp.Notifications.DefaultNotificationsProvider.NotificationTypesInfo) property.