---
uid: DevExpress.ExpressApp.Security.IsGrantedExtensions.CanRead(DevExpress.ExpressApp.Security.IRequestSecurityStrategy,DevExpress.ExpressApp.IObjectSpace,System.Object,System.String)
name: CanRead(IRequestSecurityStrategy, IObjectSpace, Object, String)
type: Method
summary: Checks whether the current user can read the specified object. If the optional `memberName` parameter is specified, the method checks whether the current user can read the specified object member.
syntax:
  content: public static bool CanRead(this IRequestSecurityStrategy security, IObjectSpace objectSpace, object targetObject, string memberName = null)
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
  - id: memberName
    type: System.String
    defaultValue: "null"
    description: A name of the target object's member to check.
  return:
    type: System.Boolean
    description: '`true`, if the current user can read the object or its member; otherwise, `false`.'
seealso: []
---
