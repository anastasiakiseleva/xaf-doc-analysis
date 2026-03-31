---
uid: "113546"
seealso:
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.schema.notmappedattribute
  altText: NotMappedAttribute
- linkType: HRef
  linkId: https://learn.microsoft.com/en-us/dotnet/api/system.drawing.imageconverter
  altText: ImageConverter
- linkId: "117395"
title: BLOB Image Properties in EF Core
---
# BLOB Image Properties in EF Core

You can declare [image properties](xref:113544) as a byte array property, or as a [reference properties](xref:113572) of the `MediaDataObject` type (available in the [Business Class Library](xref:112571)).

## Image as a Byte Array

The example below illustrates how to implement image properties in an Entity Framework Core Code-First class. Declare a [byte](https://learn.microsoft.com/en-us/dotnet/api/system.byte) [array](https://learn.microsoft.com/en-us/dotnet/api/system.array) property and apply the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) to it. Optionally, you can customize the behavior of the image editor using the attribute's parameters.

# [C#](#tab/tabid-csharp)

```csharp
using System.Drawing;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations.Schema;
// ...
[DefaultClassOptions]
public class Employee : BaseObject {
    [ImageEditor(ListViewImageEditorMode = ImageEditorMode.PopupPictureEdit,
        DetailViewImageEditorMode = ImageEditorMode.DropDownPictureEdit)]
    public virtual byte[] Photo { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

[!include[PE_ImageEditorNote](~/templates/pe_imageeditornote111109.md)]

> [!TIP]
> When an application displays a lot of large images in a List View, it may consume a lot of memory. To improve the performance, you can use lazy loading.

## Image as a MediaDataObject
The example below illustrates how to implement image properties of the @DevExpress.Persistent.BaseImpl.EF.MediaDataObject type (available in the [Business Class Library](xref:112571)) in an Entity Framework Core class. Image Property Editors are used automatically for properties of the `MediaDataObject` type, no attributes are required (however, you still can apply the [](xref:DevExpress.Persistent.Base.ImageEditorAttribute) to customize the editor's options, as it is demonstated above for byte arrays). The use of this type reduces traffic because images are cached in the browser cache (compared to images of the byte[] type). The delayed loading is always used for `MediaDataObject` properties.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
// ...
[DefaultClassOptions]
public class Contact : BaseObject {
    // ...
    public virtual string Name { get; set; }
    public virtual MediaDataObject Photo { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***
