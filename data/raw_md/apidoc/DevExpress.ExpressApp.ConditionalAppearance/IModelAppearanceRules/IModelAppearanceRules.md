---
uid: DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRules
name: IModelAppearanceRules
type: Interface
summary: The **AppearanceRules** node provides access to the conditional appearance rules defined for the business class.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(AppearanceRulesModelNodesGenerator))]
    public interface IModelAppearanceRules : IModelNode, IModelList<IModelAppearanceRule>, IList<IModelAppearanceRule>, ICollection<IModelAppearanceRule>, IEnumerable<IModelAppearanceRule>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRules._members
  altText: IModelAppearanceRules Members
- linkId: "113286"
- linkId: "112579"
- linkId: "112580"
---
The **IModelAppearanceRules** node exposes a list of the [](xref:DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRule) nodes. To learn how to use this node to add conditional appearance rules, refer to the [Declare Conditional Appearance Rules in the Application Model](xref:113372) topic.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceRulesModelNodesGenerator) Nodes Generator.

This interface is a part of the [Application Model infrastructure]( xref:112580). You do not need to implement this interface in most cases.