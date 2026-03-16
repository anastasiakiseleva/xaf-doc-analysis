---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddMemberPermission(DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject,System.String,System.String,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddMemberPermission(IPermissionPolicyTypePermissionObject, String, String, String, Nullable<SecurityPermissionState>)
type: Method
summary: Adds the member permission to the current type permission.
syntax:
  content: public static IPermissionPolicyMemberPermissionsObject AddMemberPermission(this IPermissionPolicyTypePermissionObject typePermission, string operations, string members, string criteria, SecurityPermissionState? State)
  parameters:
  - id: typePermission
    type: DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject
    description: An IPermissionPolicyTypePermissionObject object specifying the type permission.
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
