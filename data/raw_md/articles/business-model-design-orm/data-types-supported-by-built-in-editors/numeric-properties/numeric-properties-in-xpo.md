---
uid: "113533"
seealso: []
title: Numeric Properties in XPO
---
# Numeric Properties in XPO

The example below illustrates how to implement [Numeric Properties](xref:113532) in an XPO persistent class.

# [C#](#tab/tabid-csharp)

```csharp
private double doubleProperty;
public double DoubleProperty {
    get { return doubleProperty; }
    set { SetPropertyValue(nameof(DoubleProperty), ref doubleProperty, value); }
}
private float singleProperty;
public float SingleProperty {
    get { return singleProperty; }
    set { SetPropertyValue(nameof(SingleProperty), ref singleProperty, value); }
}
private long longProperty;
public long LongProperty {
    get { return longProperty; }
    set { SetPropertyValue(nameof(LongProperty), ref longProperty, value); }
}
private int integerProperty;
public int IntegerProperty {
    get { return integerProperty; }
    set { SetPropertyValue(nameof(IntegerProperty), ref integerProperty, value); }
}
private decimal decimalProperty;
public decimal DecimalProperty {
    get { return decimalProperty; }
    set { SetPropertyValue(nameof(DecimalProperty), ref decimalProperty, value); }
}
private byte byteProperty;
public byte ByteProperty {
    get { return byteProperty; }
    set { SetPropertyValue(nameof(ByteProperty), ref byteProperty, value); }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Private _doubleProperty As Double
Public Property DoubleProperty() As Double
    Get
        Return _doubleProperty
    End Get
    Set(ByVal value As Double)
        SetPropertyValue(NameOf(DoubleProperty), _doubleProperty, value)
    End Set
End Property
Private _singleProperty As Single
Public Property SingleProperty() As Single
    Get
        Return _singleProperty
    End Get
    Set(ByVal value As Single)
        SetPropertyValue(NameOf(SingleProperty), _singleProperty, value)
    End Set
End Property
Private _longProperty As Long
Public Property LongProperty() As Long
    Get
        Return _longProperty
    End Get
    Set(ByVal value As Long)
        SetPropertyValue(NameOf(LongProperty), _longProperty, value)
    End Set
End Property
Private _integerProperty As Integer
Public Property IntegerProperty() As Integer
    Get
        Return _integerProperty
    End Get
    Set(ByVal value As Integer)
        SetPropertyValue(NameOf(IntegerProperty), _integerProperty, value)
    End Set
End Property
Private _decimalProperty As Decimal
Public Property DecimalProperty() As Decimal
    Get
        Return _decimalProperty
    End Get
    Set(ByVal value As Decimal)
        SetPropertyValue(NameOf(DecimalProperty), _decimalProperty, value)
    End Set
End Property
Private _byteProperty As Byte
Public Property ByteProperty() As Byte
    Get
        Return _byteProperty
    End Get
    Set(ByVal value As Byte)
        SetPropertyValue(NameOf(ByteProperty), _byteProperty, value)
    End Set
End Property
```

***