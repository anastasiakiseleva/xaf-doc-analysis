---
uid: "402081"
title: 'Customize the Data Storing Mechanism'
owner: Yekaterina Kiseleva
---

# Customize the Data Storing Mechanism

The [Audit Trail Module](xref:112782) stores audit records (`AuditDataItem` objects) in an application database. The [SaveAuditTrailData](xref:DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.SaveAuditTrailData) event allows you to configure how this Module saves information. This event is raised when the Module commits an `AuditDataItem` object to the database. In this event handler, you can modify the `SaveAuditTrailDataContext.AuditTrailDataItems` collection, and add new or remove unnecessary items. The following code snippet removes `ObjectCreated` records.

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomizeAuditOperationTypeFilter = context => {
            if (context.AuditOperationType == AuditOperationType.ObjectChanged ||
                context.AuditOperationType == AuditOperationType.ObjectCreated) {
                context.SaveAuditOperation = false;
            }
        };
    })
```

***

## Replace the Default Data Storing Mechanism with a Custom Mechanism

To do this, set the event's `SaveAuditTrailDataContext.Handled` argument to `true` in the `SaveAuditTrailData` event handler. 

**File:** _MySolution.Blazor.Server\Startup.cs_, _MySolution.Win\Startup.cs_, _MySolution.WebApi\Startup.cs_

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.AuditTrail;
// ...
builder.Modules
    .AddAuditTrailXpo(o => {
        o.Events.OnCustomizeAuditOperationTypeFilter = context => {
            // Save the data passed as the `context.AuditTrailDataItems` parameter
            context.Handled = true; // Disable the default data storing mechanism
        };
    })
```

***

## Alternative Techniques

* If you do not want to log specific operations, implement the technique described in the [Audit Specific Operations](xref:402082) topic.
* You can create the `AuditDataStore` descendant and override its `Save` method. Register this custom data store within the Audit Trail system as described in the following topic: [](xref:112783#customize-the-blob-properties-storage-mechanism).