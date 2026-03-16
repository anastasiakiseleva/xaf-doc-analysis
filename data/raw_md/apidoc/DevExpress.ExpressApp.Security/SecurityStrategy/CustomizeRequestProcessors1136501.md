---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.CustomizeRequestProcessors
name: CustomizeRequestProcessors
type: Event
summary: Occurs after Permission Request Processors are registered.
syntax:
  content: public event EventHandler<CustomizeRequestProcessorsEventArgs> CustomizeRequestProcessors
seealso: []
---
Handle this event to register your custom processor. Use the event's  **Permissions** parameter to access current permissions. Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example.