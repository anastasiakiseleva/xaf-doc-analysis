---
uid: DevExpress.ExpressApp.Security.XafApplicationExtensions.GetSecurityStrategy(DevExpress.ExpressApp.XafApplication)
name: GetSecurityStrategy(XafApplication)
type: Method
summary: Gets a @DevExpress.ExpressApp.Security.SecurityStrategy instance of an application's [Security System](xref:113366).
syntax:
  content: public static SecurityStrategy GetSecurityStrategy(this XafApplication xafApplication)
  parameters:
  - id: xafApplication
    type: DevExpress.ExpressApp.XafApplication
    description: An [](xref:DevExpress.ExpressApp.XafApplication) object that provides methods and properties to manage the current application.
  return:
    type: DevExpress.ExpressApp.Security.SecurityStrategy
    description: A [](xref:DevExpress.ExpressApp.Security.SecurityStrategy) object that specifies an application's Security Strategy.
seealso: []
---
The following example uses this method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// ...
public class SecurityStrategyController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        // ...
    }
}
```
***

Refer to the @DevExpress.ExpressApp.Security.IsGrantedExtensions class methods for more examples.