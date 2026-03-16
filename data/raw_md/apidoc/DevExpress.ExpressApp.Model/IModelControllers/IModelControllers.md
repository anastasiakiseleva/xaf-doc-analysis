---
uid: DevExpress.ExpressApp.Model.IModelControllers
name: IModelControllers
type: Interface
summary: The Controllers node provides access to Controllers and their settings. Contains links to nodes that define the Actions contained in Controllers.
syntax:
  content: |-
    [ImageName("ModelEditor_Controllers")]
    [ModelNodesGenerator(typeof(ModelControllersNodesGenerator))]
    public interface IModelControllers : IModelNode, IModelList<IModelController>, IList<IModelController>, ICollection<IModelController>, IEnumerable<IModelController>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelControllers._members
  altText: IModelControllers Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelControllers** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelController) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelControllersNodesGenerator) Nodes Generator.