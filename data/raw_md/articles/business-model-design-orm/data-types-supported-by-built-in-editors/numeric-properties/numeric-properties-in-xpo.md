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
***