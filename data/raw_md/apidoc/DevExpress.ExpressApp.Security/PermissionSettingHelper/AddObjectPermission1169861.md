---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddObjectPermission(DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject,System.String,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddObjectPermission(IPermissionPolicyTypePermissionObject, String, String, Nullable<SecurityPermissionState>)
type: Method
summary: Finds the first type permission for the given type in the current role and adds the object permission to it. If the appropriate type permission is not found, it is created.
syntax:
  content: public static IPermissionPolicyObjectPermissionsObject AddObjectPermission(this IPermissionPolicyTypePermissionObject typePermission, string operations, string criteria, SecurityPermissionState? State)
  parameters:
  - id: typePermission
    type: DevExpress.Persistent.Base.IPermissionPolicyTypePermissionObject
    description: An IPermissionPolicyTypePermissionObject object specifying the type permission.
  - id: operations
    type: System.String
    description: A string containing the semicolon-separated list of security operations. Operation names and their delimiter are defined by string constants declared in the static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class.
  - id: criteria
    type: System.String
    description: A string containing the [criteria expression](xref:4928) that specifies the target object(s).
  - id: State
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value specifying if access is granted or denied.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyObjectPermissionsObject
    description: A DevExpress.Persistent.Base.IPermissionPolicyObjectPermissionsObject object specifying the added object permission.
seealso: []
---
