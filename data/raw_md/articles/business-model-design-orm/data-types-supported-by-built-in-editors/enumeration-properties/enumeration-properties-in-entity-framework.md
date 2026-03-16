---
uid: "113554"
seealso:
- linkId: "113563" 
- linkId: "117395"
title: Enumeration Properties in EF Core
owner: Ekaterina Kiseleva
---
# Enumeration Properties in EF Core

The example below illustrates how to implement [Enumeration Properties](xref:113552) in an EF Core Code-First class.

# [C#](#tab/tabid-csharp)

```csharp
public virtual TextOnlyEnum TextOnlyEnumProperty { get; set; }
public virtual TextAndImageEnum TextAndImageEnumProperty { get; set; }
// ...
public enum TextOnlyEnum { Minor, Moderate, Severe }
public enum TextAndImageEnum {
    [ImageName("State_Priority_Low")]
    Low,
    [ImageName("State_Priority_Normal")]
    Normal,
    [ImageName("State_Priority_High")]
    High 
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

To be able to use this enumeration type in design-time [criteria editors](xref:113564), register it in the constructor of your [](xref:DevExpress.ExpressApp.ModuleBase) descendant using the [EnumProcessingHelper.RegisterEnum](xref:DevExpress.Data.Filtering.EnumProcessingHelper.RegisterEnum*) method as follows.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
//...
public sealed partial class MySolutionModule : ModuleBase {
    public MySolutionModule() {
        InitializeComponent();
        EnumProcessingHelper.RegisterEnum(typeof(MySolution.Module.BusinessObjects.MyClass.TextOnlyEnum));
        //...
    }
    //...
}
```

***