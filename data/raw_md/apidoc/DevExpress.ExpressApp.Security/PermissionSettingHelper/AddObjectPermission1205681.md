---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddObjectPermission(DevExpress.Persistent.Base.IPermissionPolicyRole,System.Type,System.String,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddObjectPermission(IPermissionPolicyRole, Type, String, String, Nullable<SecurityPermissionState>)
type: Method
summary: Finds the first type permission for the specified type in the _role_ and adds the object permission to it. If the appropriate type permission is not found, this method creates it.
syntax:
  content: public static IPermissionPolicyObjectPermissionsObject AddObjectPermission(this IPermissionPolicyRole role, Type type, string operations, string criteria, SecurityPermissionState? state)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: The target role for a new object permission.
  - id: type
    type: System.Type
    description: This method finds the type permission for this type in the _role_.
  - id: operations
    type: System.String
    description: The semicolon-separated list of security operations. The static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class defines operation names and their delimiter.
  - id: criteria
    type: System.String
    description: The [criteria expression](xref:4928) that specifies the target object(s).
  - id: state
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value that specifies if access is granted or denied.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyObjectPermissionsObject
    description: The added object permission.
seealso: []
---
