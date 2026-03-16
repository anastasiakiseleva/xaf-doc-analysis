---
uid: DevExpress.ExpressApp.Utils.ImageLoader.CustomizeImageInfo
name: CustomizeImageInfo
type: Event
summary: Occurs when image metadata is retrieved via the [](xref:DevExpress.ExpressApp.Utils.ImageLoader)'s **Get...ImageInfo** methods. Allows you to customize the metadata.
syntax:
  content: public event EventHandler<CustomizeImageInfoEventArgs> CustomizeImageInfo
seealso: []
---
For instance, you can handle this event if you want to enable transparency support for a specific image. Handle the **CustomizeImageInfo** event and set the [CustomizeImageInfoEventArgs.MakeTransparent](xref:DevExpress.ExpressApp.Utils.CustomizeImageInfoEventArgs.MakeTransparent) property to **true**.

# [C#](#tab/tabid-csharp)

```csharp
ImageLoader.Instance.CustomizeImageInfo += ImageLoader_CustomizeImageInfo;
//...
void ImageLoader_CustomizeImageInfo(object sender, CustomizeImageInfoEventArgs e) {
    if(e.ImageName == "MyIncorrectlyDisplayedImage") e.MakeTransparent = true;            
}
```
***