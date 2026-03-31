---
uid: "113534"
title: Numeric Properties in EF Core
seealso:  
- linkId: "117395"
---
# Numeric Properties in EF Core

The example below illustrates how to implement [Numeric Properties](xref:113532) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
public virtual double DoubleProperty { get; set; }
public virtual float SingleProperty { get; set; }
public virtual long LongProperty { get; set; }
public virtual int IntegerProperty { get; set; }
public virtual decimal DecimalProperty { get; set; }
public virtual byte ByteProperty { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***