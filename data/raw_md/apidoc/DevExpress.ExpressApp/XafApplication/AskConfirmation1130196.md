---
uid: DevExpress.ExpressApp.XafApplication.AskConfirmation(DevExpress.ExpressApp.ConfirmationType)
name: AskConfirmation(ConfirmationType)
type: Method
summary: Requests an end-user confirmation.
syntax:
  content: public virtual ConfirmationResult AskConfirmation(ConfirmationType confirmationType)
  parameters:
  - id: confirmationType
    type: DevExpress.ExpressApp.ConfirmationType
    description: A [](xref:DevExpress.ExpressApp.ConfirmationType) enumeration value.
  return:
    type: DevExpress.ExpressApp.ConfirmationResult
    description: A [](xref:DevExpress.ExpressApp.ConfirmationResult) enumeration value.
seealso: []
---
Only the [logging](xref:112575) functionality is implemented in this virtual method. The confirmation type and default confirmation result are logged. The **AskConfirmation** method is overridden in the [](xref:DevExpress.ExpressApp.Win.WinApplication) class, and user interaction is performed by the [WinApplication.AskConfirmation](xref:DevExpress.ExpressApp.Win.WinApplication.AskConfirmation(DevExpress.ExpressApp.ConfirmationType)) method. The **WebApplication.AskConfirmation** method does nothing except base functionality, because it is impossible to show a message box during a request.