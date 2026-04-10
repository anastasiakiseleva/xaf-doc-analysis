---
uid: DevExpress.ExpressApp.Security.SecurityOptions.NewUserRoleName
name: NewUserRoleName
type: Property
summary: Specifies the name of a role assigned to an automatically created user.
syntax:
  content: public string NewUserRoleName { get; set; }
  parameters: []
  return:
    type: System.String
    description: The name of the default role.
seealso: []
---
This option is in effect when an application uses [Windows Active Directory Authentication](xref:119064#windows-active-directory-authentication) and the `CreateUserAutomatically` option is enabled.