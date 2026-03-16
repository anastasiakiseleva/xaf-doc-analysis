---
uid: DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo
name: VariantsInfo
type: Class
summary: Represents a set of variants available for the [View](xref:112611).
syntax:
  content: public class VariantsInfo
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo._members
  altText: VariantsInfo Members
- linkId: DevExpress.ExpressApp.ViewVariantsModule.VariantInfo
- linkId: "113011"
---
The [View Variants Module](xref:113011) provides the ability to have several customized variants of the same [View](xref:112611). The **VariantsInfo** class is used to represent a set of variants available for a particular View.

The View variants read-only collection is exposed via the [VariantsInfo.Items](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.Items) property. The items of this collection are represented by the [](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantInfo) structure.  The View variants are assigned to a certain varied View. This View identifier is exposed via the [VariantsInfo.RootViewId](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.RootViewId) property. The currently selected View variant is exposed via the [VariantsInfo.CurrentVariantId](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.CurrentVariantId) property.

Use the [VariantsInfo.GetCurrentVariantInfo](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.GetCurrentVariantInfo) method to access the currently selected variant. You can search the particular variant by its identifier via the [VariantsInfo.FindById](xref:DevExpress.ExpressApp.ViewVariantsModule.VariantsInfo.FindById(System.String)) method.