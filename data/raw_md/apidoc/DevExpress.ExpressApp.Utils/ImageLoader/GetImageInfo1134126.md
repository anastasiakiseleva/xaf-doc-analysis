---
uid: DevExpress.ExpressApp.Utils.ImageLoader.GetImageInfo(System.String)
name: GetImageInfo(String)
type: Method
summary: Supplies metadata on a standard-sized image.
syntax:
  content: public ImageInfo GetImageInfo(string imageName)
  parameters:
  - id: imageName
    type: System.String
    description: A string holding the name of the required image. This parameter is case-insensitive.
  return:
    type: DevExpress.ExpressApp.Utils.ImageInfo
    description: An [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object supplying metadata on a standard-sized image.
seealso: []
---
To customize metadata returned by the **GetImageInfo** method, handle the [ImageLoader.CustomizeImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.CustomizeImageInfo) event.

For general guidelines on using images in an **XAF** application, refer to the [](xref:112792) help topic.

The following code snippet illustrates use of the **GetImageInfo** method. The code retrieves the **Action_Open** image.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
var image = ImageLoader.Instance.GetImageInfo("Action_Open").Image;
```
***