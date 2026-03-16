---
uid: DevExpress.Persistent.Base.Security.IAuthenticationStandardUser.SetPassword(System.String)
name: SetPassword(String)
type: Method
summary: Changes the user password.
syntax:
  content: void SetPassword(string password)
  parameters:
  - id: password
    type: System.String
    description: A string which is a new password.
seealso:
- linkId: "112649"
---
Passwords are stored encrypted and cannot be changed directly. Use this method to specify a password when creating a new user in code. An example is provided in the [Client-Side Security (2-Tier Architecture)](xref:113436) topic.