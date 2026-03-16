---
uid: DevExpress.ExpressApp.Win.WinApplication.GetUserChoice(System.String,System.Windows.Forms.MessageBoxButtons)
name: GetUserChoice(String, MessageBoxButtons)
type: Method
summary: Displays a message box with the specified text and set of buttons.
syntax:
  content: public DialogResult GetUserChoice(string message, MessageBoxButtons buttons)
  parameters:
  - id: message
    type: System.String
    description: A string, which is the message to be displayed within the message box.
  - id: buttons
    type: System.Windows.Forms.MessageBoxButtons
    description: A [MessageBoxButtons](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.messageboxbuttons) enumeration value defining buttons to display.
  return:
    type: System.Windows.Forms.DialogResult
    description: A [DialogResult](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.dialogresult) enumeration value specifying the user choice.
seealso: []
---
Uses the [Messaging.GetUserChoice](xref:DevExpress.ExpressApp.Win.Core.Messaging.GetUserChoice(System.String,System.String,System.Windows.Forms.MessageBoxButtons)) method to display a message box. The caption is set to the [XafApplication.Title](xref:DevExpress.ExpressApp.XafApplication.Title) value.
