---
uid: DevExpress.ExpressApp.Utils.ImageLoader.Instance
name: Instance
type: Property
summary: Provides access to the [](xref:DevExpress.ExpressApp.Utils.ImageLoader) instance.
syntax:
  content: public static ImageLoader Instance { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Utils.ImageLoader
    description: An [](xref:DevExpress.ExpressApp.Utils.ImageLoader) object representing the **ImageLoader** instance.
seealso:
- linkId: "112792"
---
**ImageLoader** is a singleton. So, only a single instance of the **ImageLoader** class can be instantiated in an application. To invoke **ImageLoader**'s instance methods, you need to use the **ImageLoader** instance, accessible via the **Instance** property. The following code snippet illustrates this. The code retrieves the **BO_Customer** image using the [ImageLoader.GetImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetImageInfo*) method.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
var customer = ImageLoader.Instance.GetImageInfo("BO_Customer").Image;
```
***