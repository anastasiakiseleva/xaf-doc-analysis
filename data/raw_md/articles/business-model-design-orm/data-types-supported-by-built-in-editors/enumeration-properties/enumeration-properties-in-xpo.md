---
uid: "113553"
seealso:
- linkId: "113563"
title: Enumeration Properties in XPO
---
# Enumeration Properties in XPO

The example below illustrates how to implement [Enumeration Properties](xref:113552) in an XPO persistent class.

# [C#](#tab/tabid-csharp)

```csharp
private TextOnlyEnum textOnlyEnumProperty;
public TextOnlyEnum TextOnlyEnumProperty {
    get { return textOnlyEnumProperty; }
    set { SetPropertyValue(nameof(TextOnlyEnumProperty), ref textOnlyEnumProperty, value); }
}
private TextAndImageEnum textAndImageEnumProperty;
public TextAndImageEnum TextAndImageEnumProperty {
    get { return textAndImageEnumProperty; }
    set { SetPropertyValue(nameof(TextAndImageEnumProperty), ref textAndImageEnumProperty, value); }
}
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
```

# [VB.NET](#tab/tabid-vb)

```vb
Private _textOnlyEnumProperty As TextOnlyEnum
Public Property TextOnlyEnumProperty() As TextOnlyEnum
    Get
        Return _textOnlyEnumProperty
    End Get
    Set(ByVal value As TextOnlyEnum)
        SetPropertyValue(NameOf(TextOnlyEnumProperty), _textOnlyEnumProperty, value)
    End Set
End Property
Private _textAndImageEnumProperty As TextAndImageEnum
Public Property TextAndImageEnumProperty() As TextAndImageEnum
    Get
        Return _textAndImageEnumProperty
    End Get
    Set(ByVal value As TextAndImageEnum)
        SetPropertyValue(NameOf(TextAndImageEnumProperty), _textAndImageEnumProperty, value)
    End Set
End Property
' ...
Public Enum TextOnlyEnum
    Minor
    Moderate
    Severe
End Enum
Public Enum TextAndImageEnum
    <ImageName("State_Priority_Low")>
    Low
    <ImageName("State_Priority_Normal")>
    Normal
    <ImageName("State_Priority_High")>
    High
End Enum
```

***