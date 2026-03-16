---
uid: DevExpress.ExpressApp.ShowViewStrategyBase.ShowMessage(DevExpress.ExpressApp.MessageOptions)
name: ShowMessage(MessageOptions)
type: Method
summary: Shows a [Text Notification](xref:118549).
syntax:
  content: public void ShowMessage(MessageOptions options)
  parameters:
  - id: options
    type: DevExpress.ExpressApp.MessageOptions
    description: A [](xref:DevExpress.ExpressApp.MessageOptions) object which contains the platform-agnostic and platform-specific notification parameters.
seealso: []
---

XAF displays the following platform-specific notifications:

ASP.NET Core Blazor
:   A custom Alert component.

    ![|A Text Notification in XAF ASP.NET Core Blazor Application, DevExpress|](~/images/showmessage_blazor.png)
Windows Forms
:   A [Toast Notification](xref:17020) with the "_Success_" caption.
    
    ![|A Text Notification in XAF Windows Forms Application, DevExpress|](~/images/showmessage_win127649.png)

Use the following technique to show the "_{0} task(s) have been successfully updated!_" notification for two seconds when a user clicks the **Mark Completed** action.

# [C#](#tab/tabid-csharp)

```csharp{17-24,29}
// ...
using DevExpress.ExpressApp;

namespace YourSolutionName.Module.Controllers {
    public class DemoTaskController : ViewController {
        public DemoTaskController() {
            // ...
            markCompletedAction.SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects;
            markCompletedAction.Execute += (s, e) => {
                foreach (DemoTask task in e.SelectedObjects) {
                    task.DueDate = DateTime.Now;
                    task.Status = MySolution.Module.BusinessObjects.TaskStatus.Completed;
                    View.ObjectSpace.SetModified(task);
                }
                View.ObjectSpace.CommitChanges();
                View.ObjectSpace.Refresh();
                MessageOptions options = new MessageOptions();
                options.Duration = 2000;
                options.Message = string.Format("{0} task(s) have been successfully updated!", e.SelectedObjects.Count);
                options.Type = InformationType.Success;
                options.Win.Caption = "Success";
                options.Win.Type = WinMessageType.Toast;
                options.OkDelegate = () => {
                    IObjectSpace os = Application.CreateObjectSpace(typeof(DemoTask));
                    DetailView newTaskDetailView = Application.CreateDetailView(os, os.CreateObject<DemoTask>());
                    Application.ShowViewStrategy.ShowViewInPopupWindow(newTaskDetailView);
                };
                Application.ShowViewStrategy.ShowMessage(options);
            };
        }
    }
}
```
***

In this example, `Application` is an [](xref:DevExpress.ExpressApp.XafApplication) object. Use the [Controller.Application](xref:DevExpress.ExpressApp.Controller.Application), [ActionBase.Application](xref:DevExpress.ExpressApp.Actions.ActionBase.Application) or [Frame.Application](xref:DevExpress.ExpressApp.Frame.Application) property to access it.

The [MessageOptions.OkDelegate](xref:DevExpress.ExpressApp.MessageOptions.OkDelegate) is executed when a user clicks the message (or, if the [WinMessageOptions.Type](xref:DevExpress.ExpressApp.WinMessageOptions.Type) property is set to `Flyout` in a Windows Forms application, when the **OK** button is clicked). If this delegate is not specified, the message is closed on a click. In the Flyout mode, you can also use [MessageOptions.CancelDelegate](xref:DevExpress.ExpressApp.MessageOptions.CancelDelegate) to provide a handler for the **Cancel** button.

For more examples of the `ShowMessage` method usage, refer to the following topic: [Text Notifications](xref:118549).