---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser.IsActive
name: IsActive
type: Property
summary: Specifies if a user is allowed to logon.
syntax:
  content: public virtual bool IsActive { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if a user is active; otherwise - **false**.'
seealso: []
---
Inactive users cannot login to the application. Set this property to **false** for a particular user to prohibit them from using the application.