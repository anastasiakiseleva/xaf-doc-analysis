---
uid: DevExpress.ExpressApp.Security.AuthenticationStandard.AskLogonParametersViaUI
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
In the [](xref:DevExpress.ExpressApp.Security.AuthenticationStandard), this property value is always `true`: the user inputs logon parameters manually with the logon dialog.

[!include[template-ask-logon-parameters-via-ui-blazor-limitation](~/templates/template-ask-logon-parameters-via-ui-blazor-limitation.md)]
