---
uid: DevExpress.ExpressApp.Win.WinApplication.AskConfirmation(DevExpress.ExpressApp.ConfirmationType)
name: AskConfirmation(ConfirmationType)
type: Method
summary: Requests an end-user confirmation via the dialog window.
syntax:
  content: public override ConfirmationResult AskConfirmation(ConfirmationType confirmationType)
  parameters:
  - id: confirmationType
    type: DevExpress.ExpressApp.ConfirmationType
    description: A [](xref:DevExpress.ExpressApp.ConfirmationType) enumeration value specifying the confirmation dialog type.
  return:
    type: DevExpress.ExpressApp.ConfirmationResult
    description: A [](xref:DevExpress.ExpressApp.ConfirmationResult) enumeration value, specifying the end-user choice.
seealso: []
---
Overrides the [XafApplication.AskConfirmation](xref:DevExpress.ExpressApp.XafApplication.AskConfirmation(DevExpress.ExpressApp.ConfirmationType)) method. Uses the [WinApplication.GetUserChoice](xref:DevExpress.ExpressApp.Win.WinApplication.GetUserChoice(System.String,System.Windows.Forms.MessageBoxButtons)) method to display a confirmation dialog window of the required type. The user choice is [logged](xref:112575).

The following dialog is displayed when the [ConfirmationType.NeedSaveChanges](xref:DevExpress.ExpressApp.ConfirmationType.NeedSaveChanges) value is passed:

![AskConfirmation_Save](~/images/askconfirmation_save116820.png)

The "Do you want to save changes?" text is obtained from the [Application Model](xref:112580)'s **Localization** | **Confirmations** | **Save** node, and is [localizable](xref:112595).

The following dialog is displayed when the [ConfirmationType.CancelChanges](xref:DevExpress.ExpressApp.ConfirmationType.CancelChanges) value is passed:

![AskConfirmation_Cancel](~/images/askconfirmation_cancel116821.png)

The "Do you want to cancel your changes?" text is obtained from the Application Model's **Localization** | **Confirmations** | **Cancel** node, and is localizable.

This method is used in the [](xref:DevExpress.ExpressApp.Win.SystemModule.WinModificationsController) [Controller](xref:112621), to display confirmation dialogs when the [ModificationsController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.CancelAction) [Action](xref:112622) is executed, or the [View](xref:112611) is closed. To use the **AskConfirmation** method in a custom Controller, access the [](xref:DevExpress.ExpressApp.Win.WinApplication) object via the [Controller.Application](xref:DevExpress.ExpressApp.Controller.Application) property.