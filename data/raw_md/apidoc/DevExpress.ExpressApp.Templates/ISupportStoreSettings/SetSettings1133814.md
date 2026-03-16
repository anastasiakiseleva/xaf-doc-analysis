---
uid: DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)
name: SetSettings(IModelTemplate)
type: Method
summary: Creates and/or provides access to child nodes of the [Application Model](xref:112580)'s **Template** node where customizations made by an end-user must be stored. To apply these customizations, this method calls the [ISupportStoreSettings.ReloadSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.ReloadSettings) method.
syntax:
  content: void SetSettings(IModelTemplate settings)
  parameters:
  - id: settings
    type: DevExpress.ExpressApp.Model.IModelTemplate
    description: An [](xref:DevExpress.ExpressApp.Model.IModelTemplate) object that represents the Application Model's **Template** node, providing settings for the current Template.
seealso: []
---
When a Template is created, the customizations previously made by an end-user must be applied to the Template's controls (form state, toolbar state, etc.). For this purpose, the **SetSettings** method is invoked. This method must create and/or provide access to child nodes of the Application Model's **Template** node which is passed by the settings parameter. Then, this method should call the [ISupportStoreSettings.ReloadSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.ReloadSettings) method to apply the settings stored in the accessed(created) nodes to the Template's controls.

When invoking the [Model Editor](xref:112582) at runtime or closing a Window, the changes made by an end-user must be saved to the Template node's child nodes. For this purpose, the [ISupportStoreSettings.SaveSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SaveSettings) method is called.

Physically, the customizations are stored in the Model.User.xafml file. When a Template is created, the **Template** node customizations from this file are passed to the **SetSettings** method to be applied to the Template. So, if you remove this file, the **Template** node structure must be recreated by the SetSettings method.

> [!NOTE]
> UI customizations can be saved in Windows Forms applications only.