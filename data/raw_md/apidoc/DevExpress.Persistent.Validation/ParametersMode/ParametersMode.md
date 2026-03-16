---
uid: DevExpress.Persistent.Validation.ParametersMode
name: ParametersMode
type: Enum
summary: Contains values specifying how criteria string parameters used in [](xref:DevExpress.Persistent.Validation.RuleRangeAttribute) and [](xref:DevExpress.Persistent.Validation.RuleValueComparisonAttribute) constructors are treated.
syntax:
  content: public enum ParametersMode
seealso: []
---
The following example demonstrates how to pass this enumeration value to the **RuleRange** attribute:

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using System;
using DevExpress.Persistent.Validation;
//...
[RuleRange("LastSevenDays_RuleRange", "Save", "AddDays(LocalDateTimeToday(), -7)", 
    "LocalDateTimeToday()", ParametersMode.Expression)]
public virtual DateTime LastSevenDays { get; set; }

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using System;
using DevExpress.Persistent.Validation;
//...
private DateTime lastSevenDays;
[RuleRange("LastSevenDays_RuleRange", "Save", "AddDays(LocalDateTimeToday(), -7)", 
    "LocalDateTimeToday()", ParametersMode.Expression)]
public DateTime LastSevenDays {
    get { return lastSevenDays; }
    set { SetPropertyValue(nameof(LastSevenDays), ref lastSevenDays, value); }
}
//...
```
***