---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanDelete``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace)
name: CanDelete<T>(IRequestSecurityStrategy, IObjectSpace)
type: Method
summary: Checks whether the current user can delete objects of the specified type.
syntax:
  content: public static bool CanDelete<T>(this IRequestSecurityStrategy security, IObjectSpace objectSpace)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) used to obtain data to calculate this security criterion.
  typeParameters:
  - id: T
    description: An object type.
  return:
    type: System.Boolean
    description: '`true`, if the current user can delete objects of the specified type; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// ...
public class CheckDeletePermissionController : ObjectViewController<ListView, Contact> {
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        if (!securityStrategy.CanDelete<Department>(ObjectSpace)) {
            // ...
        }
    }
}
```
***