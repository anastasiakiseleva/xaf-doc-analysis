---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser
name: PermissionPolicyUser
type: Class
summary: An XAF user who has a list of associated security roles that support the **Allow/Deny** [Permission Policies](xref:116172).
syntax:
  content: |-
    [ImageName("BO_User")]
    [Persistent("PermissionPolicyUser")]
    [RuleCriteria("PermissionPolicyUser_XPO_Prevent_delete_logged_in_user", DefaultContexts.Delete, "[Oid] != CurrentUserId()", "Cannot delete the current logged-in user. Please log in using another user account and retry.")]
    public class PermissionPolicyUser : BaseObject, IPermissionPolicyUser, ISecurityUser, ISecurityUserWithRoles, IAuthenticationActiveDirectoryUser, IAuthenticationStandardUser, IXafCloneable
seealso:
- linkId: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser._members
  altText: PermissionPolicyUser Members
---
Associated roles are exposed via the [PermissionPolicyUser.Roles](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.Roles) property.