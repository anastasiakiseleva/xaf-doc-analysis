---
uid: DevExpress.ExpressApp.Security.SecurityStrategy.AllowAnonymousAccess
name: AllowAnonymousAccess
type: Property
summary: Specifies if users can access all secured data anonymously before they log in.
syntax:
  content: |-
    [Browsable(false)]
    public bool AllowAnonymousAccess { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if users can access secured data anonymously; otherwise, **false**. '
seealso: []
---
Anonymous access may be required when you use custom logon parameters and want to display certain data in the logon window before a user logs on.

> [!IMPORTANT]
> It is not recommended to allow anonymous access to all data using the **AllowAnonymousAccess** property. Instead, grant access to specific types only using the @DevExpress.ExpressApp.Security.SecurityStrategy.AnonymousAllowedTypes property. 
