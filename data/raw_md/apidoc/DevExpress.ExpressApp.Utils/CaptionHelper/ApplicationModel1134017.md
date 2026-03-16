---
uid: DevExpress.ExpressApp.Utils.CaptionHelper.ApplicationModel
name: ApplicationModel
type: Property
summary: Provides access to the [Application Model](xref:112580).
syntax:
  content: public static IModelApplication ApplicationModel { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Model.IModelApplication
    description: An [](xref:DevExpress.ExpressApp.Model.IModelApplication) object representing the Application Model's root node.
seealso: []
---
Generally, you should not use this property. If you need to access the Application Model, use the [XafApplication.Model](xref:DevExpress.ExpressApp.XafApplication.Model) property.

To learn how to customize the Application Model, refer to the [Extend and Customize the Application Model in Code](xref:112810) help topic. To learn how to use the Application Model in code, refer to the [Access the Application Model in Code](xref:112810) help topic.