---
uid: DevExpress.ExpressApp.DC.CalculatedAttribute
name: CalculatedAttribute
type: Class
summary: Applies to business class properties. Specifies an [expression](xref:4928) used to calculate the target property value.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = true)]
    public class CalculatedAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DC.CalculatedAttribute._members
  altText: CalculatedAttribute Members
- linkId: xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.EvaluateAlias``1(System.String)
---

Use the `CalculatedAttribute` to specify an expression used to calculate the value of a calculated property.

In an EF Core business class, a property decorated with the `CalculatedAttribute` works as a regular property in all [data access modes](xref:113683). Note that for an EF Core class property, the `CalculatedAttribute` has the same effect as the @DevExpress.ExpressApp.DC.PersistentAliasAttribute.

In an XPO business class, a decorated property's calculated value is correctly displayed only in the **Data View** mode.

> [!IMPORTANT]
>
> It is not recommended to use the `CalculatedAttribute` in XPO business classes. Use the [PersistentAlias](xref:DevExpress.Xpo.PersistentAliasAttribute) attribute instead.

The following code snippet uses the `CalculatedAttribute`:

# [C# (EF Core)](#tab/tabid-csharp-efcore)

```csharp
using DevExpress.ExpressApp.DC;
// ...
public class Person : BaseObject {
    // ...
    public virtual String FirstName { get; set; }
    public virtual String LastName { get; set; }
    [Calculated("Concat(FirstName, ' ', LastName)")]
    public String FullName {
        get {
            get { return EvaluateAlias<String>(); }
        }
    }
}
// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO, Non-Persistent)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.DC;
// ...
public class Person {    
    // ...
    public virtual String FirstName { get; set; }
    public virtual String LastName { get; set; }
    [Calculated("Concat(FirstName, ' ', LastName)")]
    public String FullName {
        get {
            return string.Concat(FirstName, " ", LastName);
        }
    }
}

```
***

[`EvaluateAlias`]: xref:DevExpress.Persistent.BaseImpl.EF.BaseObject.EvaluateAlias``1(System.String) 

The expression specified through the [CalculatedAttribute.Expression](xref:DevExpress.ExpressApp.DC.CalculatedAttribute.Expression) parameter is calculated on the database server side. The expression can reference persistent properties, other calculated properties, or criteria functions that can be executed by the database server through SQL.
