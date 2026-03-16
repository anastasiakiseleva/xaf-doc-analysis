---
uid: DevExpress.ExpressApp.Model.IModelActions
name: IModelActions
type: Interface
summary: The Actions node provides access to all Actions loaded in the Application Model, and allows editing their settings.
syntax:
  content: |-
    [ImageName("ModelEditor_Actions")]
    [ModelNodesGenerator(typeof(ModelActionsNodesGenerator))]
    public interface IModelActions : IModelNode, IModelList<IModelAction>, IList<IModelAction>, ICollection<IModelAction>, IEnumerable<IModelAction>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelActions._members
  altText: IModelActions Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelActions** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelAction) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelActionsNodesGenerator) Nodes Generator.