---
uid: DevExpress.ExpressApp.Model.IModelLocalization
name: IModelLocalization
type: Interface
summary: The Localization node allows [localization](xref:112595) of UI elements such as messages, exceptions, button captions and so on.
syntax:
  content: |-
    [ImageName("BO_Localization")]
    [ModelNodesGenerator(typeof(ModelLocalizationNodesGenerator))]
    public interface IModelLocalization : IModelNode, IModelList<IModelLocalizationGroup>, IList<IModelLocalizationGroup>, ICollection<IModelLocalizationGroup>, IEnumerable<IModelLocalizationGroup>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelLocalization._members
  altText: IModelLocalization Members
- linkId: "112579"
---
You can use predefined groups of localization elements to localize them in the required language. You can also add a new group with your string constants, and get localized values in code. For detailed information on using this node in code, refer to the [How to: Localize Custom String Constants](xref:112655) topic.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelLocalization** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationNodesGenerator) Nodes Generator.