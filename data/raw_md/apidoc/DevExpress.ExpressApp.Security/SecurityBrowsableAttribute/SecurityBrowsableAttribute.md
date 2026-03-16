---
uid: DevExpress.ExpressApp.Security.SecurityBrowsableAttribute
name: SecurityBrowsableAttribute
type: Class
summary: Applied to business class properties together with the [Browsable(false)](xref:System.ComponentModel.BrowsableAttribute) attribute. Unhides a hidden property in the [Member Permissions](xref:404633#member-permissions) configuration UI. The target property remains hidden in other places.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, AllowMultiple = false, Inherited = true)]
    public class SecurityBrowsableAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.Security.SecurityBrowsableAttribute._members
  altText: SecurityBrowsableAttribute Members
---
The following attributes combination makes the **MyProperty** property hidden everywhere except for the **Members** dropdown list in the [Member Permissions](xref:404633#member-permissions) tab.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[Browsable(false), SecurityBrowsable]
public virtual string MyProperty { get; set; }
```
# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
    [Browsable(false), SecurityBrowsable]
    public string MyProperty {
        get => myProperty;
        set => SetPropertyValue(nameof(MyProperty), ref myProperty, value);
    }
```

***