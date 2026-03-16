---
uid: "113530"
title: String Properties in EF Core
owner: Ekaterina Kiseleva
seealso:  
- linkId: "117395"
---
# String Properties in EF Core

The example below illustrates how to implement [String Properties](xref:113528) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
// By default, the string property size is 100.
public virtual string DefaultSizeStringProperty { get; set; }

// The string property size is limited to 15.
[FieldSize(15)]
public virtual string ShortSizeStringProperty { get; set; }

// The string property size is unlimited. It is displayed via a memo editor.
// By default, this property is not displayed in List View. You can make its column visible via the VisibleInListView attribute.
[FieldSize(FieldSizeAttribute.Unlimited)]
[VisibleInListView(true)]
public virtual string UnlimitedSizeStringProperty { get; set; }

// The property has a list of predefined values.
[ModelDefault("PredefinedValues",
    "Predefined Value 1;Predefined Value 2;Predefined Value 3;Predefined Value 4;Predefined Value 5")]
public virtual string StringWithPredefinedValuesProperty { get; set; }

// This property is displayed in the Rich Text Editor.
[FieldSize(FieldSizeAttribute.Unlimited)]
[EditorAlias(EditorAliases.RichTextPropertyEditor)]
public virtual string RichTextProperty { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***