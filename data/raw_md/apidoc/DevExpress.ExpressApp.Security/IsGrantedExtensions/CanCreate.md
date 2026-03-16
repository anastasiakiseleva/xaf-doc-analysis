---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanCreate(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,System.Type,DevExpress.ExpressApp.IObjectSpace)
name: CanCreate(IRequestSecurityStrategy, Type, IObjectSpace)
type: Method
summary: Checks whether the current user can create objects of the specified type.
syntax:
  content: public static bool CanCreate(this IRequestSecurityStrategy security, Type type, IObjectSpace objectSpace)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: type
    type: System.Type
    description: The object's type.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) used to obtain data to calculate this security criterion.
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
        if (!securityStrategy.CanCreate(View.ObjectTypeInfo.Type, ObjectSpace)) {
            // ...  
        }
    }
}
```
***