---
uid: DevExpress.ExpressApp.DC.XafDisplayNameAttribute
name: XafDisplayNameAttribute
type: Class
summary: Specifies the display name of a business class, property, field or enumeration value.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Interface, AllowMultiple = false, Inherited = true)]
    public sealed class XafDisplayNameAttribute : Attribute
seealso:
- linkId: DevExpress.ExpressApp.DC.XafDisplayNameAttribute._members
  altText: XafDisplayNameAttribute Members
---
The following snippet illustrates the **XafDisplayNameAttribute** usage.

# [C#](#tab/tabid-csharp)

```csharp
[XafDisplayName("Task")]
public class DemoTask : Task {
    // ...
}
```
***