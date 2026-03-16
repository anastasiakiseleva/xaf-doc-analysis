---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser
name: PermissionPolicyUser
type: Class
summary: An XAF user who has a list of associated security roles that support the **Allow/Deny** [Permission Policies](xref:116172).
syntax:
  content: |-
    [ImageName("BO_User")]
    [RuleCriteria("PermissionPolicyUser_EF_Prevent_delete_logged_in_user", DefaultContexts.Delete, "[ID] != CurrentUserId()", "Cannot delete the current logged-in user. Please log in using another user account and retry.")]
    public class PermissionPolicyUser : BaseObject, IPermissionPolicyUser, ISecurityUser, IAuthenticationActiveDirectoryUser, IAuthenticationStandardUser, ISecurityUserWithRoles, IXafCloneable
seealso:
- linkId: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser._members
  altText: PermissionPolicyUser Members
---
Associated roles are exposed via the [PermissionPolicyUser.Roles](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser.Roles) property.