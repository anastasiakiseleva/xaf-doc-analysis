---
uid: DevExpress.ExpressApp.Templates.ISupportStoreSettings.ReloadSettings
name: ReloadSettings()
type: Method
summary: Applies settings provided by the [Application Model](xref:112580)'s **Template** node to a [Template](xref:112609) at runtime. These settings are provided by the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method.
syntax:
  content: void ReloadSettings()
seealso: []
---
When a Template is created, the customizations previously made by an end-user must be applied to the Template's controls (form state, toolbar state, etc.). For this purpose, the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method is invoked. This method creates or provides access to child nodes of the Application Model's **Template** node which is passed by a parameter. Then, this method calls the **ReloadSettings** method, to apply the settings stored in the accessed(created) nodes to the Template's controls.

When invoking the [Model Editor](xref:112830) at runtime or closing a Window, the changes made by an end-user must be saved to the **Template** node's child nodes. For this purpose, the [ISupportStoreSettings.SaveSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SaveSettings) method is called.

> [!NOTE]
> UI customizations can only be saved in a Windows Forms application.