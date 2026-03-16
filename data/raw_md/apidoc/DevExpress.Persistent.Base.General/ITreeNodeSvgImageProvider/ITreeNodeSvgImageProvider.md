---
uid: DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider
name: ITreeNodeSvgImageProvider
type: Interface
summary: Can be implemented by the classes implementing the [](xref:DevExpress.Persistent.Base.General.ITreeNode) interface, to support SVG node images.
syntax:
  content: public interface ITreeNodeSvgImageProvider
seealso:
- linkId: DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider._members
  altText: ITreeNodeSvgImageProvider Members
- linkId: DevExpress.Persistent.Base.General.ITreeNode
- linkId: "112836"
---
Implement the **ITreeNodeSvgImageProvider** interface to enable images for [Tree List](xref:112837)'s objects.

![ITreeNodeImageProvider](~/images/itreenodeimageprovider116370.png)

The **ITreeNodeSvgImageProvider** interface declares a single member - the [ITreeNodeSvgImageProvider.GetSvgImage](xref:DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider.GetSvgImage(System.String@)) method. This method returns the SVG image corresponding to a tree node.

To see an example of the **ITreeNodeSvgImageProvider** interface implementation, refer to the [Node Images in a Tree List](xref:113215) topic.
