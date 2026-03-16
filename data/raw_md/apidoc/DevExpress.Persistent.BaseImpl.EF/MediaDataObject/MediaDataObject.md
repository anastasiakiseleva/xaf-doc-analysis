---
uid: DevExpress.Persistent.BaseImpl.EF.MediaDataObject
name: MediaDataObject
type: Class
summary: The entity used to store media data in the database.
syntax:
  content: |-
    [Browsable(false)]
    [EditorAlias("ImagePropertyEditor")]
    [MediaDataObject("MediaDataKey", "MediaData", "MediaResource.MediaData")]
    public class MediaDataObject : BaseObjectWithNotifyPropertyChanged, IEmptyCheckable
seealso:
- linkId: DevExpress.Persistent.BaseImpl.EF.MediaDataObject._members
  altText: MediaDataObject Members
---
You can use the `MediaDataObject` type to declare a reference property of a business class that is used to store and display an image.

WinForms and ASP.NET Core Blazor [Image Property Editors](xref:113544) are used automatically for properties of the `MediaDataObject` type.

You can find an example in the [BLOB Image Properties in EF Core](xref:113546#image-as-a-mediadataobject) topic.

`MediaDataObject` is a container for three values:

-  [MediaDataObject.MediaData](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaData)
    
    A byte array object that is loaded from a database on demand when required. It is not loaded together with the `MediaDataObject` itself and may contain any type of media. This property is non-persistent, its value is stored using the MediaResource.MediaData persistent property to provide delayed loading.
- [MediaDataObject.MediaDataKey](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaDataKey)
    
    A key value of the string type. This value should not be changed from your code. It is updated automatically when the `MediaData` byte array is changed and is unique for each `MediaDataObject`. `MediaDataKey` is used in a URL of the `MediaData` loaded by a browser. The URL is generated under the following conditions.

    * `MediaDataKey` is constant while `MediaData` is not updated.
    * It is not required to load MediaData when generating the URL.
    * `MediaDataKey` can be quickly obtained as it is not required to load `MediaData` every time to calculate the key.
- [MediaDataObject.MediaResource](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaResource)

    The `MediaResourceObject` object which exposes the `MediaData` property of the byte array type. The `MediaData` property of this object is persistent and stores the byte array returned by the [MediaDataObject.MediaData](xref:DevExpress.Persistent.BaseImpl.EF.MediaDataObject.MediaData) property.

Currently, the Winforms and Blazor editors (**ImagePropertyEditor**) support the `MediaDataObject` property type partially - they use `MediaData` only, and do not provide caching.

> [!NOTE]
> It is not recommend to change the `MediaData` value by direct database queries. In this instance, the URL will not change, and it will be required to manually refresh the page to see the changes.