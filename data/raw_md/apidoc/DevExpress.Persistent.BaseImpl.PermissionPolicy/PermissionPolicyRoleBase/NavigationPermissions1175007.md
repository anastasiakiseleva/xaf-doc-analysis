---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.NavigationPermissions
name: NavigationPermissions
type: Property
summary: Gets the list of objects which contain navigation permissions associated with the current [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase).
syntax:
  content: |-
    [Aggregated]
    [Appearance("XPONavigationPermissionsIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    [Association]
    public XPCollection<PermissionPolicyNavigationPermissionObject> NavigationPermissions { get; }
  parameters: []
  return:
    type: DevExpress.Xpo.XPCollection{DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyNavigationPermissionObject}
    description: An IList\<**PermissionPolicyNavigationPermissionObject**\<, which is the list of the **PermissionPolicyNavigationPermissionObject** objects which are navigation permissions associated with the current role.
seealso: []
---
