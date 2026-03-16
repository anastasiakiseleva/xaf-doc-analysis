---
uid: DevExpress.ExpressApp.Notifications.NotificationsModule
name: NotificationsModule
type: Class
summary: The XAF module contained in the _DevExpress.ExpressApp.Notifications.v<:xx.x:>.dll_ assembly.
syntax:
  content: 'public sealed class NotificationsModule : ModuleBase, INotificationsServiceOwner'
seealso:
- linkId: DevExpress.ExpressApp.Notifications.NotificationsModule._members
  altText: NotificationsModule Members
- linkId: "113690"
- linkId: "113687"
- linkId: "113689"
---
This module implements the base [Notifications](xref:113688) functionality. There are three platform-specific module classes that should be used with `NotificationsModule`:
* `NotificationsBlazorModule` shipped with _DevExpress.ExpressApp.Notifications.Blazor.v<:xx.x:>.dll_
* `NotificationsWindowsFormsModule` shipped with _DevExpress.ExpressApp.Notifications.Win.v<:xx.x:>.dll_
* `NotificationsAspNetModule` shipped with _DevExpress.ExpressApp.Notifications.Web.v<:xx.x:>.dll_

The `NotificationsModule` module constructor creates a [](xref:DevExpress.ExpressApp.Notifications.NotificationsService) object and assigns it to the [NotificationsModule.NotificationsService](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.NotificationsService) property. The [NotificationsModule.NotificationsRefreshInterval](xref:DevExpress.ExpressApp.Notifications.NotificationsModule.NotificationsRefreshInterval) property sets the notifications refresh frequency (the default value is 5 minutes).