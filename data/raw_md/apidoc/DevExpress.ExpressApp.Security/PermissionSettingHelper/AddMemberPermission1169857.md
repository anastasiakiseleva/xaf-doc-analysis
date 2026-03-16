---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddMemberPermission(DevExpress.Persistent.Base.IPermissionPolicyRole,System.Type,System.String,System.String,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddMemberPermission(IPermissionPolicyRole, Type, String, String, String, Nullable<SecurityPermissionState>)
type: Method
summary: Finds the first type permission for the given type in the current role and adds the member permission to it. If the appropriate type permission is not found, it is created.
syntax:
  content: public static IPermissionPolicyMemberPermissionsObject AddMemberPermission(this IPermissionPolicyRole role, Type type, string operations, string members, string criteria, SecurityPermissionState? State)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  - id: type
    type: System.Type
    description: A [](xref:System.Type) object specifying the target type.
  - id: operations
    type: System.String
    description: A string containing the semicolon-separated list of security operations. Operation names and their delimiter are defined by string constants declared in the static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class.
  - id: members
    type: System.String
    description: A string containing the semicolon-separated list of target member names.
  - id: criteria
    type: System.String
    description: A string containing the [criteria expression](xref:4928) that specifies the target object(s).
  - id: State
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value specifying if access is granted or denied.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyMemberPermissionsObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyMemberPermissionsObject object specifying the added member permission.
seealso: []
---
