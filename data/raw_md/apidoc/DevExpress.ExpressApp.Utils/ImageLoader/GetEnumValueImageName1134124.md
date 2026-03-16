---
uid: DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageName(System.Object)
name: GetEnumValueImageName(Object)
type: Method
summary: Returns the name of the image associated with an enumeration value.
syntax:
  content: public string GetEnumValueImageName(object enumValue)
  parameters:
  - id: enumValue
    type: System.Object
    description: The enumeration value for which the associated image name will be retrieved.
  return:
    type: System.String
    description: A string representing the name of the image associated with the specified enumeration value.
seealso:
- linkId: DevExpress.ExpressApp.Utils.EnumDescriptor
- linkId: DevExpress.ExpressApp.Utils.EnumDescriptor.GetImageInfo(System.Object)
- linkId: DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageInfo*
---
As an alternative to this method, you can use the [ImageInfo.ImageName](xref:DevExpress.ExpressApp.Utils.ImageInfo.ImageName) property of the [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object returned by the [ImageLoader.GetEnumValueImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageInfo*) and [EnumDescriptor.GetImageInfo](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GetImageInfo(System.Object)) methods.

The following code snippet illustrates use of the **GetEnumValueImageName** method. The code retrieves the name of the image associated with the **MyEnum.FirstValue** enumeration value.

# [C#](#tab/tabid-csharp)

```csharp
string image = ImageLoader.Instance.GetEnumValueImageName(MyEnum.FirstValue);
```
***