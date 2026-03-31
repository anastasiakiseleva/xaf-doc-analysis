---
uid: "113538"
title: Date and Time Properties in EF Core
seealso:  
- linkId: "117395"
---
# Date and Time Properties in EF Core

The following code snippet implements [Date and Time Properties](xref:113536) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
public virtual DateTime DateTimeProperty { get; set; }
public virtual DateTime? DateTimeNullableProperty { get; set; }
public virtual TimeSpan TimeSpanProperty { get; set; }
public virtual TimeSpan? TimeSpanNullableProperty { get; set; }
public virtual DateOnly DateOnlyProperty { get; set; }
public virtual DateOnly? DateOnlyNullableProperty { get; set; }
public virtual TimeOnly TimeOnlyProperty { get; set; }
public virtual TimeOnly? TimeOnlyNullableProperty { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***