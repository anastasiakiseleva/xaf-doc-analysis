---
uid: DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Template
name: Template
type: Property
summary: Specifies the [Template](xref:112609) which is created in a [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event handler.
syntax:
  content: public IFrameTemplate Template { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.IFrameTemplate
    description: An object that supports the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface. This object represents the created Template.
seealso: []
---
When creating a custom Template in a [XafApplication.CreateCustomTemplate](xref:DevExpress.ExpressApp.XafApplication.CreateCustomTemplate) event handler, assign it to this property to show it instead of a default one.