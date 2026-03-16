---
uid: DevExpress.ExpressApp.Notifications.NotificationsController.CustomizeNotificationViewParameters
name: CustomizeNotificationViewParameters
type: Event
summary: Occurs before XAF invokes a [notification](xref:113690) window.
syntax:
  content: public event EventHandler<CustomizeShowViewParametersEventArgs> CustomizeNotificationViewParameters
seealso: []
---
Handle the `CustomizeNotificationViewParameters` event to customize the notification view parameters passed as the event's [CustomizeShowViewParametersEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.SystemModule.CustomizeShowViewParametersEventArgs.ShowViewParameters) argument. The argument type is [](xref:DevExpress.ExpressApp.ShowViewParameters).