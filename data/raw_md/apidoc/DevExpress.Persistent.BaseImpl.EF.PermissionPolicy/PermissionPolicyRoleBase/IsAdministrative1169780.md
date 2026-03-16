---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyRoleBase.IsAdministrative
name: IsAdministrative
type: Property
summary: Specifies whether users associated with the current role are administrators.
syntax:
  content: |-
    [ImmediatePostData]
    [ToolTip("Permissions are customizable and apply only to non-Administrative roles.")]
    public virtual bool IsAdministrative { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true`, if users associated with the current role are administrators; otherwise - `false`.'
seealso:
- linkId: "113436"
- linkId: "113384"
---
When the `IsAdministrative` option is set to `true`, it overrides all other permissions (both built-in and custom) and grants full access to all operations.