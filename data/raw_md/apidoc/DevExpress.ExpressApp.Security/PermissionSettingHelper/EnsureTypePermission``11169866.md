---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.EnsureTypePermission``1(DevExpress.Persistent.Base.IPermissionPolicyRole)
name: EnsureTypePermission<T>(IPermissionPolicyRole)
type: Method
summary: Searches for the first permission for the specified type in the current role. If the type permission is not found, it is created.
syntax:
  content: |-
    public static IPermissionPolicyTypePermissionObject EnsureTypePermission<T>(this IPermissionPolicyRole role)
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
    description: A DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject object specifying the found or created type permission.
seealso: []
---
