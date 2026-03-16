---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanWrite(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,System.Type,DevExpress.ExpressApp.IObjectSpace,System.Object,System.String)
name: CanWrite(IRequestSecurityStrategy, Type, IObjectSpace, Object, String)
type: Method
summary: Checks whether the current user can write an object with the specified key. If the optional `memberName` parameter is specified, the method checks whether the current user can write the specified object member.
syntax:
  content: public static bool CanWrite(this IRequestSecurityStrategy security, Type type, IObjectSpace objectSpace, object targetObjectKey, string memberName = null)
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
  - id: memberName
    type: System.String
    defaultValue: "null"
    description: A name of the target object's member to check.
  return:
    type: System.Boolean
    description: '`true`, if the current user can write the object or its member; otherwise, `false`.'
seealso: []
---
# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Security;
using System;
// ...
public class CheckWritePermissionController : ObjectViewController<ListView, Contact> {
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
            if (!securityStrategy.CanWrite(typeof(Department), ObjectSpace, key, nameof(Department.Office))) {
                // ...
            }
        }
    }
}
```

***