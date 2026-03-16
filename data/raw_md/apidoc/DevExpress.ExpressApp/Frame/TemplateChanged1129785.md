---
uid: DevExpress.ExpressApp.Frame.TemplateChanged
name: TemplateChanged
type: Event
summary: Occurs after setting a [Template](xref:112609) for a [](xref:DevExpress.ExpressApp.Frame).
syntax:
  content: public event EventHandler TemplateChanged
seealso:
- linkId: DevExpress.ExpressApp.Frame.SetTemplate(DevExpress.ExpressApp.Templates.IFrameTemplate)
- linkId: DevExpress.ExpressApp.Frame.TemplateChanging
---
Handle the **TemplateChanged** event to customize the current [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Template](xref:DevExpress.ExpressApp.Frame.Template). For details on Tempates customization, refer to the [Template Customization](xref:112696) topic.

To make the application load a custom, rather than a default Template, handle the [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event. If you need to customize a Template and apply your customization each time the Template is displayed, handle the [XafApplication.CustomizeTemplate](xref:DevExpress.ExpressApp.XafApplication.CustomizeTemplate) event.