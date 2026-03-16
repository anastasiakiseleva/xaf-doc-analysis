---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.ChangePasswordOnFirstLogon
name: ChangePasswordOnFirstLogon
type: Property
summary: Specifies whether the user must change password on the next logon.
syntax:
  content: public bool ChangePasswordOnFirstLogon { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the user must change password on the next logon; otherwise - **false**.'
seealso: []
---
If this property is set to true for a particular user, an additional window will be displayed after authentication.

![ChangePasswordOnFirstLogon](~/images/changepasswordonfirstlogon115373.png)