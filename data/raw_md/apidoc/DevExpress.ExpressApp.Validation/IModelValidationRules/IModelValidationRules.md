---
uid: DevExpress.ExpressApp.Validation.IModelValidationRules
name: IModelValidationRules
type: Interface
summary: The Rules node defines all the Rules that are applied in an application.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelValidationRulesNodeGenerator))]
    public interface IModelValidationRules : IModelNode, IModelList<IModelRuleBase>, IList<IModelRuleBase>, ICollection<IModelRuleBase>, IEnumerable<IModelRuleBase>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Validation.IModelValidationRules._members
  altText: IModelValidationRules Members
- linkId: "113684"
- linkId: "112579"
- linkId: "112580"
---
By default, the Rules node contains several Rules. You can add other Rules (both supplied Rule types and your own) using the context menu of this node.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelValidationRules** node represents a list of the [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Validation.ModelValidationRulesNodeGenerator) Nodes Generator.