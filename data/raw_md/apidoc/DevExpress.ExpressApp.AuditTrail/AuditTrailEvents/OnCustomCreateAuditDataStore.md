---
uid: DevExpress.ExpressApp.AuditTrail.AuditTrailEvents.OnCustomCreateAuditDataStore
name: OnCustomCreateAuditDataStore
type: Property
summary: Specifies a delegate method that creates a custom data store for audit trails.
syntax:
  content: public Action<CustomCreateAuditDataStoreContext> OnCustomCreateAuditDataStore { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.AuditTrail.CustomCreateAuditDataStoreContext}
    description: A delegate method that takes the event context object as an argument.
seealso:
- linkId: "403115"
- linkId: "112783"
---

Use this property to specify a custom audit data store (an **AuditDataStore** descendant):

**File:** _MySolution.WebApi\startup.cs_ (_MySolution.Blazor.Server\startup.cs_)

# [C#](#tab/tabid-cs)
```csharp
builder.Modules
    .AddAuditTrailXpo(options => {
        options.Events.OnCustomCreateAuditDataStore = (context) => {
            context.AuditDataStore = new CustomAuditDataStore();
        };
    })
```
***

You can also register the audit trail services directly as the code below demonstrates:

**File:** _MySolution.WebApi\startup.cs_ (_MySolution.Blazor.Server\startup.cs_)

# [C#](#tab/tabid-cs)
```csharp
services
    .AddAuditTrailXpoServices(options => {
        options.Events.OnCustomCreateAuditDataStore = (context) => {
            context.AuditDataStore = new CustomAuditDataStore();
        };
    })
```
***
