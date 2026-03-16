---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanCreate``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace)
name: CanCreate<T>(IRequestSecurityStrategy, IObjectSpace)
type: Method
summary: Checks whether the current user can create objects of the specified type.
syntax:
  content: public static bool CanCreate<T>(this IRequestSecurityStrategy security, IObjectSpace objectSpace)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) used to obtain data to calculate this security criterion.
  typeParameters:
  - id: T
    description: The object's type.
  return:
    type: System.Boolean
    description: '`true`, if the current user can create objects of the specified type; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// ...
public class CheckCreatePermissionController : ViewController<ListView> {
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        if (!securityStrategy.CanCreate<Contact>(ObjectSpace)) {
            // ...  
        }
    }
}
```
***
