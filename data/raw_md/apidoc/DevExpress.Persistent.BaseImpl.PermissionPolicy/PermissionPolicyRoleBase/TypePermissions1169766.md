---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.TypePermissions
name: TypePermissions
type: Property
summary: Gets the list of objects which contain type permissions associated with the current [](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase).
syntax:
  content: |-
    [Aggregated]
    [Appearance("XPOTypePermissionsIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    [Association]
    public XPCollection<PermissionPolicyTypePermissionObject> TypePermissions { get; }
  parameters: []
  return:
    type: DevExpress.Xpo.XPCollection{DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyTypePermissionObject}
    description: An IList\<**PermissionPolicyTypePermissionObject**\<, which is the list of the **PermissionPolicyTypePermissionObject** objects which are type permissions associated with the current role.
seealso: []
---
