---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanDelete``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.Object)
name: CanDelete<T>(IRequestSecurityStrategy, IObjectSpace, Object)
type: Method
summary: Checks whether the current user can delete an object with the specified key.
syntax:
  content: public static bool CanDelete<T>(this IRequestSecurityStrategy security, IObjectSpace objectSpace, object targetObjectKey)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) used to obtain data to calculate this security criterion.
  - id: targetObjectKey
    type: System.Object
    description: The object's key.
  typeParameters:
  - id: T
    description: The object's type.
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
        securityStrategy = Application.GetSecurityStrategy();
        View.CurrentObjectChanged += View_CurrentObjectChanged;
    }
    private void View_CurrentObjectChanged(object sender, EventArgs e) {
        Department department = ViewCurrentObject.Department;
        if (department != null) {
            object key = ObjectSpace.GetKeyValue(department);
            if (!securityStrategy.CanDelete<Department>(ObjectSpace, key)) {
                // ...
            }
        }
    }
}
```

***