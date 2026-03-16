---
uid: DevExpress.ExpressApp.Model.IModelFileImageSource
name: IModelFileImageSource
type: Interface
summary: A FileImageSource node defines the image source when the images are stored in a separate folder.
syntax:
  content: |-
    [KeyProperty("Folder")]
    public interface IModelFileImageSource : IModelImageSource, IModelNode
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelFileImageSource._members
  altText: IModelFileImageSource Members
- linkId: "112579"
- linkId: "112580"
- linkId: "112792"
---
For this source, a folder with images is specified. For each image, the **Copy to Output Directory** option must be set to **Copy always**, so the images will always be copied to the output directory.

This interface is a part of the [Application Model infrastructure](xref:112580). You do not need to implement this interface in most cases.