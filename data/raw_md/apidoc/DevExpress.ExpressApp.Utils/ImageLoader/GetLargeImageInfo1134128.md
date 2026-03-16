---
uid: DevExpress.ExpressApp.Utils.ImageLoader.GetLargeImageInfo(System.String)
name: GetLargeImageInfo(String)
type: Method
summary: Supplies metadata on a large image.
syntax:
  content: public ImageInfo GetLargeImageInfo(string imageName)
  parameters:
  - id: imageName
    type: System.String
    description: A string holding the name of the required image. This parameter is case-insensitive.
  return:
    type: DevExpress.ExpressApp.Utils.ImageInfo
    description: An [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object supplying metadata on a large image.
seealso: []
---
To customize metadata returned by the **GetLargeImageInfo** method, handle the [ImageLoader.CustomizeImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.CustomizeImageInfo) event.

For general guidelines on using images in an **XAF** application, refer to the [](xref:112792) help topic.

The following code snippet illustrates use of the **GetLargeImageInfo** method. The code retrieves the large **Action_Open** image.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
Image image = ImageLoader.Instance.GetLargeImageInfo("Action_Open").Image;
```
***