---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomTemplate
name: CreateCustomTemplate
type: Event
summary: Occurs when creating a [Template](xref:112609).
syntax:
  content: public event EventHandler<CreateCustomTemplateEventArgs> CreateCustomTemplate
seealso:
- linkId: "112696"
- linkId: "112618"
- linkId: "113706"
---
In Windows Forms and ASP.NET Core Blazor applications, this event is raised when a [Window](xref:112608) is created. Handle this event to create a custom [Template](xref:112609) for this Window. Use the handler's [CreateCustomTemplateEventArgs.Context](xref:DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Context) parameter to create a custom Template for a particular context. For details, refer to the [Template Customization](xref:112696), [How To: Create a Custom Blazor Application Template](xref:403452), [How to: Create a Custom WinForms Ribbon Template](xref:112618) and [How to: Create a Custom WinForms Standard Template ](xref:113706) topics.

The @DevExpress.ExpressApp.XafApplication.CreateCustomTemplate event is triggered at an XAF WinForms application's startup, once or twice. This depends on the conditions below.

|  | When the Event is Triggered | When to Handle the Event |
| --- | --- | --- |
| 1 | On the application's startup, **before** the [Application Model](xref:112580) loads. |  To create custom [Logon](xref:113151) or Main Window templates that do not require the Application Model. If you handle the event at this time, the application creates templates in a [separate thread](https://supportcenter.devexpress.com/ticket/details/bc4941/winforms-the-winapplication-setup-method-runs-in-a-separate-thread) and demonstrates a reduced startup time. |
| 2 | On the application's startup, **after** the Application Model loads - if no custom templates were passed the first time the event was triggered. | To get Logon or Main Window templates created the first time the event was triggered or to create templates that depend on the Application Model for their settings. |
