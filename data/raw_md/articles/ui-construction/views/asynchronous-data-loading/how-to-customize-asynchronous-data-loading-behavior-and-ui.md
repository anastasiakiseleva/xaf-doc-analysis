---
uid: '401750'
title: 'How to: Customize Asynchronous Data Loading Behavior and UI (Windows Forms)'
---
# How to: Customize Asynchronous Data Loading Behavior and UI (Windows Forms)

This topic describes how to use the built-in `AsyncLoadingCancelationController` and `AsyncLoadingIndicationController` to customize [asynchronous data loading](xref:401747) in your WinForms application.

## Show a Confirmation Message When a User Cancels Loading

### For All Views

In the _Program.cs_ file, set the static `ShowConfirmationDefault` field of the `AsyncLoadingCancelationController` to `true`.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using DevExpress.ExpressApp.Win.SystemModule;
// ...
public class Program {
    [STAThread]
    public static void Main(string[] arguments) {
        AsyncLoadingCancelationController.ShowConfirmationDefault = true;
        // ...
    }
    // ...
}
```
***

### For a Particular View

1. Add a new View Controller to the [WinForms application project](xref:118045) (_MySolution.Win_).
2. In the overridden `OnActivated` method, use the @DevExpress.ExpressApp.Frame.GetController``1 method to access the `AsyncLoadingCancelationController`. 
3. Set the `AsyncLoadingCancelationController`'s `ShowConfirmation` property to `true`.  

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.SystemModule;
// ...
public class EnableConfirmationController : ObjectViewController<ListView, Contact> {
    protected override void OnActivated() {
        base.OnActivated();
        AsyncLoadingCancelationController controller = Frame.GetController<AsyncLoadingCancelationController>();
        if (controller != null) {
            controller.ShowConfirmation = true;
        }
    }
}
```
***

The following image demonstrates the default confirmation message displayed when a user cancels data loading.

![Default confirmation message](~/images/AsyncLoadingCancelationController_ShowConfirmation.png)

To change the confirmation message text, open the Model Editor, navigate to the **Localization** | **Confirmations** | **ConfirmCancelAsyncOperation** node, and change its **Value**.

![Confirmation message in Model Editor](~/images/ConfirmCancelAsyncOperation.png)

## Disable Custom Actions While Data Loading

XAF disables all built-in Actions except **Close** to prevent manipulations of the current View's data. It is recommended that you disable custom Actions while View data is loading asynchronously. 

1. Create an `AsyncLoadingIndicationController`'s descendant in the [WinForms application project](xref:118045) (_MySolution.Win_).
2. Override its `UpdateActions` protected method.
3. In the overridden method, use the @DevExpress.ExpressApp.Frame.GetController``1 method to access a custom Controller that contains an Action you want to disable.
4. Pass this Action to the `AsyncLoadingIndicationController.UpdateAction` method.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.SystemModule;
// ...
public class UpdateCustomActionsOnAsyncLoadingController : AsyncLoadingIndicationController {
    protected override void UpdateActions(bool isEnabled) {
        base.UpdateActions(isEnabled);
        UpdateAction(Frame.GetController<CustomActionController>()?.CustomAction, isEnabled);
    }
}
```
***

The image below demonstrates how this Controller affects the UI.

![Custom Action in UI](~/images/AsyncLoadingIndicationController_UpdateAction.png)

## Customize Loading Indication

You can implement custom logic when an application starts or stops loading data. For example, you can display [text notifications](xref:118549), as shown below.

1. Create an `AsyncLoadingIndicationController`'s descendant in the [WinForms application project](xref:118045) (_MySolution.Win_).
2. Override its `StartLoading` and **`StopLoading` protected methods.
3. In the overridden methods, use the @DevExpress.ExpressApp.ShowViewStrategyBase.ShowMessage* method to show a notification.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Win.SystemModule;
using System.Windows.Forms;
// ...
public class CustomAsyncLoadingIndicationController : AsyncLoadingIndicationController {
    private void ShowMessage(string message, string caption, InformationType informationType) {
        MessageOptions options = new MessageOptions();
        options.Duration = 2000;
        options.Message = string.Format(message);
        options.Type = informationType;
        options.Win.Caption = caption;
        options.Win.Type = WinMessageType.Alert;
        Application.ShowViewStrategy.ShowMessage(options);
    }
    protected override void StopLoading() {
        base.StopLoading();
        ShowMessage("Operation completed", "Stop loading", InformationType.Info);
    }
    protected override void StartLoading(Control control) {
        base.StartLoading(control);
        ShowMessage("Data is loading", "Start loading", InformationType.Info);
    }
}
```
***

The following image shows the result.

![Custom Loading Indication](~/images/AsyncLoadingIndicationController_StartLoading.png)
