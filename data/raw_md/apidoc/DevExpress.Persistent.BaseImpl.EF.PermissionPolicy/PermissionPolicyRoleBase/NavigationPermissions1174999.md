---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase.NavigationPermissions
name: NavigationPermissions
type: Property
summary: Gets the list of objects which contain navigation permissions associated with the current [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase).
syntax:
  content: |-
    [Aggregated]
    [Appearance("EFNavigationPermissionsIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    public virtual IList<PermissionPolicyNavigationPermissionObject> NavigationPermissions { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyNavigationPermissionObject}
    description: An IList\<**PermissionPolicyNavigationPermissionObject**>, which is the list of the **PermissionPolicyNavigationPermissionObject** objects which are navigation permissions associated with the current role.
seealso: []
---
