---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser.SetPassword(System.String)
name: SetPassword(String)
type: Method
summary: Changes the user password.
syntax:
  content: public void SetPassword(string password)
  parameters:
  - id: password
    type: System.String
    description: A string which is a new password.
seealso: []
---
The [](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser) class declares the public **StoredPassword** property to store a password. Passwords are stored encrypted and cannot be changed directly. Use this method to specify a password when creating a new user in code. An example is provided in the [Client-Side Security (2-Tier Architecture)](xref:113436) topic.

If you need to allow a user to change password using the **ChangePassword** action, grant the _write_ access to the **StoredPassword** property.