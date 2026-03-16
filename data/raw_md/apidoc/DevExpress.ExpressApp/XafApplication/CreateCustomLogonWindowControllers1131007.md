---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomLogonWindowControllers
name: CreateCustomLogonWindowControllers
type: Event
summary: Occurs when creating [Controllers](xref:112621) for a Logon Window.
syntax:
  content: public event EventHandler<CreateCustomLogonWindowControllersEventArgs> CreateCustomLogonWindowControllers
seealso: []
---
A limited set of required built-in Controllers is activated for a Logon Window (e.g., **FillActionContainersController**,  **DiagnosticInfoController**, Controllers of the [Validation](xref:113684) and [Conditional Appearance](xref:113286) modules, etc.). Handle this event to create the required Controllers in addition to the system's Controllers. Add these Controllers to the list passed as the handler's **Controllers** parameter. An example of handling the **CreateCustomLogonWindowControllers** event is provided in the [Logon Form Controllers and Actions](xref:113475) topic.