---
uid: DevExpress.ExpressApp.ViewVariantsModule.VariantInfo
name: VariantInfo
type: Struct
summary: Represents a [View](xref:112611) variant.
syntax:
  content: public struct VariantInfo
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.VariantInfo._members
  altText: VariantInfo Members
- linkId: DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo
- linkId: "113011"
---
The [View Variants Module](xref:113011) provides the ability to have several customized variants of the same View. The **VariantInfo** is used to represent a  variant available for a particular [View](xref:112611).

Each variant has an associated View, invoked when selecting this variant. The identifier of this View is exposed via the [VariantInfo.ViewID](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo.ViewID) field. Additionally, each variant has its own identifier and caption exposed via the [VariantInfo.Id](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo.Id) and [VariantInfo.Caption](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo.Caption) fields.