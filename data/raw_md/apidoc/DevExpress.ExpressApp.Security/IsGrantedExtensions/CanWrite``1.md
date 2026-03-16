---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanWrite``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.String)
name: CanWrite<T>(IRequestSecurityStrategy, IObjectSpace, String)
type: Method
summary: Checks whether the current user can write objects of the specified type. If the optional `memberName` parameter is specified, the method checks whether the current user can write the specified object members.
syntax:
  content: public static bool CanWrite<T>(this IRequestSecurityStrategy security, IObjectSpace objectSpace, string memberName = null)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) used to obtain data to calculate this security criterion.
  - id: memberName
    type: System.String
    defaultValue: "null"
    description: A name of the object member to check.
  typeParameters:
  - id: T
    description: An object type.
  return:
    type: System.Boolean
    description: '`true`, if the current user can write objects of the specified type or the specified object members; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
// ...
public class CheckWritePermissionController : ObjectViewController<ListView, Contact> {
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        if (!securityStrategy.CanWrite<Department>(ObjectSpace, nameof(Department.Office))) {
            // ...
        }
    }
}
```

***