---
uid: DevExpress.ExpressApp.ViewVariantsModule.IFrameVariantsEngine.ChangeFrameViewToVariant(DevExpress.ExpressApp.Frame,DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo,DevExpress.ExpressApp.ViewVariantsModule.VariantInfo)
name: ChangeFrameViewToVariant(Frame, VariantsInfo, VariantInfo)
type: Method
summary: Changes the view variant.
syntax:
  content: void ChangeFrameViewToVariant(Frame frame, VariantsInfo variantsInfo, VariantInfo variantInfo)
  parameters:
  - id: frame
    type: DevExpress.ExpressApp.Frame
    description: A [](xref:DevExpress.ExpressApp.Frame) object.
  - id: variantsInfo
    type: DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo
    description: A [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo) object that specifies a set of available view variants.
  - id: variantInfo
    type: DevExpress.ExpressApp.ViewVariantsModule.VariantInfo
    description: A [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo) object that specifies the new view variant.
seealso: []
---
Modifies the [Frame.View](xref:DevExpress.ExpressApp.Frame.View) value of the passed [](xref:DevExpress.ExpressApp.Frame) object and the [VariantsInfo.CurrentVariantId](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.CurrentVariantId) value of the passed [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo) object, and saves the current choice when required. Creates a new [](xref:DevExpress.ExpressApp.View) object based on the passed [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo) object or uses the **ListPropertyEditor.RecreateListView** if the [](xref:DevExpress.ExpressApp.NestedFrame) is passed.