---
uid: DevExpress.ExpressApp.ViewVariantsModule.ModelVariantsProvider.GetVariants(System.String)
name: GetVariants(String)
type: Method
summary: Returns a set of view variants available for the specific root View in the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariants) Application Model node. In case there are no view variants, returns `null`.
syntax:
  content: public VariantsInfo GetVariants(string rootVariantViewId)
  parameters:
  - id: rootVariantViewId
    type: System.String
    description: A string representing the identifier of the varied View having the [VariantsInfo.Items](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.Items) as View variants.
  return:
    type: DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo
    description: A [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo) object that contains a set of view variants.
seealso: []
---
