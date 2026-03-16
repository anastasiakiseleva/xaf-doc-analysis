---
uid: DevExpress.Persistent.Base.General.ISupportNotifications.AlarmTime
name: AlarmTime
type: Property
summary: Specifies the time when the notification should be triggered.
syntax:
  content: DateTime? AlarmTime { get; set; }
  parameters: []
  return:
    type: System.Nullable{System.DateTime}
    description: A [Nullable](xref:System.Nullable`1)\<[](xref:System.DateTime)> value that specifies the time when the notification should be triggered.
seealso: []
---
Refer to the [How to: Use Notifications with a Custom Business Class (Implement ISupportNotifications) ](xref:113689) example to see how to implement this property.
> [!IMPORTANT]
> The notification is disabled when this property is set to `null`.