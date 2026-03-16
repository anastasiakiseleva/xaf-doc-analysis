---
uid: DevExpress.Persistent.BaseImpl.MediaDataObject
name: MediaDataObject
type: Class
summary: The XPO persistent class used to store media data in the database.
syntax:
  content: |-
    [Browsable(false)]
    [EditorAlias("ImagePropertyEditor")]
    [MediaDataObject("MediaDataKey", "MediaData", "MediaData")]
    public class MediaDataObject : BaseObject, IEmptyCheckable
seealso:
- linkId: DevExpress.Persistent.BaseImpl.MediaDataObject._members
  altText: MediaDataObject Members
---
You can use the `MediaDataObject` type to declare a reference property of a business class that is used to store and display an image.

WinForms and ASP.NET Core Blazor [Image Property Editors](xref:113544) are used automatically for properties of the `MediaDataObject` type.

You can find an example in the [BLOB Image Properties in XPO](xref:113545#image-as-a-mediadataobject) topic.

`MediaDataObject` is a container for two values:

- [MediaDataObject.MediaData](xref:DevExpress.Persistent.BaseImpl.MediaDataObject.MediaData)
    A byte array object that is loaded from a database on demand when required. It is not loaded together with the `MediaDataObject` itself and may contain any type of media.
- [MediaDataObject.MediaDataKey](xref:DevExpress.Persistent.BaseImpl.MediaDataObject.MediaDataKey)
    A key value of the string type. This value should not be changed from your code. It is updated automatically when the `MediaData` byte array is changed and is unique for each `MediaDataObject`. `MediaDataKey` is used in a URL of the `MediaData` loaded by a browser. The URL is generated under the following conditions.

    * `MediaDataKey` is constant while `MediaData` is not updated.
    * It is not required to load `MediaData` when generating the URL.
    * `MediaDataKey` can be quickly obtained as it is not required to load `MediaData` every time to calculate the key.


The Winforms and Blazor editors (**ImagePropertyEditor**) support the `MediaDataObject` property type partially - they use `MediaData` only, and do not provide caching.

> [!NOTE]
> It is not recommend to change the `MediaData` value by direct database queries. In this instance, the URL will not change, and it will be required to manually refresh the page to see the changes.