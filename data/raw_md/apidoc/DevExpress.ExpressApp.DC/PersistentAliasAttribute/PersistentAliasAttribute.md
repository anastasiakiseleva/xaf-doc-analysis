---
uid: DevExpress.ExpressApp.DC.PersistentAliasAttribute
name: PersistentAliasAttribute
type: Class
summary: Applies to EF Core business class properties. Specifies an [expression](xref:4928) used to calculate the target property value.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = true)]
    public class PersistentAliasAttribute : CalculatedAttribute
seealso:
- linkId: DevExpress.ExpressApp.DC.PersistentAliasAttribute._members
  altText: PersistentAliasAttribute Members
- linkId: DevExpress.Persistent.BaseImpl.EF.BaseObject.EvaluateAlias``1(System.String)
  altText: EvaluateAlias
- linkId: "405280"
---

Use the `PersistentAliasAttribute` to specify an expression used to calculate the value of a calculated property.

In an EF Core business class, a property decorated with the `PersistentAliasAttribute` works like a regular property in all [data access modes](xref:113683). Note that for an EF Core class property, the `PersistentAliasAttribute` has the same effect as the @DevExpress.ExpressApp.DC.CalculatedAttribute.

The following code snippet uses the `PersistentAliasAttribute`:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
// ...
public class Person : BaseObject {
    // ...
    public virtual String FirstName { get; set; }
    public virtual String LastName { get; set; }
    [PersistentAlias("Concat(FirstName, ' ', LastName)")]
    public String FullName {
        get {
            get { return EvaluateAlias<String>(); }
        }
    }
}
// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```
***

The expression specified through the [CalculatedAttribute.Expression](xref:DevExpress.ExpressApp.DC.CalculatedAttribute.Expression) parameter is calculated on the database server side. The expression can reference persistent properties, other calculated properties, or criteria functions that can be executed by the database server through SQL.
