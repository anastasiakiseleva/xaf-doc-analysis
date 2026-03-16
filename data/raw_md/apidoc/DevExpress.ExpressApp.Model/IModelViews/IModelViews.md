---
uid: DevExpress.ExpressApp.Model.IModelViews
name: IModelViews
type: Interface
summary: The Views node provides access to the Views of all the business classes added to the Application Model.
syntax:
  content: |-
    [ImageName("ModelEditor_Views")]
    [ModelNodesGenerator(typeof(ModelViewsNodesGenerator))]
    public interface IModelViews : IModelNode, IModelList<IModelView>, IList<IModelView>, ICollection<IModelView>, IEnumerable<IModelView>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelViews._members
  altText: IModelViews Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelViews** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelView) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelViewsNodesGenerator) Nodes Generator.