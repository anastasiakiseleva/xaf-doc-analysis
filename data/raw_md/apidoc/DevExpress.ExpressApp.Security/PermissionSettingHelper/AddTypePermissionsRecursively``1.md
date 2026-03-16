---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddTypePermissionsRecursively``1(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState},DevExpress.ExpressApp.DC.ITypesInfo)
name: AddTypePermissionsRecursively<T>(IPermissionPolicyRole, String, Nullable<SecurityPermissionState>, ITypesInfo)
type: Method
summary: Recursively adds type permissions to the current role for each type which [is assignable from](https://learn.microsoft.com/en-us/dotnet/api/system.type.isassignablefrom#System_Type_IsAssignableFrom_System_Type_) the given type (or is equal to it). If the permission for the type exists already, then the settings of this existing type permission are altered.
syntax:
  content: public static void AddTypePermissionsRecursively<T>(this IPermissionPolicyRole role, string operations, SecurityPermissionState? state, ITypesInfo typesInfo = null)
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: An [](xref:DevExpress.Persistent.Base.IPermissionPolicyRole) object specifying the security role.
  - id: operations
    type: System.String
    description: A string containing the semicolon-separated list of security operations. Operation names and their delimiter are defined by string constants declared in the static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class.
  - id: state
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value specifying if access is granted or denied.
  - id: typesInfo
    type: DevExpress.ExpressApp.DC.ITypesInfo
    defaultValue: "null"
    description: An @DevExpress.ExpressApp.DC.ITypesInfo object that provides access to XAF-related information on business classes.
  typeParameters:
  - id: T
    description: ''
seealso: []
---
