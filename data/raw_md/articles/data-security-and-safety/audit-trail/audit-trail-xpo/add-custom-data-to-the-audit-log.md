---
uid: "402077"
title: 'Add Custom Data to the Audit Log'
---
# Add Custom Data to the Audit Log
Object changes are stored as `AuditDataItem` objects (see [Audit Trail Module Overview](xref:112782)). You can add custom data (information on events that are not audited) to the audit log directly by adding an `AuditDataItem` object to the Audit Data Items collection. The following code snippet demonstrates this scenario:

# [C# (.NET)](#tab/tabid-csharp-net6)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;
// ...
var auditTrailService = serviceProvider.GetRequiredService<AuditTrailService>();
AuditDataItem customDataItem = new AuditDataItem(myAuditedObject, null, 
    "CustomOldValue", "CustomNewValue", AuditOperationType.CustomData);
auditTrailService.AddCustomAuditData(mySession, customDataItem);
auditTrailService.SaveAuditData(mySession);
```
***

You can implement this code at any point in a program, for example, in a custom [Controller](xref:112621).

> [!NOTE]
> You should always invoke the [SaveAuditData](xref:DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.SaveAuditData(DevExpress.Xpo.Session)) method after adding custom audit data manually, without reusing the Session of the View's `ObjectSpace`. Otherwise, the audit data will not be written to the database.
