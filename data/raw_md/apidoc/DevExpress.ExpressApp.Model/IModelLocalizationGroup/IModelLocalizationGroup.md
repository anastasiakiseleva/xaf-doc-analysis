---
uid: DevExpress.ExpressApp.Model.IModelLocalizationGroup
name: IModelLocalizationGroup
type: Interface
summary: A LocalizationGroup node represents a group of localizable items.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelLocalizationGroupGenerator))]
    public interface IModelLocalizationGroup : IModelLocalizationItemBase, IModelNode, IModelList<IModelLocalizationItemBase>, IList<IModelLocalizationItemBase>, ICollection<IModelLocalizationItemBase>, IEnumerable<IModelLocalizationItemBase>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelLocalizationGroup._members
  altText: IModelLocalizationGroup Members
- linkId: "112579"
- linkId: "112580"
- linkId: "112595"
- linkId: "112655"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelLocalizationGroup** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelLocalizationItemBase) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationGroupGenerator) Nodes Generator.