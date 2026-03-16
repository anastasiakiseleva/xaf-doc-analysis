---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanRead``1(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.Object,System.String)
name: CanRead<T>(IRequestSecurityStrategy, IObjectSpace, Object, String)
type: Method
summary: Checks whether the current user can read an object with the specified key. If the optional `memberName` parameter is specified, the method checks whether the current user can read the specified object member.
syntax:
  content: public static bool CanRead<T>(this IRequestSecurityStrategy security, IObjectSpace objectSpace, object targetObjectKey, string memberName = null)
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
  - id: memberName
    type: System.String
    defaultValue: "null"
    description: A name of the target object's member to check.
  typeParameters:
  - id: T
    description: The object's type.
  return:
    type: System.Boolean
    description: '`true`, if the current user can read the object or its member; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using System;
// ...
public class CheckReadPermissionController : ObjectViewController<ListView, Contact> {
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
            if (!securityStrategy.CanRead<Department>(ObjectSpace, key, nameof(Department.Office))) {
                // ...
            }
        }
    }
}
```

***
