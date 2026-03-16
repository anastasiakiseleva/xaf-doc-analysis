---
uid: DevExpress.ExpressApp.Win.Core.Messaging
name: Messaging
type: Class
summary: Provides methods used to display message boxes in Windows Forms XAF applications.
syntax:
  content: public class Messaging
seealso:
- linkId: DevExpress.ExpressApp.Win.Core.Messaging._members
  altText: Messaging Members
- linkId: "113312"
---
This class exposes the [Messaging.GetUserChoice](xref:DevExpress.ExpressApp.Win.Core.Messaging.GetUserChoice(System.String,System.String,System.Windows.Forms.MessageBoxButtons)) and overloaded [Messaging.Show](xref:DevExpress.ExpressApp.Win.Core.Messaging.Show*) methods, used by the [](xref:DevExpress.ExpressApp.Win.WinApplication) class to display confirmation messages, message boxes and exceptions (the [](xref:DevExpress.XtraEditors.XtraMessageBox) functionality is used by default).

![AskConfirmation_Save](~/images/askconfirmation_save116820.png)

**WinApplication** uses the [Messaging.GetMessaging](xref:DevExpress.ExpressApp.Win.Core.Messaging.GetMessaging(DevExpress.ExpressApp.XafApplication)) method to create a **Messaging** instance. The created instance is assigned to the [WinApplication.Messaging](xref:DevExpress.ExpressApp.Win.WinApplication.Messaging) property. You can implement a custom **Messaging** descendant by overriding the **ShowCore** method and specifying a descendant type via the [IModelOptionsWin.Messaging](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.Messaging) property in the [Model Editor](xref:112582) (see [How to: Implement a Custom Messaging Class](xref:113312)). Additionally, you can handle the [Messaging.ConfirmationDialogClosed](xref:DevExpress.ExpressApp.Win.Core.Messaging.ConfirmationDialogClosed) event to execute custom code after the message box is closed.

You can access a **Messaging** instance from your code and use the **GetUserChoice** or **Show** methods when it is required to show a message box in a Windows Forms application (see [How to: Customize the Export Action Behavior](xref:113287)).