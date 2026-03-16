---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.EnsureTypePermission(DevExpress.Persistent.Base.IPermissionPolicyRole,System.Type)
name: EnsureTypePermission(IPermissionPolicyRole, Type)
type: Method
summary: Searches for the first permission for the specified type in the current role. If the type permission is not found, it is created.
syntax:
  content: public static IPermissionPolicyTypePermissionObject EnsureTypePermission(this IPermissionPolicyRole role, Type targetType)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  - id: targetType
    type: System.Type
    description: A [](xref:System.Type) object specifying the target type.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject object specifying the found or created type permission.
seealso: []
---
