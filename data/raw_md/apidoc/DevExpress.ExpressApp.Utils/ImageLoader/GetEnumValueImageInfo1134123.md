---
uid: DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageInfo(System.Object)
name: GetEnumValueImageInfo(Object)
type: Method
summary: Supplies metadata on the image associated with an enumeration value.
syntax:
  content: public ImageInfo GetEnumValueImageInfo(object enumValue)
  parameters:
  - id: enumValue
    type: System.Object
    description: The enumeration value for which image metada will be retrieved.
  return:
    type: DevExpress.ExpressApp.Utils.ImageInfo
    description: An [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object supplying metadata on the image associated with the specified enumeration value.
seealso:
- linkId: DevExpress.ExpressApp.Utils.EnumDescriptor
- linkId: DevExpress.ExpressApp.Utils.EnumDescriptor.GetImageInfo(System.Object)
- linkId: DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageName*
---
To customize metadata returned by the **GetEnumValueImageInfo** method, handle the [ImageLoader.CustomizeImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.CustomizeImageInfo) event.

As an alternative to this method, you can use the [EnumDescriptor.GetImageInfo](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GetImageInfo(System.Object)) method.

The following code snippet illustrates use of the **GetEnumValueImageInfo** method. The code retrieves the image associated with the **MyEnum.FirstValue** enumeration value.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
var image = ImageLoader.Instance.GetEnumValueImageInfo(MyEnum.FirstValue).Image;
```
***