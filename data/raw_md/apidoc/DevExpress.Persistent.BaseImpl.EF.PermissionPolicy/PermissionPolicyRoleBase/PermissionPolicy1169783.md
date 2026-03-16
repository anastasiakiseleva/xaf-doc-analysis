---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase.PermissionPolicy
name: PermissionPolicy
type: Property
summary: Specifies the Security System behavior when there are no explicitly specified permissions for a specific type, object or member.
syntax:
  content: |-
    [Appearance("EFPermissionPolicyIsAdministrative", Enabled = false, Criteria = "IsAdministrative", Context = "DetailView")]
    [VisibleInListView(false)]
    public virtual SecurityPermissionPolicy PermissionPolicy { get; set; }
  parameters: []
  return:
    type: DevExpress.Persistent.Base.SecurityPermissionPolicy
    description: A [](xref:DevExpress.Persistent.Base.SecurityPermissionPolicy) enumeration value specifying the behavior when there are no explicitly specified permissions.
seealso: []
---
With this property, you can assign "deny all", "read only all" or "allow all" default permission policies for each role. For each operation, you can explicitly specify the _Allow_ or _Deny_ modifier or leave it blank.