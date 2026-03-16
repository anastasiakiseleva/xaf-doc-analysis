---
uid: DevExpress.ExpressApp.CustomizeTemplateEventArgs.Template
name: Template
type: Property
summary: Provides access to the [Template](xref:112609) to be customized.
syntax:
  content: public IFrameTemplate Template { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.IFrameTemplate
    description: An object that supports the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface. This object  represents the customized Template.
seealso: []
---
Use members of the object returned by this property, to customize it. For instance, use the [IFrameTemplate.GetContainers](xref:DevExpress.ExpressApp.Templates.IFrameTemplate.GetContainers) method that provides access to the Template's [Action Container](xref:112610) collection, which allows you to customize them.