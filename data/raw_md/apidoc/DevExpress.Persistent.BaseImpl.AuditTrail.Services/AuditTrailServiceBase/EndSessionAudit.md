---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.EndSessionAudit(DevExpress.Xpo.Session)
name: EndSessionAudit(Session)
type: Method
summary: Stops auditing object changes made within the specified _session_.
syntax:
  content: public void EndSessionAudit(Session session)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session whose audit is to be stopped.
seealso: []
---
> [!Note]
> If you want to disable and enable the [Audit Trail Module](xref:112782) for a particular scenario, use solutions from the following help topic: [Disable the Audit Trail Module](xref:402080).

# [C#](#tab/tabid-csharp-net6)

```csharp{11}
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