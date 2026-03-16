---
uid: DevExpress.ExpressApp.ViewVariantsModule.IModelVariant
name: IModelVariant
type: Interface
summary: A Variant node defines an item of the [ChangeVariantController.ChangeVariantAction](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.ChangeVariantAction) action. Each item represents a View variant available for a varied View.
syntax:
  content: |-
    [DisplayProperty("Caption")]
    [ImageName("ModelEditor_ListView")]
    public interface IModelVariant : IModelNode
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.IModelVariant._members
  altText: IModelVariant Members
- linkId: "112580"
- linkId: "113011"
---
You can delete a variant by selecting the **Delete Variant** context menu.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.