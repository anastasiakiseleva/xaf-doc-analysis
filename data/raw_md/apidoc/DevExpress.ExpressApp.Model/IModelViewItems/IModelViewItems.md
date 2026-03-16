---
uid: DevExpress.ExpressApp.Model.IModelViewItems
name: IModelViewItems
type: Interface
summary: The Items node provides access to the View Items that are displayed in a Composite View.
syntax:
  content: |-
    [ImageName("ModelEditor_DetailViewItems")]
    [ModelNodesGenerator(typeof(ModelDetailViewItemsNodesGenerator))]
    public interface IModelViewItems : IModelNode, IModelList<IModelViewItem>, IList<IModelViewItem>, ICollection<IModelViewItem>, IEnumerable<IModelViewItem>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelViewItems._members
  altText: IModelViewItems Members
- linkId: "112579"
- linkId: "112580"
---
This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelViewItems** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelViewItem) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewItemsNodesGenerator) Nodes Generator.