---
uid: DevExpress.ExpressApp.Scheduler.SchedulerModuleBase.CustomizeReminderEventTypes
name: CustomizeReminderEventTypes
type: Event
summary: Occurs when the business object types that supply notifications are collected.
syntax:
  content: public event EventHandler<NotificationEventTypesEventArgs> CustomizeReminderEventTypes
seealso: []
---
Handle this event to customize the collected types list. By default, this list includes all business object types that support the **IReminderEvent** interface (e.g., the **Event** type from the [Business Class Library](xref:112571) and its descendants).