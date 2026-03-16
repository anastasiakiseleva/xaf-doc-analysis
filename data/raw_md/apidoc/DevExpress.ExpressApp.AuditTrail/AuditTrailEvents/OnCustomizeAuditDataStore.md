---
uid: DevExpress.ExpressApp.AuditTrail.AuditTrailEvents.OnCustomizeAuditDataStore
name: OnCustomizeAuditDataStore
type: Property
summary: Specifies a delegate method that applies customization logic to the audit data store.
syntax:
  content: public Action<CustomizeAuditDataStoreContext> OnCustomizeAuditDataStore { get; set; }
  parameters: []
  return:
    type: System.Action{DevExpress.ExpressApp.AuditTrail.CustomizeAuditDataStoreContext}
    description: A delegate method that takes the event context object as an argument.
seealso:
- linkId: "403115"
- linkId: "112783"
---

Use this property to customize the audit data store's settings. For example, the code below demonstrates how to specify a custom null value string for the audit data store:

**File:** _MySolution.WebApi\startup.cs_ (_MySolution.Blazor.Server\startup.cs_)

# [C#](#tab/tabid-cs)
```csharp
builder.Modules
    .AddAuditTrailXpo(options => {
        options.Events.OnCustomizeAuditDataStore = (context) => {
            context.AuditDataStore.NullValueString = "CustomNullValueString";
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
        options.Events.OnCustomizeAuditDataStore = (context) => {
            context.AuditDataStore.NullValueString = "CustomNullValueString";
        };
    })
```
***
