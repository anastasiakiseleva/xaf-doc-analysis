---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.FindFirstTypePermission``1(DevExpress.Persistent.Base.IPermissionPolicyRole)
name: FindFirstTypePermission<T>(IPermissionPolicyRole)
type: Method
summary: Searches for the first permission for the specified type in the current role.
syntax:
  content: |-
    public static IPermissionPolicyTypePermissionObject FindFirstTypePermission<T>(this IPermissionPolicyRole role)
        where T : class
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  typeParameters:
  - id: T
    description: ''
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject object specifying the found type permission.
seealso: []
---
