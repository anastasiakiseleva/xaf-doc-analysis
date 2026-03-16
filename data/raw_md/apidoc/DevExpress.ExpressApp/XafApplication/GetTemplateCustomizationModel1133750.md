---
uid: DevExpress.ExpressApp.XafApplication.GetTemplateCustomizationModel(DevExpress.ExpressApp.Templates.IFrameTemplate)
name: GetTemplateCustomizationModel(IFrameTemplate)
type: Method
summary: Returns the [Application Model](xref:112580) node where settings of a specified [Template](xref:112696) are stored.
syntax:
  content: public virtual IModelTemplate GetTemplateCustomizationModel(IFrameTemplate template)
  parameters:
  - id: template
    type: DevExpress.ExpressApp.Templates.IFrameTemplate
    description: An object that contains members of the [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interface.
  return:
    type: DevExpress.ExpressApp.Model.IModelTemplate
    description: An [](xref:DevExpress.ExpressApp.Model.IModelTemplate) object that represents an Application Model node with a Template's settings.
seealso: []
---
This method provides access to the Application Model node where the settings of the Template specified by the _template_ parameter are stored. This node is used by the Template's [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method, which creates child nodes to store Template customizations made by an end-user. The `GetTemplateCustomizationModel` method creates and returns a child node for the [](xref:DevExpress.ExpressApp.Model.IModelTemplates) node. You can create another node by overriding this method in your `XafApplication` descendant.