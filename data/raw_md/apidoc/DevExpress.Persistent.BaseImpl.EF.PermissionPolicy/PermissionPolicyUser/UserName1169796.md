---
uid: DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser.UserName
name: UserName
type: Property
summary: Specifies the user's login name.
syntax:
  content: |-
    [RuleRequiredField("User Name required", "Save", "The user name must not be empty")]
    [RuleUniqueValue("User Name is unique", "Save", "The login with the entered UserName was already registered within the system")]
    [RuleUserNameFormatIsCorrect("The username is formatted correctly", "Save")]
    public virtual string UserName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the user's login name.
seealso: []
---
