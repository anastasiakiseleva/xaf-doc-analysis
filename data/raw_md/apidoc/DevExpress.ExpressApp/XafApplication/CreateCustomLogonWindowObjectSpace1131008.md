---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomLogonWindowObjectSpace
name: CreateCustomLogonWindowObjectSpace
type: Event
summary: Occurs when creating an Object Space for a Logon Window's [Detail View](xref:112611).
syntax:
  content: public event EventHandler<CreateCustomLogonWindowObjectSpaceEventArgs> CreateCustomLogonWindowObjectSpace
seealso: []
---
Handle this event to specify a custom Object Space for a Logon Window's Detail View. Pass the required Object Space as the handler's **ObjectSpace** parameter. To see an example of using this event, refer to the [](xref:404264) section.

> [!NOTE]
> The **CreateCustomLogonWindowObjectSpace** event is not raised when the logon form is not created, e.g., when the [AuthenticationBase.AskLogonParametersViaUI](xref:DevExpress.ExpressApp.Security.AuthenticationBase.AskLogonParametersViaUI) property is set to **false**.
