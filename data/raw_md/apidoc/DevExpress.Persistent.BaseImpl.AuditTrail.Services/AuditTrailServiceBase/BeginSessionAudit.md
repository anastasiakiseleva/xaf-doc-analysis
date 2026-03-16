---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.BeginSessionAudit(DevExpress.Xpo.Session,DevExpress.Persistent.AuditTrail.AuditTrailStrategy)
name: BeginSessionAudit(Session, AuditTrailStrategy)
type: Method
summary: Starts auditing object changes made within the specified _session_.
syntax:
  content: public ObjectAuditProcessor BeginSessionAudit(Session session, AuditTrailStrategy strategy)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session to be audited.
  - id: strategy
    type: DevExpress.Persistent.AuditTrail.AuditTrailStrategy
    description: The **AuditTrailStrategy** value.
  return:
    type: DevExpress.Persistent.AuditTrail.ObjectAuditProcessor
    description: A processor that the Audit Trail Module uses for the specified _auditingMode_.
seealso: []
---
> [!Note]
> If you want to disable the [Audit Trail Module](xref:112782), use solutions from the following help topic: [Disable the Audit Trail Module](xref:402080).

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
            AuditTrailStrategy.OnObjectChanged);
    }
    // ...
}
```
***