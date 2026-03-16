---
uid: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.IsLogoffEnabled
name: IsLogoffEnabled
type: Property
summary: Gets a boolean value indicating that a user can log off and then logon again without restarting the application.
syntax:
  content: public override bool IsLogoffEnabled { get; }
  parameters: []
  return:
    type: System.Boolean
    description: A boolean value indicating that a user can log off the application.
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction
---
In the [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory) authentication, this property always returns **false**.