---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.IsSessionAudited(DevExpress.Xpo.Session)
name: IsSessionAudited(Session)
type: Method
summary: Indicates whether the [Audit Trail Module](xref:112782) audits object changes within the specified _session_.
syntax:
  content: public bool IsSessionAudited(Session session)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session object that this method checks.
  return:
    type: System.Boolean
    description: '`true` if the [Audit Trail Module](xref:112782) audits object changes in the specified _session_; otherwise, `false`.'
seealso: []
---
The following code snippet demonstrates the use of this method:

# [C#](#tab/tabid-csharp-net6)

```csharp{11-12}
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;

public partial class MyController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        Session session = ((XPObjectSpace)ObjectSpace).Session;
        var auditTrailService = Application.ServiceProvider.GetRequiredService<AuditTrailService>();
        if(auditTrailService.IsSessionAudited(session)) {
            auditTrailService.BeginSessionAudit(session,
            AuditTrailStrategy.OnObjectChanged, ObjectAuditingMode.Full);
        }
    }
    // ...
}
```
***