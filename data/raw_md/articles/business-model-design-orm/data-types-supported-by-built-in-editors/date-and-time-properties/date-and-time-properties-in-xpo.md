---
uid: "113537"
seealso: []
title: Date and Time Properties in XPO
---
# Date and Time Properties in XPO

The following code snippet implements [Date and Time Properties](xref:113536) in an XPO persistent class.

```csharp
private DateTime dateTimeProperty;
public DateTime DateTimeProperty {
    get { return dateTimeProperty; }
    set { SetPropertyValue(nameof(DateTimeProperty), ref dateTimeProperty, value); }
}
private DateTime? dateTimeNullableProperty;
public DateTime? DateTimeNullableProperty {
    get { return dateTimeNullableProperty; }
    set { SetPropertyValue(nameof(DateTimeNullableProperty), ref dateTimeNullableProperty, value); }
}
private DateOnly dateOnlyProperty;
public DateOnly DateOnlyProperty {
    get { return dateOnlyProperty; }
    set { SetPropertyValue(nameof(DateOnlyProperty), ref dateOnlyProperty, value); }
}
private DateOnly? dateOnlyNullableProperty;
public DateOnly? DateOnlyNullableProperty {
    get { return dateOnlyNullableProperty; }
    set { SetPropertyValue(nameof(DateOnlyNullableProperty), ref dateOnlyNullableProperty, value); }
}
private TimeSpan timeSpanProperty;
public TimeSpan TimeSpanProperty {
    get { return timeSpanProperty; }
    set { SetPropertyValue(nameof(TimeSpanProperty), ref timeSpanProperty, value); }
}
private TimeSpan? timeSpanNullableProperty;
public TimeSpan? TimeSpanNullableProperty {
    get { return timeSpanNullableProperty; }
    set { SetPropertyValue(nameof(TimeSpanNullableProperty), ref timeSpanNullableProperty, value); }
}
private TimeOnly timeOnlyProperty;
public TimeOnly TimeOnlyProperty {
    get { return timeOnlyProperty; }
    set { SetPropertyValue(nameof(TimeOnlyProperty), ref timeOnlyProperty, value); }
}
private TimeOnly? timeOnlyNullableProperty;
public TimeOnly? TimeOnlyNullableProperty {
    get { return timeOnlyNullableProperty; }
    set { SetPropertyValue(nameof(TimeOnlyNullableProperty), ref timeOnlyNullableProperty, value); }
}
```
