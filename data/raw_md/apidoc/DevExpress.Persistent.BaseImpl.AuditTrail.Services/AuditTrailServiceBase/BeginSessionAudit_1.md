---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.BeginSessionAudit(DevExpress.Xpo.Session,DevExpress.Persistent.AuditTrail.AuditTrailStrategy,DevExpress.Persistent.AuditTrail.ObjectAuditingMode)
name: BeginSessionAudit(Session, AuditTrailStrategy, ObjectAuditingMode)
type: Method
summary: Starts auditing object changes made within the specified _session_.
syntax:
  content: public ObjectAuditProcessor BeginSessionAudit(Session session, AuditTrailStrategy strategy, ObjectAuditingMode auditingMode)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session to be audited.
  - id: strategy
    type: DevExpress.Persistent.AuditTrail.AuditTrailStrategy
    description: The `AuditTrailStrategy` value.
  - id: auditingMode
    type: DevExpress.Persistent.AuditTrail.ObjectAuditingMode
    description: The `ObjectAuditingMode` value that is the [object auditing mode](xref:402079). The default value is `Full`.
  return:
    type: DevExpress.Persistent.AuditTrail.ObjectAuditProcessor
    description: A processor that the Audit Trail Module uses for the specified _auditingMode_.
seealso: []
---
> [!Note]
> If you want to disable and enable the [Audit Trail Module](xref:112782) for a particular scenario, use solutions from the following help topic: [Disable the Audit Trail Module](xref:402080).

# [C#](#tab/tabid-csharp-net6)

```csharp{13-14}
using DevExpress.ExpressApp;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;
// ...
public partial class MyController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        var auditTrailService = Application.ServiceProvider.GetRequiredService<AuditTrailService>();
        Session session = ((XPObjectSpace)ObjectSpace).Session;
        auditTrailService.EndSessionAudit(session);
        // ...
        auditTrailService.BeginSessionAudit(session, 
            AuditTrailStrategy.OnObjectChanged, ObjectAuditingMode.Lightweight);
    }
    // ...
}
```
***