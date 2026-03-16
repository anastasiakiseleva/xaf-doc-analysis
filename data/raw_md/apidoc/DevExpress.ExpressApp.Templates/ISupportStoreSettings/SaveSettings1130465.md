---
uid: DevExpress.ExpressApp.Templates.ISupportStoreSettings.SaveSettings
name: SaveSettings()
type: Method
summary: Saves a Template's settings previously changed by an end-user to the child nodes of the [Application Model](xref:112580)'s **Templates** node. These child nodes were previously specified by the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method.
syntax:
  content: void SaveSettings()
seealso: []
---
Template customizations that have been made by an end-user must be saved to the Application Model's **Template** node. For this purpose, the **SaveSettings** method is called when a Template is disposed of. The nested structure of this node must be specified by the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method, which is invoked earlier - when creating a Template. The saved customizations are then applied to the Template by calling the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method again.

Physically, the customizations are stored in the _Model.User.xafml_ file. When a Template is created, the **Template** node customizations from this file are passed to the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method, to be applied to the Template. So, if you remove this file, the **Template** node structure must be recreated by the [ISupportStoreSettings.SetSettings](xref:DevExpress.ExpressApp.Templates.ISupportStoreSettings.SetSettings(DevExpress.ExpressApp.Model.IModelTemplate)) method.

> [!NOTE]
> UI customizations can only be saved in Windows Forms applications.