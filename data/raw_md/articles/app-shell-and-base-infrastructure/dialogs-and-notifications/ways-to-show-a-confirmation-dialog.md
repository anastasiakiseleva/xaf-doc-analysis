---
uid: "118240"
seealso:
- linkId: "112803"
- linkId: "118222"
- linkId: "118165"
title: Ways to Show a Confirmation Dialog
---
# Ways to Show a Confirmation Dialog

This topic describes how to show a confirmation message/dialog with additional fields.

> [!TIP]
> If you want to show a text notification, refer to the following topic: [Text Notifications](xref:118549).


## Use the ConfirmationMessage Property

Use the [ActionBase.ConfirmationMessage](xref:DevExpress.ExpressApp.Actions.ActionBase.ConfirmationMessage) property in code or [IModelAction.ConfirmationMessage](xref:DevExpress.ExpressApp.Model.IModelAction.ConfirmationMessage) in the Model Editor to change a default confirmation message for built-in or custom [Actions](xref:112622).

For example, implement the following Controller to change the **Delete** Action's confirmation message:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.SystemModule;
using DevExpress.ExpressApp;
using System;

namespace MySolutionName.Module.Controllers {
    public class ConfirmationWindowActionController : ViewController {
        DeleteObjectsViewController deleteObjectsViewController;
        protected override void OnActivated() {
            base.OnActivated();
            deleteObjectsViewController = Frame.GetController<DeleteObjectsViewController>();
            if (deleteObjectsViewController != null) {
                View.SelectionChanged += View_SelectionChanged;
                SetConfirmationMessage();
            }
        }
        void View_SelectionChanged(object sender, EventArgs e) {
            SetConfirmationMessage();
        }

        private void SetConfirmationMessage() {
            deleteObjectsViewController.DeleteAction.ConfirmationMessage = String.Format("You are about to delete {0} object(s). Do you want to proceed?", View.SelectedObjects.Count);
        }

        protected override void OnDeactivated() {
            base.OnDeactivated();
            if (deleteObjectsViewController != null) {
                View.SelectionChanged -= View_SelectionChanged;
                deleteObjectsViewController = null;
            }
        }
    }
}
```
***

Click the **Delete** Action to see the result:

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor Application, DevExpress](~/images/xaf-blazor-confirmation-dialog.png)
Windows Forms
:   ![XAF WinForms Application, DevExpress](~/images/xaf-win-confirmation-dialog.png)

## Use a New Detail View
This section demonstrates how to invoke pop-up window with a non-persistent object's [Detail View](xref:DevExpress.ExpressApp.DetailView). 

Add the following [non-persistent class](xref:116516) to your platform-agnostic _MySolution.Module_ project. Decorate this class with the [](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) to register it in the [Types Info Subsystem](xref:113669).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Model;

[DomainComponent]
public class ConfirmationWindowParameters {
    public ConfirmationWindowParameters() { }
    [ModelDefault("AllowEdit", "False")]
    public string ConfirmationMessage { get; set; }
}
```
***

