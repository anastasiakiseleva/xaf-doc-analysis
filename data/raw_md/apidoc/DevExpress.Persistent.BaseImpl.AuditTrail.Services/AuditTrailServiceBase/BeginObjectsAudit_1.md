---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.BeginObjectsAudit(DevExpress.Xpo.Session,DevExpress.Persistent.AuditTrail.ObjectAuditingMode,System.Object[])
name: BeginObjectsAudit(Session, ObjectAuditingMode, Object[])
type: Method
summary: Starts auditing the specified objects according to _auditingMode_.
syntax:
  content: public void BeginObjectsAudit(Session session, ObjectAuditingMode auditingMode, params object[] alreadyLoadedObjects)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session object.
  - id: auditingMode
    type: DevExpress.Persistent.AuditTrail.ObjectAuditingMode
    description: The **ObjectAuditingMode** value that is the [object auditing mode](xref:402079). The default value is `Full`.
  - id: alreadyLoadedObjects
    type: System.Object[]
    description: Objects to be audited.
seealso: []
---
Call this method in non-XAF applications only.

# [C#](#tab/tabid-csharp-net6)

```csharp{14}
using DevExpress.ExpressApp;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;
// ...
var auditTrailService = serviceProvider.GetRequiredService<AuditTrailService>();
using var uow = new UnitOfWork(serviceProvider);
auditTrailService.BeginSessionAudit(uow, AuditTrailStrategy.OnObjectChanged, ObjectAuditingMode.Full);
NestedUnitOfWork nestedUow = uow.BeginNestedUnitOfWork();
PersistentObject1 obj = new PersistentObject1(nestedUow);
obj.Property1 = "1";
obj.Property2 = "2";
nestedUow.CommitChanges();
auditTrailService.BeginObjectsAudit(uow, ObjectAuditingMode.Lightweight, nestedUow.GetParentObject(obj));
uow.CommitChanges();
auditTrailService.SaveAuditData(uow);
```
***