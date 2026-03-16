---
uid: DevExpress.ExpressApp.Notifications.NotificationsController.CustomProcessNotifications
name: CustomProcessNotifications
type: Event
summary: Occurs before XAF invokes a [notification](xref:113690) window.
syntax:
  content: public event EventHandler<NotificationItemsEventArgs> CustomProcessNotifications
seealso: []
---
Handle the `CustomProcessNotifications` event to apply custom processing to the notification list received from the [Notifications Service](xref:113693). To suppress the default logic, set the `Handled` property to `true` and call the [NotificationsController.RefreshNotifications](xref:DevExpress.ExpressApp.Notifications.NotificationsController.RefreshNotifications) method to display the notification list after XAF runs your custom logic.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Notifications;
using DevExpress.Persistent.Base.General;

namespace MySolution.Module.Controllers;
public class MyController : WindowController {
    protected override void OnActivated() {
        //...
        var controller = Frame.GetController<NotificationsController>();
        controller?.CustomProcessNotifications += Controller_CustomProcessNotifications;
    }
    private void Controller_CustomProcessNotifications(object sender, DevExpress.Persistent.Base.General.NotificationItemsEventArgs e) {
        foreach(INotificationItem item in e.NotificationItems) {
            //...
        }
        e.Handled = true;
        ((NotificationsController)sender).RefreshNotifications();
    }
}
```