Use one of the following approaches to show the confirmation message in a pop-up window when an Action is executed: 
* [use the CustomizePopupWindowParams event](#use-the-customizepopupwindowparams-event);
* [use the ShowViewInPopupWindow method](#use-the-showviewinpopupwindow-method).

### Use the CustomizePopupWindowParams event

1. Create a new [](xref:DevExpress.ExpressApp.ViewController) and [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction) in its constructor. 
2. In the Action's `CustomizePopupWindowParams` event, create a [non-persistent Object Space](xref:DevExpress.ExpressApp.NonPersistentObjectSpace), a new  **`ConfirmationWindowParameters`** class instance, and the [](xref:DevExpress.ExpressApp.DetailView) for this object. 
3. Specify the `ConfirmationWindowParameters` object's properties and set the [CustomizePopupWindowParamsEventArgs.View](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.View) parameter to the newly created Detail View to show it in the pop-up window.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;

public class ConfirmationWindowController : ViewController {
    public ConfirmationWindowController() {
        PopupWindowShowAction showConfirmationWindowAction = 
new PopupWindowShowAction(this, "CustomConfirmationWindow", DevExpress.Persistent.Base.PredefinedCategory.View);
        showConfirmationWindowAction.ImageName = "ModelEditor_Views";
        showConfirmationWindowAction.CustomizePopupWindowParams += 
showConfirmationWindowAction_CustomizePopupWindowParams;
    }
    private void showConfirmationWindowAction_CustomizePopupWindowParams(object sender, 
CustomizePopupWindowParamsEventArgs e) {
        NonPersistentObjectSpace objectSpace = 
        (NonPersistentObjectSpace)Application.CreateObjectSpace(typeof(ConfirmationWindowParameters));
        ConfirmationWindowParameters parameters = objectSpace.CreateObject<ConfirmationWindowParameters>();
        parameters.ConfirmationMessage = "Confirmation message text.";
        objectSpace.CommitChanges();
        DetailView confirmationDetailView = Application.CreateDetailView(objectSpace, parameters);
        confirmationDetailView.Caption = "Custom Confirmation Window";
        confirmationDetailView.ViewEditMode = DevExpress.ExpressApp.Editors.ViewEditMode.View;
        e.View = confirmationDetailView;
    }
}
```
***

> [!Note]
> You can also process the **OK** and **Close** button clicks. For this purpose, use the [CustomizePopupWindowParamsEventArgs.DialogController](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.DialogController) property to access the Dialog Controller, and subscribe to its [Accepting](xref:DevExpress.ExpressApp.SystemModule.DialogController.Accepting) and [Canceling](xref:DevExpress.ExpressApp.SystemModule.DialogController.Cancelling) events.

### Use the ShowViewInPopupWindow method

1. Create a new [ViewController](xref:DevExpress.ExpressApp.ViewController) and [SimpleAction](xref:DevExpress.ExpressApp.Actions.SimpleAction) in its constructor.
2. In the Action's `Execute` event, create a [non-persistent Object Space](xref:DevExpress.ExpressApp.NonPersistentObjectSpace), a new `ConfirmationWindowParameters` class instance, and the [](xref:DevExpress.ExpressApp.DetailView) for this object.
3. Set the `ConfirmationWindowParameters` object's properties to the required values and call the [ShowViewStrategyBase.ShowViewInPopupWindow](xref:DevExpress.ExpressApp.ShowViewStrategyBase.ShowViewInPopupWindow(DevExpress.ExpressApp.View,System.Action,System.Action,System.String,System.String,DevExpress.ExpressApp.Frame,System.Action{DevExpress.ExpressApp.ShowViewParameters})) method. Pass the newly created Detail View as the `ShowViewInPopupWindow`'s first parameter to show this View in a pop-up. You can also pass delegates for processing the **OK** and **Cancel** buttons click. 

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;

public class ConfirmationWindowController : ViewController {
    public ConfirmationWindowController() {
        SimpleAction showConfirmationWindowAction = new SimpleAction(this, "CustomConfirmationWindow", PredefinedCategory.View);
        showConfirmationWindowAction.ImageName = "ModelEditor_Views";
        showConfirmationWindowAction.Execute += ShowConfirmationWindowAction_Execute;
    }
    private void ShowConfirmationWindowAction_Execute(object sender, 
    SimpleActionExecuteEventArgs e) {
        NonPersistentObjectSpace objectSpace = 
        (NonPersistentObjectSpace)Application.CreateObjectSpace(typeof(ConfirmationWindowParameters));
        ConfirmationWindowParameters parameters = new ConfirmationWindowParameters();
        parameters.ConfirmationMessage = "A confirmation message text.";
        DetailView confirmationDetailView = Application.CreateDetailView(objectSpace, parameters);
        confirmationDetailView.Caption = "Custom Confirmation Window";
        Application.ShowViewStrategy.ShowViewInPopupWindow(confirmationDetailView, OkDelegate, CancelDelegate);
    }
    public void OkDelegate() {
            Application.ShowViewStrategy.ShowMessage("The message is accepted!");
    }
    public void CancelDelegate() {
            Application.ShowViewStrategy.ShowMessage("The message is canceled!");
    }
}
```
***

The following images demonstrate the confirmation window (for both approaches):

ASP.NET Core Blazor
:   ![XAF ASP.NET Core Blazor Application Confirmation Window, DevExpress](~/images/xaf-blazor-confirmation-dialog-2.png)
Windows Forms
:   ![XAF Windows Forms Application Confirmation Window, DevExpress](~/images/xaf-win-confirmation-dialog-2.png)

## Use the Messaging Class' Methods (Windows Forms)

Use the [](xref:DevExpress.ExpressApp.Win.Core.Messaging) class's methods to display a confirmation message with standard dialog buttons (see [MessageBoxButtons](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.messageboxbuttons)) in WinForms applications. The following Controller demonstrates how to use this class to show a confirmation window:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win;

public class MessagingController : ViewController {
    public MessagingController() {
        SimpleAction showMessagingConfirmationForm = new SimpleAction(this, "CustomDeleteAction", DevExpress.Persistent.Base.PredefinedCategory.View);
        showMessagingConfirmationForm.ImageName = "Action_Delete";
        showMessagingConfirmationForm.Execute += showMessagingConfirmationForm_Execute;
    }
    void showMessagingConfirmationForm_Execute(object sender, SimpleActionExecuteEventArgs e) {
        if (WinApplication.Messaging.GetUserChoice("Do you want to delete the selected object(s)?", 
"Confirmation Window", MessageBoxButtons.YesNo) == DialogResult.Yes)
            View.ObjectSpace.Delete(e.SelectedObjects);
        View.ObjectSpace.CommitChanges();
    }
}
```
***

The image below demonstrates this implementation result.

![XAF Windows Forms, Custom Confirmation Message, DevExpress](~/images/xaf-win-confirmation-dialog-3.png)
