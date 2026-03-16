---
uid: DevExpress.ExpressApp.Model.IModelControllerActions
name: IModelControllerActions
type: Interface
summary: The Actions node represents the Actions contained in a Controller.
syntax:
  content: |-
    [ModelNodesGenerator(typeof(ModelControllerActionsNodesGenerator))]
    public interface IModelControllerActions : IModelNode, IModelList<IModelActionLink>, IList<IModelActionLink>, ICollection<IModelActionLink>, IEnumerable<IModelActionLink>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelControllerActions._members
  altText: IModelControllerActions Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelControllerActions** node represents a list of the [](xref:DevExpress.ExpressApp.SystemModule.IModelActionLink) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelControllerActionsNodesGenerator) Nodes Generator.