---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddObjectPermission``1(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddObjectPermission<T>(IPermissionPolicyRole, String, String, Nullable<SecurityPermissionState>)
type: Method
summary: Finds the first type permission for the specified type in the _role_ and adds the object permission to it. If the appropriate type permission is not found, this method creates it.
syntax:
  content: |-
    public static IPermissionPolicyObjectPermissionsObject AddObjectPermission<T>(this IPermissionPolicyRole role, string operations, string criteria, SecurityPermissionState? state)
        where T : class
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: The target role for a new object permission.
  - id: operations
    type: System.String
    description: The semicolon-separated list of security operations. The static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class defines operation names and their delimiter.
  - id: criteria
    type: System.String
    description: The [criteria expression](xref:4928) that specifies the target object(s).
  - id: state
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value that specifies if access is granted or denied.
  typeParameters:
  - id: T
    description: This method finds the type permission for this type in the _role_.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyObjectPermissionsObject
    description: The added object permission.
seealso: []
---
Alternatively, you can use the @DevExpress.ExpressApp.Security.PermissionSettingHelper.AddObjectPermissionFromLambda``1(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String,System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}},System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}) method, which takes a [lambda expression](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions) instead of a [criteria expression](xref:4928). <!--Refer to the following help topic for more information on supported lambda expressions: [](xref:402860).-->
