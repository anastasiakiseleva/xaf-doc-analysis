---
uid: DevExpress.ExpressApp.ViewVariantsModule.FrameVariantsEngine.GetVariants(DevExpress.ExpressApp.View)
name: GetVariants(View)
type: Method
summary: Returns a set of view variants available for the specific View.
syntax:
  content: public VariantsInfo GetVariants(View view)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) object.
  return:
    type: DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo
    description: An [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo) object that contains a list of view variants.
seealso: []
---
This method checks whether or not the passed View is created as a view variant, and returns a set of view variants available for this View.