---
uid: "113541"
seealso: []
title: Boolean Properties in XPO
---
# Boolean Properties in XPO

The example below illustrates how to implement [Boolean Properties](xref:113540) in an XPO persistent class.

# [C#](#tab/tabid-csharp)

```csharp
// By default, a Boolean property is displayed via a CheckEdit control.
public bool BooleanProperty {
    get { return booleanProperty; }
    set { SetPropertyValue(nameof(BooleanProperty), ref booleanProperty, value); }
}
// To use a drop-down control, specify captions with the CaptionsForBoolValues attribute.
private bool booleanWithCaptions;
[CaptionsForBoolValues("TRUE", "FALSE")]
public bool BooleanWithCaptions {
    get { return booleanWithCaptions; }
    set { SetPropertyValue(nameof(BooleanWithCaptions), ref booleanWithCaptions, value); }
}
// To display images in a drop-down, apply the ImagesForBoolValues attribute.
private bool booleanWithImages;
[ImagesForBoolValues("ImageForTrue", "ImageForFalse")]
[CaptionsForBoolValues("TRUE", "FALSE")]
public bool BooleanWithImages {
    get { return booleanWithImages; }
    set { SetPropertyValue(nameof(BooleanWithImages), ref booleanWithImages, value); }
}
```
***

[!include[BoolOptionsInME](~/templates/booloptionsinme111108.md)]