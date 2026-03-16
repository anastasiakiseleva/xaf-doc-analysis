---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser.StoredPassword
name: StoredPassword
type: Property
summary: Specifies the encrypted password stored in the database.
syntax:
  content: |-
    [Browsable(false)]
    [NonCloneable]
    [SecurityBrowsable]
    public virtual string StoredPassword { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the encrypted password.
seealso: []
---
Passwords are stored encrypted and cannot be changed directly. Use `DevExpress.Persistent.BaseImpl.EF.User.SetPassword(System.String)` method to specify a password when creating a new user in code.