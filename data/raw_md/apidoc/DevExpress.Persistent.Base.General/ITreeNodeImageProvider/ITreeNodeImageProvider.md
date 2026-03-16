---
uid: DevExpress.Persistent.Base.General.ITreeNodeImageProvider
name: ITreeNodeImageProvider
type: Interface
summary: Can be implemented by the classes implementing the [](xref:DevExpress.Persistent.Base.General.ITreeNode) interface, to support raster node images.
syntax:
  content: public interface ITreeNodeImageProvider
seealso:
- linkId: DevExpress.Persistent.Base.General.ITreeNodeImageProvider._members
  altText: ITreeNodeImageProvider Members
- linkId: DevExpress.Persistent.Base.General.ITreeNode
- linkId: "112836"
---
Implement the **ITreeNodeImageProvider** interface to enable images for a [Tree List](xref:112837)'s objects.

![ITreeNodeImageProvider](~/images/itreenodeimageprovider116370.png)

The **ITreeNodeImageProvider** interface declares a single member - the [ITreeNodeImageProvider.GetImage](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider.GetImage(System.String@)) method. This method returns a raster image corresponding to a tree node.

To see an example of the **ITreeNodeImageProvider** interface implementation, refer to the [Node Images in a Tree List](xref:113215) topic.