---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.ActionPermissions
name: ActionPermissions
type: Property
summary: Gets the collection of objects that contain [Action permissions](xref:404633#action-permissions) associated with the current @DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.
syntax:
  content: |-
    [Aggregated]
    [Appearance("XPOActionPermissionsIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    [Association]
    public XPCollection<PermissionPolicyActionPermissionObject> ActionPermissions { get; }
  parameters: []
  return:
    type: DevExpress.Xpo.XPCollection{DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyActionPermissionObject}
    description: A collection of objects that contain [Action permissions](xref:404633#action-permissions) associated with the current @DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyRoleBase.
seealso: []
---
