---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.BeginObjectsAudit(DevExpress.Xpo.Session,System.Object[])
name: BeginObjectsAudit(Session, Object[])
type: Method
summary: Starts auditing the specified objects in `Full` [object auditing mode](xref:402079).
syntax:
  content: public void BeginObjectsAudit(Session session, params object[] alreadyLoadedObjects)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session to be audited.
  - id: alreadyLoadedObjects
    type: System.Object[]
    description: Objects to be audited.
seealso: []
---
`AuditTrailViewController` calls this method internally. 

# [C#](#tab/tabid-csharp-net6)

```csharp{14}
using DevExpress.ExpressApp;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;
// ...
var auditTrailService = serviceProvider.GetRequiredService<AuditTrailService>();
UnitOfWork uow = new UnitOfWork(serviceProvider);  
BeginSessionAudit(uow, AuditTrailStrategy.OnObjectChanged, ObjectAuditingMode.Full);  
NestedUnitOfWork nestedUow = uow.BeginNestedUnitOfWork();  
PersistentObject1 obj = new PersistentObject1(nestedUow);  
obj.Property1 = "1";  
obj.Property2 = "2";  
nestedUow.CommitChanges();  
BeginObjectsAudit(uow, nestedUow.GetParentObject(obj));
uow.CommitChanges();  
SaveAuditData(uow);  
```
***