---
uid: DevExpress.Persistent.BaseImpl.EF.BaseObject.EvaluateAlias``1(System.String)
name: EvaluateAlias<T>(String)
type: Method
summary: Calculates the value of a calculated property whose name is specified by the `propertyName` parameter. The expression used in calculation must be specified through the [`PersistentAlias`](xref:DevExpress.ExpressApp.DC.PersistentAliasAttribute) or [`Calculated`](xref:DevExpress.ExpressApp.DC.CalculatedAttribute) attribute.
syntax:
  content: protected T EvaluateAlias<T>(string propertyName = null)
  parameters:
  - id: propertyName
    type: System.String
    defaultValue: "null"
    description: Specifies the name of a property value to be calculated.
  typeParameters:
  - id: T
    description: The calculated property value type.
  return:
    type: '{T}'
    description: The calculated property value.
seealso:
- linkId: DevExpress.ExpressApp.DC.PersistentAliasAttribute
- linkId: "405280"
---

Use the `EvaluateAlias` method to calculate the value of a calculated property. 

The `propertyName` parameter specifies the name of a property value to be calculated. If this parameter is not specified and the `EvaluateAlias` method is called in a property getter, the `propertyName` parameter is automatically set to this property's name.

The following code snippet uses the `EvaluateAlias` method:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Model;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

[DefaultClassOptions]
public class Payment : BaseObject {
    public virtual decimal Rate { get; set; }
    public virtual float Hours { get; set; }

    [PersistentAlias("Rate * Hours")]
    public decimal Amount {
        // Ensure that the type parameter `T` is set to the type 
        // that matches the calculated expression result type.
        get { return EvaluateAlias<decimal>(); }
    }
}
```

***
