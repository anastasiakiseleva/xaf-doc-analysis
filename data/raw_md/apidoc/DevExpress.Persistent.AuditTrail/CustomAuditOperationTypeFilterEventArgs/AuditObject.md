---
uid: DevExpress.Persistent.AuditTrail.CustomAuditOperationTypeFilterEventArgs.AuditObject
name: AuditObject
type: Field
summary: A modified object.
syntax:
  content: public readonly object AuditObject
  return:
    type: System.Object
    description: A modified object.
seealso: []
---

The following example obtains this field value:

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp-blazor)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomizeAuditOperationTypeFilter = context => {
            Contact contact = context.AuditObject as Contact;
            // ...
        };
    })
```

***
