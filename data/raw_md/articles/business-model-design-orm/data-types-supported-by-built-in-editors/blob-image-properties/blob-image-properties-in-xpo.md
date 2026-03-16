---
uid: "113545"
seealso: []
title: BLOB Image Properties in XPO
owner: Ekaterina Kiseleva
---
# BLOB Image Properties in XPO

You can declare [image properties](xref:113544) as byte arrays or `MediaDataObject` type [reference properties](xref:113572) (this type is available in the [Business Class Library](xref:112571)).

## Image as a Byte Array
The example below illustrates how to implement byte array type image properties in an XPO persistent class by declaring a [byte](https://learn.microsoft.com/en-us/dotnet/api/system.byte) [array](https://learn.microsoft.com/en-us/dotnet/api/system.array) property and applying the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) to it. You can also customize the image editor using the attribute's parameters.

# [C#](#tab/tabid-csharp)

```csharp
[VisibleInListView(true)]
[ImageEditor(ListViewImageEditorMode = ImageEditorMode.PictureEdit, 
    DetailViewImageEditorMode = ImageEditorMode.PictureEdit, 
    ListViewImageEditorCustomHeight = 40)]
public byte[] ImageProperty {
    get { return GetPropertyValue<byte[]>(nameof(ImageProperty)); }
    set { SetPropertyValue<byte[]>(nameof(ImageProperty), value); }
}
[Delayed(true), VisibleInListViewAttribute(true)]
[ImageEditor(ListViewImageEditorMode = ImageEditorMode.PopupPictureEdit, DetailViewImageEditorMode = ImageEditorMode.DropDownPictureEdit)]
public byte[] ImageDelayedProperty {
    get { return GetDelayedPropertyValue<byte[]>(nameof(ImageDelayedProperty)); }
    set { SetDelayedPropertyValue<byte[]>(nameof(ImageDelayedProperty), value); }
}
```
***

[!include[PE_ImageEditorNote](~/templates/pe_imageeditornote111109.md)]

> [!TIP]
> When an application displays a lot of large images in a List View, it may consume much memory. To improve the performance, you can use lazy loading.

## Image as a MediaDataObject
The example below illustrates how to implement @DevExpress.Persistent.BaseImpl.MediaDataObject type's image properties (available in the [Business Class Library](xref:112571)) in an XPO persistent class. Image Property Editors are used automatically for `MediaDataObject` type's properties; no attributes are required (however, you still can apply the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) to customize the editor's options, as it is demonstrated above for byte arrays). Using this type reduces traffic because images are cached in the browser cache (compared to byte[] type images). Delayed loading is always used for `MediaDataObject` properties.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Xpo;
using DevExpress.Persistent.BaseImpl;
// ...
[DefaultClassOptions]
public class Contact : BaseObject {
    public Contact(Session session) : base(session) { }
    private string name;
    public string Name {
        get { return name; }
        set { SetPropertyValue(nameof(Name), ref name, value); }
    }
    private MediaDataObject image;
    public MediaDataObject Image {
        get { return image; }
        set { SetPropertyValue(nameof(Image), ref image, value); }
    }
}
```
***
