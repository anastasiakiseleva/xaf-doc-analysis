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
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Win
Imports DevExpress.ExpressApp.Xpo
Imports DevExpress.Persistent.Base
Imports DevExpress.XtraSplashScreen
Imports System.Threading
Imports System.Windows.Forms
' ...
Public Class AsyncChangeDueDateController
    Inherits ObjectViewController(Of DetailView, DemoTask)
    Public Sub New()
        Dim changeDueDateAction As New SimpleAction(Me, "ChangeDueDate", PredefinedCategory.Edit)
        changeDueDateAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject
        AddHandler changeDueDateAction.Execute, AddressOf ChangeDueDateAction_Execute
    End Sub
    Private Async Sub ChangeDueDateAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim handle As IOverlaySplashScreenHandle = Nothing
        Dim control As Control = TryCast(Frame.Template, Control)
        Dim _application As WinApplication = TryCast(Application, WinApplication)
        Dim cancellationTokenSource As New CancellationTokenSource()
        ViewCurrentObject.DueDate = New Date(2019, 10, 21)
        Try
            If control IsNot Nothing AndAlso control.IsHandleCreated Then
                handle = _application.StartOverlayForm(control)
            End If
            Await (CType(ObjectSpace, XPObjectSpace)).CommitChangesAsync(cancellationTokenSource.Token)
        Finally
            If handle IsNot Nothing Then
                _application.StopOverlayForm(handle)
            End If
        End Try
    End Sub
End Class
```

***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]