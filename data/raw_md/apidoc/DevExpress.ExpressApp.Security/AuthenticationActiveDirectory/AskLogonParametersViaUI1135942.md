---
uid: DevExpress.ExpressApp.Security.AuthenticationActiveDirectory.AskLogonParametersViaUI
name: AskLogonParametersViaUI
type: Property
summary: A boolean value that indicates whether the logon process is interactive (a user inputs logon parameters manually).
syntax:
  content: public override bool AskLogonParametersViaUI { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true** if the logon process is interactive; otherwise, **false**.'
seealso: []
---
In the [](xref:DevExpress.ExpressApp.Security.AuthenticationActiveDirectory), this property value is always `false`, meaning the logon process is automated.

[!include[template-ask-logon-parameters-via-ui-blazor-limitation](~/templates/template-ask-logon-parameters-via-ui-blazor-limitation.md)]
