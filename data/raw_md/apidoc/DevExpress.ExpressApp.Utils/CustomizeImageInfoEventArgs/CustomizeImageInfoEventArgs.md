---
uid: DevExpress.ExpressApp.Utils.CustomizeImageInfoEventArgs
name: CustomizeImageInfoEventArgs
type: Class
summary: Arguments passed to the [ImageLoader.CustomizeImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.CustomizeImageInfo) event.
syntax:
  content: 'public class CustomizeImageInfoEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.Utils.CustomizeImageInfoEventArgs._members
  altText: CustomizeImageInfoEventArgs Members
---
The **CustomizeImageInfo** event occurs when image metadata is retrieved via the [](xref:DevExpress.ExpressApp.Utils.ImageLoader)'s **Get...ImageInfo** methods. Handle this event, to customize the metadata.

The **CustomizeImageInfoEventArgs** class exposes several properties whose values can be customized. For example, you can make an image retrieved via the [ImageLoader.GetImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetImageInfo*) method non-transparent, by setting the [CustomizeImageInfoEventArgs.MakeTransparent](xref:DevExpress.ExpressApp.Utils.CustomizeImageInfoEventArgs.MakeTransparent) property to **false**.