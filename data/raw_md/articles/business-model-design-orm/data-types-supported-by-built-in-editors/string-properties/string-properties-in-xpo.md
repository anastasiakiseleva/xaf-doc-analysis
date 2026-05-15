---
uid: "113529"
seealso:
- linkId: DevExpress.Xpo.SizeAttribute
- linkId: DevExpress.Xpo.DelayedAttribute
- linkId: DevExpress.ExpressApp.Model.ModelDefaultAttribute
- linkId: DevExpress.Xpo.Metadata.ValueConverter
title: String Properties in XPO
---
# String Properties in XPO

The example below illustrates how to implement [String Properties](xref:113528) in an XPO persistent class.

# [C#](#tab/tabid-csharp)

```csharp
// By default, the string property size is 100.
private string defaulSizeStringProperty;
public string DefaultSizeStringProperty {
    get { return defaulSizeStringProperty; }
    set { SetPropertyValue(nameof(DefaultSizeStringProperty), ref defaulSizeStringProperty, value); }
}
// The string property size is limited to 15.
private string shortSizeStringProperty;
[Size(15)]
public string ShortSizeStringProperty {
    get {
        return shortSizeStringProperty;
    }
        set { SetPropertyValue(nameof(ShortSizeStringProperty), ref shortSizeStringProperty, value); }
}
// The string property size is unlimited. It is displayed via a memo editor.
// By default, this property is not displayed in List View. You can make its column visible with the VisibleInListView attribute.
private string unlimitedSizeStringProperty;
[Size(SizeAttribute.Unlimited), VisibleInListView(true)]
public string UnlimitedSizeStringProperty {
    get {
        return unlimitedSizeStringProperty;
    }
    set { 
        SetPropertyValue(nameof(UnlimitedSizeStringProperty), ref unlimitedSizeStringProperty, value);
    }
}
// Delayed loading and compression are applied to this property.
private XPDelayedProperty compressedUnlimitedStringProperty = new XPDelayedProperty();
[Delayed(nameof(compressedUnlimitedStringProperty)), ValueConverter(typeof(StringCompressionConverter))]
public string CompressedUnlimitedStringProperty {
    get { return (string)compressedUnlimitedStringProperty.Value; }
    set { 
        compressedUnlimitedStringProperty.Value = value;
        OnChanged(nameof(CompressedUnlimitedStringProperty));
    }
}
// This property has a list of predefined values.
private string stringWithPredefinedValuesProperty;
[ModelDefault("PredefinedValues", "Predefined Value 1;Predefined Value 2;Predefined Value 3;Predefined Value 4;Predefined Value 5")]
public string StringWithPredefinedValuesProperty {
    get { return stringWithPredefinedValuesProperty; }
    set { stringWithPredefinedValuesProperty = value; }
}
// This property is displayed in the Rich Text Editor.
private string richTextProperty;
[Size(SizeAttribute.Unlimited)]
[EditorAlias(EditorAliases.RichTextPropertyEditor)] 
public string RichTextProperty { 
    get { return richTextProperty; }
    set { SetPropertyValue(nameof(RichTextProperty), ref richTextProperty, value); }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
' By default, the string property size is 100.
Private defaulSizeStringProperty As String
Public Property DefaultSizeStringProperty() As String
    Get
        Return defaulSizeStringProperty
    End Get
    Set(ByVal value As String)
        SetPropertyValue(NameOf(DefaultSizeStringProperty), defaulSizeStringProperty, value)
    End Set
End Property
' The string property size is limited to 15.
Private _shortSizeStringProperty As String
<Size(15)>
Public Property ShortSizeStringProperty() As String
    Get
        Return _shortSizeStringProperty
    End Get
        Set(ByVal value As String)
            SetPropertyValue(NameOf(ShortSizeStringProperty), _shortSizeStringProperty, value)
        End Set
End Property
' The string property size is unlimited. It is displayed via a memo editor.
' By default, this property is not displayed in List View. You can make its column visible with the VisibleInListView attribute.
Private _unlimitedSizeStringProperty As String
<Size(SizeAttribute.Unlimited), VisibleInListView(True)>
Public Property UnlimitedSizeStringProperty() As String
    Get
        Return _unlimitedSizeStringProperty
    End Get
    Set(ByVal value As String)
        SetPropertyValue(NameOf(UnlimitedSizeStringProperty), _unlimitedSizeStringProperty, value)
    End Set
End Property
' Delayed loading and compression are applied to this property.
Private _compressedUnlimitedStringProperty As New XPDelayedProperty()
<Delayed(NameOf(_compressedUnlimitedStringProperty)), ValueConverter(GetType(StringCompressionConverter))>
Public Property CompressedUnlimitedStringProperty() As String
    Get
        Return CStr(_compressedUnlimitedStringProperty.Value)
    End Get
    Set(ByVal value As String)
        _compressedUnlimitedStringProperty.Value = value
        OnChanged(NameOf(CompressedUnlimitedStringProperty))
    End Set
End Property
' This property has a list of predefined values.
Private _stringWithPredefinedValuesProperty As String
<ModelDefault("PredefinedValues", "Predefined Value 1;Predefined Value 2;Predefined Value 3;Predefined Value 4;Predefined Value 5")>
Public Property StringWithPredefinedValuesProperty() As String
    Get
        Return _stringWithPredefinedValuesProperty
    End Get
    Set(ByVal value As String)
        _stringWithPredefinedValuesProperty = value
    End Set
End Property
' This property is displayed in the Rich Text Editor.
Private _richTextProperty As String
<Size(SizeAttribute.Unlimited), EditorAlias(EditorAliases.RichTextPropertyEditor)>
Public Property RichTextProperty() As String
	Get
		Return _richTextProperty
	End Get
	Set(ByVal value As String)
		SetPropertyValue(NameOf(RichTextProperty), _richTextProperty, value)
	End Set
End Property
```
***