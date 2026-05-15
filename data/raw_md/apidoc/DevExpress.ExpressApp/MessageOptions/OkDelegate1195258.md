---
uid: DevExpress.ExpressApp.MessageOptions.OkDelegate
name: OkDelegate
type: Property
summary: Specifies a delegate that is executed when a user clicks a notification message (or if the [WinMessageOptions.Type](xref:DevExpress.ExpressApp.WinMessageOptions.Type) property is set to **Flyout** in a WinForms application and the  **OK** button is clicked).
syntax:
  content: public Action OkDelegate { get; set; }
  parameters: []
  return:
    type: System.Action
    description: A [](xref:System.Action) that is executed a user clicks the message.
seealso: []
---

### Winforms UI

The code snippet below demonstrates how to use this property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
public class ProjectTaskController : ViewController {
    //…
    MessageOptions options = new MessageOptions();
    options.OkDelegate = () => {
        IObjectSpace os = Application.CreateObjectSpace(typeof(ProjectTask));
        DetailView newTaskDetailView = Application.CreateDetailView(os, os.CreateObject<ProjectTask>());
        Application.ShowViewStrategy.ShowViewInPopupWindow(newTaskDetailView);
     };
     //…
     Application.ShowViewStrategy.ShowMessage(options);
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Public Class ProjectTaskController
    Inherits ViewController
    '…
    Private options As New MessageOptions()
    options.OkDelegate = Sub()
        Dim os As IObjectSpace = Application.CreateObjectSpace(GetType(ProjectTask))
        Dim newTaskDetailView As DetailView = Application.CreateDetailView(os, os.CreateObject(Of ProjectTask)())
        Application.ShowViewStrategy.ShowViewInPopupWindow(newTaskDetailView)
    End Sub
    '…
    Application.ShowViewStrategy.ShowMessage(options)
End Class
```

***

### ASP.NET Core Blazor UI

Use the **OkDelegate** property to specify a delegate that is executed when a user clicks the notification's OK button.