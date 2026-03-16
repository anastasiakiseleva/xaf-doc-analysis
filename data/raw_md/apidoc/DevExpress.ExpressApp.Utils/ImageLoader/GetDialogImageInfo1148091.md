---
uid: DevExpress.ExpressApp.Utils.ImageLoader.GetDialogImageInfo(System.String,System.String)
name: GetDialogImageInfo(String, String)
type: Method
summary: Supplies metadata on an image used in dialog windows.
syntax:
  content: public ImageInfo GetDialogImageInfo(string imageName, string imageFolder)
  parameters:
  - id: imageName
    type: System.String
    description: A string holding the name of the required image. This parameter is case-insensitive.
  - id: imageFolder
    type: System.String
    description: A string holding the name of the required image folder.
  return:
    type: DevExpress.ExpressApp.Utils.ImageInfo
    description: An [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object supplying metadata on an image used in dialog windows.
seealso: []
---
To customize metadata returned by the **GetDialogImageInfo** method, handle the [ImageLoader.CustomizeImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.CustomizeImageInfo) event.

For general guidelines on using images in an **XAF** application, refer to the [](xref:112792) help topic.
