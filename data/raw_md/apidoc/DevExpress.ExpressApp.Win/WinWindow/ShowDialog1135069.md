---
uid: DevExpress.ExpressApp.Win.WinWindow.ShowDialog
name: ShowDialog()
type: Method
summary: Shows the [](xref:DevExpress.ExpressApp.Win.WinWindow)'s [WinWindow.Form](xref:DevExpress.ExpressApp.Win.WinWindow.Form) as a modal dialog box with the currently active window set as its owner.
syntax:
  content: public DialogResult ShowDialog()
  return:
    type: System.Windows.Forms.DialogResult
    description: A  **System.Windows.Forms.DialogResult** enumeration value, indicating the return value of the dialog box.
seealso: []
---
Generally, this method should not be called from your code. It is intended to be used in Show View Strategies (see [](xref:DevExpress.ExpressApp.ShowViewStrategyBase)) and internal classes only.