---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanDelete(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.Object)
name: CanDelete(IRequestSecurityStrategy, IObjectSpace, Object)
type: Method
summary: Checks whether the current user can delete the target object.
syntax:
  content: public static bool CanDelete(this IRequestSecurityStrategy security, IObjectSpace objectSpace, object targetObject)
  parameters:
  - id: security
    type: DevExpress.ExpressApp.Security.IRequestSecurityStrategy
    description: An object that specifies the application's security strategy.
  - id: objectSpace
    type: DevExpress.ExpressApp.IObjectSpace
    description: An [Object Space](xref:113707) used to obtain data to calculate this security criterion.
  - id: targetObject
    type: System.Object
    description: The target object to check.
  return:
    type: System.Boolean
    description: '`true`, if the current user can delete the target; otherwise, `false`.'
seealso: []
---
