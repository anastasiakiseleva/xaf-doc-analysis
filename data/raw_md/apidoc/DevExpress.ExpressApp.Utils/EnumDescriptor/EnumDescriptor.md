---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor
name: EnumDescriptor
type: Class
summary: Supplies metadata information on an enumeration used in an **XAF** application.
syntax:
  content: 'public class EnumDescriptor : IEnumDescriptor'
seealso:
- linkId: DevExpress.ExpressApp.Utils.EnumDescriptor._members
  altText: EnumDescriptor Members
- linkId: "112825"
- linkId: "402159"
---
The **EnumDescriptor** class' properties and methods provide access to the enumeration metadata - the enumeration values, associated display captions and image. The most useful members of the **EnumDescriptor** class are the [EnumDescriptor.GetCaption](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GetCaption*) and [EnumDescriptor.GetImageInfo](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GetImageInfo(System.Object)) methods. The following code snippet illustrates their use. The code retrieves images and display captions associated with **MyEnum** enumeration values.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
//...
EnumDescriptor myDescriptor = new EnumDescriptor(typeof(MyEnum));
foreach(object enumValue in myDescriptor.Values) {
    string caption = myDescriptor.GetCaption(enumValue);
    var image = myDescriptor.GetImageInfo(enumValue).Image;
    //process caption and image
}
```
***