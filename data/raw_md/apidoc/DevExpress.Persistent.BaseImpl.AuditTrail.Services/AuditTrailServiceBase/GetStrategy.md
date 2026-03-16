---
uid: DevExpress.Persistent.BaseImpl.AuditTrail.Services.AuditTrailServiceBase.GetStrategy(DevExpress.Xpo.Session)
name: GetStrategy(Session)
type: Method
summary: Gets the audit strategy for the specified _session_.
syntax:
  content: public AuditTrailStrategy? GetStrategy(Session session)
  parameters:
  - id: session
    type: DevExpress.Xpo.Session
    description: The @DevExpress.Xpo.Session object whose audit strategy this method returns.
  return:
    type: System.Nullable{DevExpress.Persistent.AuditTrail.AuditTrailStrategy}
    description: The _session_'s audit strategy.
seealso: []
---
The `AuditTrailStrategy` contains the following values:

`OnObjectLoaded`
:   The Audit Trail Module starts auditing an object when it is loaded.
`OnObjectChanged`
:   The Audit Trail Module starts auditing an object when it is changed.

# [C#](#tab/tabid-csharp-net6)

```csharp{11-12}
using DevExpress.ExpressApp;
using DevExpress.Persistent.AuditTrail;
using DevExpress.Xpo;
using Microsoft.Extensions.DependencyInjection;
// ...
public class MyController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        var auditTrailService = Application.ServiceProvider.GetRequiredService<AuditTrailService>();
        Session session = ((XPObjectSpace)ObjectSpace).Session;
        if (auditTrailService.GetStrategy(session).HasValue &&
            auditTrailService.GetStrategy(session).Value == AuditTrailStrategy.OnObjectLoaded) {
            // ...
        }
    }
    // ...
}
```
***