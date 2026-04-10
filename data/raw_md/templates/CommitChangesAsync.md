The following code demonstrates how you can use this method in a WinForms-specific [View Controller](xref:112621#view-controllers).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win;
using DevExpress.ExpressApp.Xpo;
using DevExpress.Persistent.Base;
using DevExpress.XtraSplashScreen;
using System.Threading;
using System.Windows.Forms; 
// ...
public class AsyncChangeDueDateController : ObjectViewController<DetailView, DemoTask> {
    public AsyncChangeDueDateController() {
        SimpleAction changeDueDateAction =
            new SimpleAction(this, "ChangeDueDate", PredefinedCategory.Edit);
        changeDueDateAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        changeDueDateAction.Execute += ChangeDueDateAction_Execute;
    }
    async private void ChangeDueDateAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        IOverlaySplashScreenHandle handle = null;
        Control control = Frame.Template as Control;
        WinApplication application = Application as WinApplication;
        CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        ViewCurrentObject.DueDate = new System.DateTime(2019,10,21);
        try {
            if (control != null && control.IsHandleCreated) {
                handle = application.StartOverlayForm(control);
            }
            await ((XPObjectSpace)ObjectSpace).CommitChangesAsync(cancellationTokenSource.Token);
        }
        finally {
            if (handle != null) {
                application.StopOverlayForm(handle);
            }
        }
    }
}
```
***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]