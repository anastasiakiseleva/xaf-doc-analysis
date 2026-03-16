---
uid: DevExpress.ExpressApp.Win.Core.Messaging.GetUserChoice(System.String,System.String,System.Windows.Forms.MessageBoxButtons)
name: GetUserChoice(String, String, MessageBoxButtons)
type: Method
summary: Displays a warning message box with specified message text, caption and buttons.
syntax:
  content: public DialogResult GetUserChoice(string message, string caption, MessageBoxButtons buttons)
  parameters:
  - id: message
    type: System.String
    description: A string which is the text displayed within the message box.
  - id: caption
    type: System.String
    description: A string which is the message box caption.
  - id: buttons
    type: System.Windows.Forms.MessageBoxButtons
    description: A [MessageBoxButtons](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.messageboxbuttons) enumeration value defining which buttons to display within the message box.
  return:
    type: System.Windows.Forms.DialogResult
    description: A [DialogResult](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.dialogresult) enumeration value, which indicates the user choice made within the message box.
seealso: []
---
This method used the [Messaging.Show](xref:DevExpress.ExpressApp.Win.Core.Messaging.Show*) method to display a message box. The [MessageBoxIcon.Warning](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.messageboxicon) icon is displayed within the message box.

![AskConfirmation_Save](~/images/askconfirmation_save116820.png)
