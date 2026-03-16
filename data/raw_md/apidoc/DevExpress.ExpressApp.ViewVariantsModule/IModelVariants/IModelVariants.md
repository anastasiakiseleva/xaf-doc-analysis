---
uid: DevExpress.ExpressApp.ViewVariantsModule.IModelVariants
name: IModelVariants
type: Interface
summary: The Variants node provides access to the varied Views declared for a particular view.
syntax:
  content: |-
    [ImageName("ModelEditor_Views")]
    public interface IModelVariants : IModelNode, IModelList<IModelVariant>, IList<IModelVariant>, ICollection<IModelVariant>, IEnumerable<IModelVariant>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.ViewVariantsModule.IModelVariants._members
  altText: IModelVariants Members
- linkId: "112580"
- linkId: "113011"
---
The **IModelVariants** node represents a list of [](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariant) nodes which specify items of the [ChangeVariantController.ChangeVariantAction](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController.ChangeVariantAction) Action. These items are View variants available for a varied View. The Action is visible if there are two or more variants. You can add a new variant by selecting the **Add Variant** context menu. The [IModelVariants.Current](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariants.Current) property represents a currently selected variant identifier.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.