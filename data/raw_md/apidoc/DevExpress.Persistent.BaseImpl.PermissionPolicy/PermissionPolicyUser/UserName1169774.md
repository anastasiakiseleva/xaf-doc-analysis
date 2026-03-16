---
uid: DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.UserName
name: UserName
type: Property
summary: Specifies the user's login name.
syntax:
  content: |-
    [RuleRequiredField("PermissionPolicyUser_UserName_RuleRequiredField", DefaultContexts.Save)]
    [RuleUniqueValue("PermissionPolicyUser_UserName_RuleUniqueValue", DefaultContexts.Save, "The login with the entered user name was already registered within the system")]
    [RuleUserNameFormatIsCorrect("PermissionPolicyUser_UserName_RuleUserNameFormatIsCorrect", DefaultContexts.Save)]
    public string UserName { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which is the user's login name.
seealso: []
---
