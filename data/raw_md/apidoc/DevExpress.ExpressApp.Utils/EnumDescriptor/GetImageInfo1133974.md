---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.GetImageInfo(System.Object)
name: GetImageInfo(Object)
type: Method
summary: Supplies metadata on the image associated with a particular value of the enumeration represented by the [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor).
syntax:
  content: public ImageInfo GetImageInfo(object value)
  parameters:
  - id: value
    type: System.Object
    description: The enumeration value for which image metada will be retrieved.
  return:
    type: DevExpress.ExpressApp.Utils.ImageInfo
    description: An [](xref:DevExpress.ExpressApp.Utils.ImageInfo) object supplying metadata on the image associated with the specified value of the enumeration represented by the EnumDescriptor.
seealso:
- linkId: DevExpress.ExpressApp.Utils.ImageLoader
- linkId: DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageInfo*
- linkId: DevExpress.ExpressApp.Utils.ImageLoader.GetEnumValueImageName*
---
The following code snippet illustrates use of the **GetImageInfo** property. The code retrieves images and display captions associated with **MyEnum** enumeration values.

# [C#](#tab/tabid-csharp)

```csharp
//...
EnumDescriptor myDescriptor = new EnumDescriptor(typeof(MyEnum));
foreach(object enumValue in myDescriptor.Values) {
    string caption = myDescriptor.GetCaption(enumValue);
    var image = myDescriptor.GetImageInfo(enumValue).Image;
    //process caption and image
}
```
***