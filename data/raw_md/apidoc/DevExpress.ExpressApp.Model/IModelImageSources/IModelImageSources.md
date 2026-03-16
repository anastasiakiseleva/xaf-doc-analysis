---
uid: DevExpress.ExpressApp.Model.IModelImageSources
name: IModelImageSources
type: Interface
summary: The ImageSources node is used by the system when it loads images. In this node, you can specify your image sources, and set their loading order.
syntax:
  content: |-
    [ImageName("ModelEditor_ImageSources")]
    [ModelNodesGenerator(typeof(ImageSourceNodesGenerator))]
    public interface IModelImageSources : IModelNode, IModelList<IModelImageSource>, IList<IModelImageSource>, ICollection<IModelImageSource>, IEnumerable<IModelImageSource>, IEnumerable
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelImageSources._members
  altText: IModelImageSources Members
- linkId: "112579"
- linkId: "112580"
- linkId: "112792"
---
For information on loading images, refer to the [](xref:112792) topic.

Use the **Add | FileImageSource** or **Add | AssemblyResourceImageSource** menu item of this node's context menu to add a new image source. Specify its **Index** property to set the loading order.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.

The **IModelImageSources** node represents a list of the [](xref:DevExpress.ExpressApp.Model.IModelImageSource) nodes.

To customize the default content of this node, implement a [Generator Updater](xref:112810) for the [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ImageSourceNodesGenerator) Nodes Generator.