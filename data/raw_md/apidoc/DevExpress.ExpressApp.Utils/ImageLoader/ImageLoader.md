---
uid: DevExpress.ExpressApp.Utils.ImageLoader
name: ImageLoader
type: Class
summary: Manages images used in an XAF application.
syntax:
  content: public class ImageLoader
seealso:
- linkId: DevExpress.ExpressApp.Utils.ImageLoader._members
  altText: ImageLoader Members
---
For general guidelines on using images in an XAF application, refer to the [](xref:112792) help topic.

The `ImageLoader` class exposes methods that retrieve metadata on images used in the application. Since XAF uses images of four standard sizes, `ImageLoader` exposes four methods dealing with images of a particular size. The following table lists them.

| Method | Description |
|---|---|
| [ImageLoader.GetImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetImageInfo*) | Supplies metadata on a standard-sized image. |
| [ImageLoader.GetLargeImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetLargeImageInfo*) | Supplies metadata on a large image. |
| [ImageLoader.GetDialogImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetDialogImageInfo*) | Supplies metadata on an image used in dialog windows. |

> [!NOTE]
> All the methods above take the case-insensitive _imageName_ parameter.

`ImageLoader` is a singleton. So, only a single instance of the `ImageLoader` class can be instantiated in an application. To invoke `ImageLoader`'s instance methods, you need to use the `ImageLoader` instance, accessible via the [ImageLoader.Instance](xref:DevExpress.ExpressApp.Utils.ImageLoader.Instance) property. The following code snippet illustrates this. The code retrieves the `BO_Customer` image using the `GetImageInfo` method.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
var customer = ImageLoader.Instance.GetImageInfo("BO_Customer").Image;
```
***