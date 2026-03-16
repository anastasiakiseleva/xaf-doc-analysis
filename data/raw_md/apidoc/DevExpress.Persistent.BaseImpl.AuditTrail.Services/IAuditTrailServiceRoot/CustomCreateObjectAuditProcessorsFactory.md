---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.IAuditTrailServiceRoot.CustomCreateObjectAuditProcessorsFactory
name: CustomCreateObjectAuditProcessorsFactory
type: Event
summary: Handle this event to replace a default `ObjectAuditProcessor` for a particular [object auditing mode](xref:402079) with a custom processor.
syntax:
  content: event EventHandler<CustomCreateObjectAuditProcessorsFactoryEventArgs> CustomCreateObjectAuditProcessorsFactory
seealso: []
---
The following code snippet handles this event:

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp-blazor)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomCreateObjectAuditProcessorsFactory = context => {
            context.ObjectAuditProcessorsFactory = new ObjectAuditProcessorsFactory(ObjectAuditingMode.Full,
                typeof(CustomAuditProcessor));
        };
    })
```

***

