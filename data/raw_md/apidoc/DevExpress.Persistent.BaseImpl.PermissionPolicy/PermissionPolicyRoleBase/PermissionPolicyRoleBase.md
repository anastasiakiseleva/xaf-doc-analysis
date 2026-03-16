---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase
name: PermissionPolicyRoleBase
type: Class
summary: The base class for a security role that supports the **Allow/Deny** [Permission Policies](xref:116172).
syntax:
  content: |-
    [Persistent("PermissionPolicyRole")]
    public class PermissionPolicyRoleBase : BaseObject, IPermissionPolicyRole, ISecurityRole, ISecuritySystemRole, INavigationPermissions, IActionPermissions
seealso:
- linkId: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase._members
  altText: PermissionPolicyRoleBase Members
---
In **XAF** applications, permissions are not assigned to a user directly. Users have roles, which in turn are characterized by a permission set. So, each user has one or more roles that determine what actions can be performed. The list of users associated with the current role is exposed via the Users property.

Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example on implementing a custom Role.
> [!TIP]
> [!include[PermissionSettingHelper_Tip](~/templates/permissionsettinghelper_tip111727.md)]
