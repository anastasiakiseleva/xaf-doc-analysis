---
uid: DevExpress.ExpressApp.Actions.ActionBase.GetFormattedConfirmationMessage
name: GetFormattedConfirmationMessage()
type: Method
summary: Returns a formatted confirmation message displayed when executing an [Action](xref:112622).
syntax:
  content: public string GetFormattedConfirmationMessage()
  return:
    type: System.String
    description: A string that represents a formatted confirmation message.
seealso: []
---
Via an Action's [ActionBase.ConfirmationMessage](xref:DevExpress.ExpressApp.Actions.ActionBase.ConfirmationMessage) property, you can specify a message that will be displayed before executing the Action. Moreover, you can set this property to a string value that contains variables. When an [Action Container](xref:112610) performs a confirmation dialog display,  it uses the **GetFormattedConfirmationMessage** method to get the specified message.

When implementing a custom Action Container, use the **GetFormattedConfirmationMessage** to get an Action's cofirmation message.

You can handle the [ActionBase.CustomGetFormattedConfirmationMessage](xref:DevExpress.ExpressApp.Actions.ActionBase.CustomGetFormattedConfirmationMessage) event to customize this method result.