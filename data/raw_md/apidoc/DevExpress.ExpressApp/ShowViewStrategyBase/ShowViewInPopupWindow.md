---
uid: DevExpress.ExpressApp.ShowViewStrategyBase.ShowViewInPopupWindow(DevExpress.ExpressApp.View,System.Action,System.Action,System.String,System.String,DevExpress.ExpressApp.Frame,System.Action{DevExpress.ExpressApp.ShowViewParameters})
name: ShowViewInPopupWindow(View, Action, Action, String, String, Frame, Action<ShowViewParameters>)
type: Method
summary: Shows the specified View in a popup dialog with **OK** and **Cancel** buttons.
syntax:
  content: public void ShowViewInPopupWindow(View view, Action okDelegate = null, Action cancelDelegate = null, string okButtonCaption = null, string cancelButtonCaption = null, Frame sourceFrame = null, Action<ShowViewParameters> configureDelegate = null)
  parameters:
  - id: view
    type: DevExpress.ExpressApp.View
    description: A View to be displayed in the pop-up window.
  - id: okDelegate
    type: System.Action
    defaultValue: "null"
    description: A delegate method that is executed when the **OK** button is clicked.
  - id: cancelDelegate
    type: System.Action
    defaultValue: "null"
    description: A delegate method that is executed when the **Cancel** button is clicked.
  - id: okButtonCaption
    type: System.String
    defaultValue: "null"
    description: The caption of the **OK** button.
  - id: cancelButtonCaption
    type: System.String
    defaultValue: "null"
    description: The caption of the **Cancel** button.
  - id: sourceFrame
    type: DevExpress.ExpressApp.Frame
    defaultValue: "null"
    description: A [Frame](xref:112608) from which the pop-up window is invoked.
  - id: configureDelegate
    type: System.Action{DevExpress.ExpressApp.ShowViewParameters}
    defaultValue: "null"
    description: A delegate method that allows you to configure View parameters before creating the pop-up window.
seealso: []
---
The `ShowViewInPopupWindow` method displays a dialog that contains the specified View and two buttons - **OK** and **Cancel**. Both buttons close the dialog.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.DC;
// ...
public class MyDialogController : ViewController {
    public MyDialogController() {
        SimpleAction action = new SimpleAction(this, "Email", "View");
        action.Execute += Action_Execute;
    }
    private void Action_Execute(object sender, SimpleActionExecuteEventArgs e) {
        IObjectSpace objectSpace = Application.CreateObjectSpace<MyDialog>();
        MyDialog myDialogObject = objectSpace.CreateObject<MyDialog>();
        myDialogObject.Message = "Do you want to send an email?";
        DetailView dialogView = Application.CreateDetailView(objectSpace, myDialogObject);
        Application.ShowViewStrategy.ShowViewInPopupWindow(dialogView,
            () => Application.ShowViewStrategy.ShowMessage("Done."),
            () => Application.ShowViewStrategy.ShowMessage("Cancelled."),
            null, null, this.Frame
        );
    }
}

[DomainComponent]
public class MyDialog {
    public string Message { get; set; }
}
```

### Advanced Example

This code sample calls the `ShowViewInPopupWindow` method and accesses the following information inside the method implementation:

* the initial view and its objects;
* the pop-up view and its objects;
* the @DevExpress.ExpressApp.ShowViewParameters and its objects;
* the dialog controller for configuration.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using MySolution.Module.BusinessObjects;
namespace MySolution.Blazor.Server.Controllers;
public class CustomBlazorController :ObjectViewController<DetailView, Contact> {
    public CustomBlazorController() {
        var myAction = new SimpleAction(this, "MyBlazorAction", PredefinedCategory.Edit);
        myAction.Execute += MyAction_Execute;
    }
    private void MyAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        var objectSpace = Application.CreateObjectSpace(typeof(Contact));
        var listView = Application.CreateListView(typeof(Contact), true);
        Application.ShowViewStrategy.ShowViewInPopupWindow(listView,
            () => {
                var mainViewObject = ((Contact)View.CurrentObject);
                var popupViewObjects = listView.SelectedObjects;
                Application.ShowViewStrategy.ShowMessage($"The main view's current object is {mainViewObject.FirstName}. The number of selected objects in the pop-up view is: {popupViewObjects.Count}");
            },
            () => Application.ShowViewStrategy.ShowMessage("Cancelled."),
            null, null, this.Frame,
            (showViewParameters) => {
                var dialogController = (DialogController)showViewParameters.Controllers.First(ctrl => ctrl is DialogController);
                dialogController.AcceptAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
            }
        );
    }
}
```

You can also use @DevExpress.ExpressApp.Actions.PopupWindowShowAction to show a [View](xref:112611) in a pop-up window. For more information, refer to the following help topic: [](xref:402158).