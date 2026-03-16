---
uid: DevExpress.ExpressApp.SystemModule.DialogController.WindowTemplateChanged
name: WindowTemplateChanged
type: Event
summary: Occurs after setting a [Template](xref:112609) for the Dialog Controller's pop-up [Window](xref:112608).
syntax:
  content: public event EventHandler WindowTemplateChanged
seealso: []
---
Handle the **WindowTemplateChanged** event to customize the current pop-up Window's Template ([Frame.Template](xref:DevExpress.ExpressApp.Frame.Template)). For details on customizing a Template, refer to the [Template Customization](xref:112696) topic.

To make the application load a custom, rather than a default Template, handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event. If you need to customize a Template and apply your customization each time the Template is displayed, handle the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event.