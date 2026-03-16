---
uid: "113312"
seealso:
- linkId: DevExpress.ExpressApp.Model.IModelOptions
- linkId: DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.Messaging
title: 'How to: Implement a Custom Messaging Class'
owner: Ekaterina Kiseleva
---
# How to: Implement a Custom Messaging Class

Message boxes that contain text and several buttons are be displayed in Windows Forms XAF applications in many situations. For instance, a message box is shown when an end-user closes a Detail View with modified data or cancels changes via the [ModificationsController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.CancelAction) Action. These message boxes are provided by the [](xref:DevExpress.ExpressApp.Win.Core.Messaging) class.

![AskConfirmation_Save](~/images/askconfirmation_save116820.png)

This class utilizes the [](xref:DevExpress.XtraEditors.XtraMessageBox) functionality. In certain scenarios it can be required to customize the `Messaging` class. In this instance you should inherit this class. This topic details a way of implementing such a descendant.

> [!NOTE]
> You can handle the [Messaging.ConfirmationDialogClosed](xref:DevExpress.ExpressApp.Win.Core.Messaging.ConfirmationDialogClosed) event instead of implementing a custom `Messaging` class, if executing a custom code after upon the closing of a message box is required.

## Change the Default Focused Button
The `Messaging` class exposes the [Messaging.Show](xref:DevExpress.ExpressApp.Win.Core.Messaging.Show*) virtual method, which displays a message box via the [XtraMessageBox.Show](xref:DevExpress.XtraEditors.XtraMessageBox.Show*) method. The `XtraMessageBox.Show` overload that takes _owner_, _text_, _caption_, _buttons_ and _icon_ parameters is used by default. This overload displays a message box with the first ("OK") button initially focused. In this example, we will override the `Messaging.Show` method and use another `XtraMessageBox.Show` method's overload that takes the _defaultButton_ extra parameter. Thus, it will be possible to specify which button to focus.

Add a new `CustomXtraMessageBoxMessaging` class to the [WinForms application project](xref:118045) (_MySolution.Win_). This class should inherit the `Messaging` class. Add the default public constructor and override the `ShowCore` method as it is shown in the snippet below.

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
using DevExpress.ExpressApp;
using DevExpress.XtraEditors;
using DevExpress.ExpressApp.Win.Core;
// ...
public class CustomXtraMessageBoxMessaging : Messaging {
    public CustomXtraMessageBoxMessaging(XafApplication application)
        : base(application) { }
    protected override DialogResult ShowCore(
        string message, string caption, MessageBoxButtons buttons, MessageBoxIcon icon) {
        return XtraMessageBox.Show(
           message, caption, buttons, icon, MessageBoxDefaultButton.Button2);
    }
}
```
***

Invoke the [Model Editor](xref:112582) for the Windows forms application project and navigate to the **Options** node. The [IModelOptionsWin.Messaging](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.Messaging) property specifies the type of messaging used in Windows Forms application. Set this property value to the fully qualified name of your custom class (e.g. `"CustomMessaging.Win.CustomXtraMessageBoxMessaging"`).

![CustomMessaging_3](~/images/custommessaging_3116824.png)

Run the Windows Forms application. Open any persistent object's Detail View and make some changes. Click **Close**. The message box with "No" button focused will be displayed.

![CustomMessaging1](~/images/custommessaging1116822.png)

## Use a custom Message Box instead of XtraMessageBox
You can use a fully custom message box in your `Messaging` implementation. In the snippet below, a use of [System.Windows.Forms.MessageBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.messagebox) class is demonstrated.

# [C#](#tab/tabid-csharp)

```csharp
using System.Windows.Forms;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.Core;
// ...
public class CustomWinFormsMessageBoxMessaging : Messaging {
    public CustomWinFormsMessageBoxMessaging(XafApplication application)
        : base(application) { }
    protected override DialogResult ShowCore(
        string message, string caption, MessageBoxButtons buttons, MessageBoxIcon icon) {
        return MessageBox.Show(message, caption, buttons, icon);
    }
}
```
***

Invoke the [Model Editor](xref:112582) for the Windows forms application project. Navigate to the **Options** node. Set the [IModelOptionsWin.Messaging](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.Messaging) property to the fully qualified name of your custom class (e.g. `"CustomMessaging.Win.CustomWinFormsMessageBoxMessaging"`).

Run the Windows Forms application. Open any persistent object's Detail View and make some changes. Click **Close**. The following message box will be displayed.

![CustomMessaging2](~/images/custommessaging2116823.png)
