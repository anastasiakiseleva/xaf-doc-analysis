---
uid: DevExpress.Persistent.Base.General.ITreeNodeImageProvider.GetImage(System.String@)
name: GetImage(out String)
type: Method
summary: Returns the raster image corresponding to a tree node.
syntax:
  content: DXImage GetImage(out string imageName)
  parameters:
  - id: imageName
    type: System.String
    description: The returned raster image's name.
  return:
    type: DevExpress.Drawing.DXImage
    description: The raster image corresponding to a tree node.
seealso: []
---
This method returns the raster image that corresponds to a [Tree List](xref:112836)'s node.
Specify the `imageName` parameter only if you use the same image for multiple nodes. Otherwise, assign `null`.