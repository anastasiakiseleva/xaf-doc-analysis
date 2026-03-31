---
uid: "113542"
title: Boolean Properties in EF Core
seealso: 
- linkId: "117395"
---
# Boolean Properties in EF Core

The example below illustrates how to implement [Boolean Properties](xref:113540) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
// By default, a Boolean property is displayed via a CheckEdit control.
public virtual bool BooleanProperty { get; set; }

// To use a drop-down control, specify captions with the CaptionsForBoolValues attribute.
[CaptionsForBoolValues("TRUE", "FALSE")]
public virtual bool BooleanWithCaptions { get; set; }

// To display images in a drop-down, apply the ImagesForBoolValues attribute.
[ImagesForBoolValues("ImageForTrue", "ImageForFalse")]
[CaptionsForBoolValues("TRUE", "FALSE")]
public virtual bool BooleanWithImages { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

[!include[BoolOptionsInME](~/templates/booloptionsinme111108.md)]