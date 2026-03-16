---
uid: DevExpress.ExpressApp.Window.Template
name: Template
type: Property
summary: Returns a Window's [Template](xref:112609).
syntax:
  content: public IWindowTemplate Template { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.IWindowTemplate
    description: An object implementing the [](xref:DevExpress.ExpressApp.Templates.IWindowTemplate) interface. It represents the current Window's Template.
seealso:
- linkId: DevExpress.ExpressApp.Frame.Template
- linkId: DevExpress.ExpressApp.Frame.TemplateChanged
- linkId: DevExpress.ExpressApp.Frame.Context
---
Each window has a particular [Frame.Context](xref:DevExpress.ExpressApp.Frame.Context). According to this Context, the Template type to be created is chosen.

Use the **IWindowTemplate** object that is returned by this property to access its [Action Containers](xref:112610) collection. To learn how to customize a Template, refer to the [Template Customization](xref:112696) topic.