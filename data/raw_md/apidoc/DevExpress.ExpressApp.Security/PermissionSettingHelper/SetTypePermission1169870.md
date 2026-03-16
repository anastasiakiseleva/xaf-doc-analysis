---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.SetTypePermission(DevExpress.Persistent.Base.IPermissionPolicyRole,System.Type,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: SetTypePermission(IPermissionPolicyRole, Type, String, Nullable<SecurityPermissionState>)
type: Method
summary: Searches for the first permission for the specified type in the current role, and rewrites its settings according to the specified parameters. If the type permission is not found, it is created.
syntax:
  content: public static IPermissionPolicyTypePermissionObject SetTypePermission(this IPermissionPolicyRole role, Type targetType, string operations, SecurityPermissionState? state)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  - id: targetType
    type: System.Type
    description: A [](xref:System.Type) object specifying the target type.
  - id: operations
    type: System.String
    description: A string containing the semicolon-separated list of security operations. Operation names and their delimiter are defined by string constants declared in the static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class.
  - id: state
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value specifying if access is granted or denied.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject object specifying the found or created type permission.
seealso: []
---
