---
uid: DevExpress.Persistent.Base.UseInAuditTrailAttribute
name: UseInAuditTrailAttribute
type: Class
summary: Specifies whether a property takes part in audit.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property | AttributeTargets.Field, AllowMultiple = false)]
    public class UseInAuditTrailAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.UseInAuditTrailAttribute._members
  altText: UseInAuditTrailAttribute Members
---
The `UseInAuditTrailAttribute` is a part of [Audit Trail Module](xref:112782) functionality and specifies whether a property participates in the audit. You can use this attribute to customize the default Audit Trail module behavior.

### Default Audit Trail Module Behavior

The Audit Trail Module [logs changes](xref:112782#tracked-changes) in the following objects and properties:

* Persistent classes.
* Public writable simple and reference properties defined in persistent classes.
* Public collection properties defined in persistent classes.

Read-only properties (those without a setter) and properties decorated with the @DevExpress.Xpo.NonPersistentAttribute are excluded from the audit trail.

### Exclude a Property from the Audit Trail

Apply the `UseInAuditTrailAttribute` with its `Include` parameter set to `false` to stop logging property changes:

# [C# (EF Core)](#tab/tabid-csharp-ef)
```csharp
[UseInAuditTrail(false)]
public virtual string MyPersistentProperty { get; set; }
```
# [C# (XPO)](#tab/tabid-csharp-xpo)
```csharp
[UseInAuditTrail(false)]
public string MyPersistentProperty { 
    get { return myPersistentProperty; }
    set { SetPropertyValue(nameof(MyPersistentProperty), ref myPersistentProperty, value); }
}
```
***

### Include a Non-Persistent Property in the Audit Trail

To log changes in a non-persistent property, apply the `UseInAuditTrailAttribute` with its `Include` parameter set to `true`:

# [C# (EF Core)](#tab/tabid-csharp-ef)
```csharp
[UseInAuditTrail(true)]
[NotMapped]
public string MyNonPersistentProperty { get; set; }
```
# [C# (XPO)](#tab/tabid-csharp-xpo)
```csharp
[UseInAuditTrail(true)]
[NonPersistent]
public string MyNonPersistentProperty {
    get { return myNonPersistentProperty; }
    set { SetPropertyValue(nameof(MyNonPersistentProperty), ref myNonPersistentProperty, value); }
}
```
***