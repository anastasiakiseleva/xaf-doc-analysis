---
uid: DevExpress.ExpressApp.Security.PermissionSettingHelper.AddMemberPermissionFromLambda``1(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String,System.String,System.Linq.Expressions.Expression{System.Func{``0,System.Boolean}},System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState})
name: AddMemberPermissionFromLambda<T>(IPermissionPolicyRole, String, String, Expression<Func<T, Boolean>>, Nullable<SecurityPermissionState>)
type: Method
summary: Finds the first type permission for the specified type in the _role_ and adds the member permission to it. If the appropriate type permission is not found, this method creates it.
syntax:
  content: |-
    public static IPermissionPolicyMemberPermissionsObject AddMemberPermissionFromLambda<T>(this IPermissionPolicyRole role, string operations, string members, Expression<Func<T, bool>> lambda, SecurityPermissionState? State)
        where T : class
  parameters:
  - id: role
    type: DevExpress.Persistent.Base.IPermissionPolicyRole
    description: The target role for a new object permission.
  - id: operations
    type: System.String
    description: The semicolon-separated list of security operations. The static [](xref:DevExpress.ExpressApp.Security.SecurityOperations) class defines operation names and their delimiter.
  - id: members
    type: System.String
    description: The semicolon-separated list of target member names.
  - id: lambda
    type: System.Linq.Expressions.Expression{System.Func{{T},System.Boolean}}
    description: 'The [lambda expression](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions) that specifies the target object(s). <!--The following help topic describes supported lambda expressions: [](xref:402860).-->'
  - id: State
    type: System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionState) enumeration value that specifies if access is granted or denied.
  typeParameters:
  - id: T
    description: This method finds the type permission for this type in the _role_.
  return:
    type: DevExpress.Persistent.Base.IPermissionPolicyMemberPermissionsObject
    description: The added member permission.
seealso: []
---
The following example demonstrates how to use this method in @DevExpress.ExpressApp.Updating.ModuleUpdater.UpdateDatabaseAfterUpdateSchema (_MySolution.Module_\\_DatabaseUpdater_\\_Updater.cs_):

# [C#](#tab/tabid-csharp)

```csharp{15-20}
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp.Security;
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp.Updating;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.PermissionPolicy;
// ...
public class Updater : ModuleUpdater {
    // ...
    public override void UpdateDatabaseAfterUpdateSchema() {
        base.UpdateDatabaseAfterUpdateSchema();
        PermissionPolicyRole defaultRole = ObjectSpace.FirstOrDefault<PermissionPolicyRole>(role => role.Name == "Default");
        if(defaultRole == null) {
            defaultRole = ObjectSpace.CreateObject<PermissionPolicyRole>();
            defaultRole.AddMemberPermissionFromLambda<ApplicationUser>(
                SecurityOperations.Write, 
                "ChangePasswordOnFirstLogon", 
                u => u.Oid == (Guid)CurrentUserIdOperator.CurrentUserId(), 
                SecurityPermissionState.Allow
            );
            // ...
        }
        // ...
    }
}
```

***

> [!Note]
> Alternatively, you can use the @DevExpress.ExpressApp.Security.PermissionSettingHelper.AddMemberPermission``1(DevExpress.Persistent.Base.IPermissionPolicyRole,System.String,System.String,System.String,System.Nullable{DevExpress.Persistent.Base.SecurityPermissionState}) method, which takes a [criteria expression](xref:4928) instead of a [lambda expression](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/lambda-expressions).

[`PermissionPolicyRole`]: xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRole
[`FindObject`]: xref:DevExpress.ExpressApp.IObjectSpace.FindObject``1(DevExpress.Data.Filtering.CriteriaOperator)
[`CreateObject`]: xref:DevExpress.ExpressApp.IObjectSpace.CreateObject``1
[`SecurityOperations`]: xref:DevExpress.ExpressApp.Security.SecurityOperations
[`SecurityPermissionState`]: xref:DevExpress.Persistent.Base.SecurityPermissionState
