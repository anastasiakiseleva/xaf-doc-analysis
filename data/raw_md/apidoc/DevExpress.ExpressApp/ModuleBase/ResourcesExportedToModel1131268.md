---
uid: DevExpress.ExpressApp.ModuleBase.ResourcesExportedToModel
name: ResourcesExportedToModel
type: Property
summary: Provides access to a collection of Resource Localizers used in the current module to extend the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelLocalization) node.
syntax:
  content: public List<Type> ResourcesExportedToModel { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.List{System.Type}
    description: An **IList\<Type>** collection of Resource Localizer types.
seealso:
- linkId: "113301"
---
By default, the **Localization** node allows you to localize only internal XAF resources. However, you can extend this node with child nodes that will allow you to localize the resource strings of the required control used in your application. For this purpose, use the [XafApplication.ResourcesExportedToModel](xref:DevExpress.ExpressApp.XafApplication.ResourcesExportedToModel) property of your application object. A module's **ResourcesExportedToModel** property is an alternative to the application's **ResourcesExportedToModel** property. It also can be set at design time and runtime. However, the localization resources added in a module cannot be removed in another module or application. They can be canceled in the same module only.