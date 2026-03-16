---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRole
name: PermissionPolicyRole
type: Class
summary: A security role that supports the **Allow/Deny** [Permission Policies](xref:116172).
syntax:
  content: |-
    [ImageName("BO_Role")]
    public class PermissionPolicyRole : PermissionPolicyRoleBase, IPermissionPolicyRoleWithUsers, ICanInitializeRole
seealso:
- linkId: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRole._members
  altText: PermissionPolicyRole Members
---
In **XAF** applications, permissions are not assigned to a user directly. Users have roles, which in turn are characterized by a permission set. So, each user has one or more roles that determine what actions can be performed. The list of users associated with the current role is exposed via the [PermissionPolicyRole.Users](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRole.Users) property.

Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic for an example of how to implement a custom Role.

> [!TIP]
> [!include[PermissionSettingHelper_Tip](~/templates/permissionsettinghelper_tip111727_1.md)]
