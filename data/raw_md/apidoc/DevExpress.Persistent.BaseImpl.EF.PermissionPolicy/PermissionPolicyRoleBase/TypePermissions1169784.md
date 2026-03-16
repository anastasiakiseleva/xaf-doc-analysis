---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase.TypePermissions
name: TypePermissions
type: Property
summary: Gets the list of objects which contain type permissions associated with the current [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase).
syntax:
  content: |-
    [Aggregated]
    [Appearance("EFTypePermissionsIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    public virtual IList<PermissionPolicyTypePermissionObject> TypePermissions { get; set; }
  parameters: []
  return:
    type: System.Collections.Generic.IList{DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyTypePermissionObject}
    description: An IList\<**PermissionPolicyTypePermissionObject**>, which is the list of the **PermissionPolicyTypePermissionObject** objects which are type permissions associated with the current role.
seealso: []
---
