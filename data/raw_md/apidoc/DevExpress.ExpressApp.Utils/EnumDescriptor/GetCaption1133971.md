---
uid: DevExpress.ExpressApp.Utils.EnumDescriptor.GetCaption(System.Object)
name: GetCaption(Object)
type: Method
summary: Returns the display caption associated with a specified value of the enumeration represented by the [](xref:DevExpress.ExpressApp.Utils.EnumDescriptor).
syntax:
  content: public string GetCaption(object value)
  parameters:
  - id: value
    type: System.Object
    description: An object representing the enumeration value whose corresponding display caption will be retrieved.
  return:
    type: System.String
    description: A string representing the display caption associated with the specified value of the enumeration represented by the **EnumDescriptor**.
seealso: []
---
The following code snippet illustrates use of the **GetCaption** method. The code retrieves images and display captions associated with **MyEnum** enumeration values.

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