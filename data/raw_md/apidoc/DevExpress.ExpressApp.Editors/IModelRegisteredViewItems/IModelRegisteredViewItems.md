---
uid: DevExpress.ExpressApp.Editors.IModelRegisteredViewItems
name: IModelRegisteredViewItems
type: Interface
summary: The ViewItems node specifies [View Items](xref:112612) to be used in a [Detail View](xref:112611).
syntax:
  content: |-
    [ImageName("ModelEditor_DetailViewItems")]
    [ModelNodesGenerator(typeof(ModelRegisteredViewItemsGenerator))]
    public interface IModelRegisteredViewItems : IModelNode, IModelList<IModelRegisteredViewItem>, IList<IModelRegisteredViewItem>, ICollection<IModelRegisteredViewItem>, IEnumerable<IModelRegisteredViewItem>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Editors.IModelRegisteredViewItems._members
  altText: IModelRegisteredViewItems Members
- linkId: "112579"
- linkId: "112580"
---
This node shows which View Items are used by default. With this node, you can edit the default behavior by assigning another available View Items.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelRegisteredViewItems** node represents a list of the [](xref:DevExpress.ExpressApp.Editors.IModelRegisteredViewItem) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Editors.ModelRegisteredViewItemsGenerator) Nodes Generator.