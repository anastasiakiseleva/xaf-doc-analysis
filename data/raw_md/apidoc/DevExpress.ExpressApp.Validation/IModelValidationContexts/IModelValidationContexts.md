---
uid: DevExpress.ExpressApp.Validation.IModelValidationContexts
name: IModelValidationContexts
type: Interface
summary: The Contexts node defines the validation contexts used in the application.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelValidationContextsNodeGenerator))]
    public interface IModelValidationContexts : IModelNode, IModelList<IModelValidationContext>, IList<IModelValidationContext>, ICollection<IModelValidationContext>, IEnumerable<IModelValidationContext>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Validation.IModelValidationContexts._members
  altText: IModelValidationContexts Members
- linkId: "113684"
- linkId: "112579"
- linkId: "112580"
---
When using the **ShowAllContexts** Action to see whether entered data is valid, the invoked window provides information on all checked rules. This information is grouped by contexts. You can localize the contexts, so that the information is readable for end-users. To do this, use this node.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelValidationContexts** node represents a list of the [](xref:DevExpress.ExpressApp.Validation.IModelValidationContext) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Validation.ModelValidationContextsNodeGenerator) Nodes Generator.