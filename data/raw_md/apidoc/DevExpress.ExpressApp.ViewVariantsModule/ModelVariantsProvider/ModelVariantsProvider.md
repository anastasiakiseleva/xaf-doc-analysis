---
uid: DevExpress.ExpressApp.ViewVariantsModule.ModelVariantsProvider
name: ModelVariantsProvider
type: Class
summary: Provide a list of view variants available for the specific View in the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariants) Application Model node, and stores the variant selected by the user to the [IModelVariants.Current](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariants.Current) property.
syntax:
  content: 'public class ModelVariantsProvider : IVariantsProvider'
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.ModelVariantsProvider._members
  altText: ModelVariantsProvider Members
---
The **ModelVariantsProvider** implements the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IVariantsProvider) interface and stores view variants in the Application Model. You can create a custom **ModelVariantsProvider** implementation and pass it to the [ViewVariantsModule.VariantsProvider](xref:DevExpress.ExpressApp.ViewVariantsModule.ViewVariantsModule.VariantsProvider) property.