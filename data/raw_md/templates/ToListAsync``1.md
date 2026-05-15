The following code snippet uses this method in a WinForms-specific [View Controller](xref:112621#view-controllers) to add contacts from the Development Department to the task's `Contacts` collection.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win;
using DevExpress.ExpressApp.Xpo;
using DevExpress.XtraSplashScreen;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
// ...
public class AsyncTaskContactsController : ObjectViewController<DetailView, DemoTask> {
    public AsyncTaskContactsController() : base() {
        base.OnActivated();
        SimpleAction assignToDepartmentAction = new SimpleAction(this, "Assign to the Dev.Departmant", "Edit");
        assignToDepartmentAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        assignToDepartmentAction.Execute += assignToDepartmentAction_Execute;
    }
    async private void assignToDepartmentAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        IOverlaySplashScreenHandle handle = null;
        Control control = Frame.Template as Control;
        WinApplication application = Application as WinApplication;
        CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        var contacts = from c in ObjectSpace.GetObjectsQuery<Contact>()
                        where c.Department.Title == "Development Department"
                        select c;
        IList<Contact> contactsList = null;
        try {
            if (control != null && control.IsHandleCreated) {
                handle = application.StartOverlayForm(control);
            }
            contactsList = await ((XPObjectSpace)ObjectSpace).ToListAsync<Contact>(contacts, cancellationTokenSource.Token);
            ViewCurrentObject.Contacts.AddRange(contactsList);
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
Imports DevExpress.XtraSplashScreen
Imports System.Collections.Generic
Imports System.Threading
Imports System.Windows.Forms
' ...
Public Class AsyncTaskContactsController
    Inherits ObjectViewController(Of DetailView, DemoTask)
    Public Sub New()
        MyBase.New()
        MyBase.OnActivated()
        Dim assignToDepartmentAction As New SimpleAction(Me, "Assign to the Dev.Departmant", "Edit")
        assignToDepartmentAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject
        AddHandler assignToDepartmentAction.Execute, AddressOf assignToDepartmentAction_Execute
    End Sub
    Private Async Sub assignToDepartmentAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim handle As IOverlaySplashScreenHandle = Nothing
        Dim control As Control = TryCast(Frame.Template, Control)
        Dim _application As WinApplication = TryCast(Application, WinApplication)
        Dim cancellationTokenSource As New CancellationTokenSource()
        Dim contacts As IQueryable(Of Contact) = From c In ObjectSpace.GetObjectsQuery(Of Contact)()
                                                 Where c.Department.Title = "Development Department"
                                                 Select c
        Dim contactsList As IList(Of Contact) = Nothing
        Try
            If control IsNot Nothing AndAlso control.IsHandleCreated Then
                handle = _application.StartOverlayForm(control)
            End If
            contactsList =
                Await CType(ObjectSpace, XPObjectSpace).ToListAsync(Of Contact)(contacts,
                cancellationTokenSource.Token)
            ViewCurrentObject.Contacts.AddRange(contactsList)
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