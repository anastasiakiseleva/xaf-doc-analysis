---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanDelete(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,System.Type,DevExpress.ExpressApp.IObjectSpace,System.Object)
name: CanDelete(IRequestSecurityStrategy, Type, IObjectSpace, Object)
type: Method
summary: Checks whether the current user can delete an object with the specified key.
syntax:
  content: public static bool CanDelete(this IRequestSecurityStrategy security, Type type, IObjectSpace objectSpace, object targetObjectKey)
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
  - id: targetObjectKey
    type: System.Object
    description: The object's key.
  return:
    type: System.Boolean
    description: '`true`, if the current user can delete an object with the specified key; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using System;
// ...
public class CheckDeletePermissionController : ObjectViewController<ListView, Contact> {
    SecurityStrategy securityStrategy;
    protected override void OnActivated() {
        base.OnActivated();
        SecurityStrategy securityStrategy = Application.GetSecurityStrategy();
        View.CurrentObjectChanged += View_CurrentObjectChanged;
    }
    private void View_CurrentObjectChanged(object sender, EventArgs e) {
        Department department = ViewCurrentObject.Department;
        if (department != null) {
            object key = ObjectSpace.GetKeyValue(department);
            if (!securityStrategy.CanDelete(typeof(Department), ObjectSpace, key)) {
                // ...
            }
        }
    }
}
```

***