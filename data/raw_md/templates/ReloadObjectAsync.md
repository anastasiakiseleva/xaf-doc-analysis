The following code uses this method in a [View Controller](xref:112621#view-controllers) to refresh a List View after a user changes an object on a Detail View and commits these changes. In this scenario, the List View should be [read-only](xref:DevExpress.ExpressApp.View.AllowEdit).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Win.Editors;
using DevExpress.ExpressApp.Xpo;
using System.Threading;
// ...
public class AsyncUpdateListViewController : ObjectViewController<ListView, DemoTask> {
    public AsyncUpdateListViewController() : base() {
        SimpleAction updateListViewAction = new SimpleAction(this, "Open assigned contact", "Edit");
        updateListViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        updateListViewAction.Execute += updateListViewAction_Execute;
    }
    private void updateListViewAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        object assignedContact = ViewCurrentObject.AssignedTo;
        IObjectSpace contactObjectSpace = Application.CreateObjectSpace(assignedContact.GetType());
        View contactView = Application.CreateDetailView(contactObjectSpace, contactObjectSpace.GetObject(assignedContact), true);
        e.ShowViewParameters.CreatedView = contactView;
        contactObjectSpace.Committed += async (s, args) => {
            CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
            await ((XPObjectSpace)ObjectSpace).ReloadObjectAsync(assignedContact, cancellationTokenSource.Token);
            if (View.Editor is GridListEditor) {
                GridListEditor gridListEditor = (GridListEditor)View.Editor;
                gridListEditor.GridView.LayoutChanged();
            }
        };
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Win.Editors
Imports DevExpress.ExpressApp.Xpo
Imports System.Threading
' ...
Public Class AsyncUpdateListViewController
    Inherits ObjectViewController(Of ListView, DemoTask)
    Public Sub New()
        MyBase.New()
        Dim updateListViewAction As New SimpleAction(Me, "Open assigned contact", "Edit")
        updateListViewAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject
        AddHandler updateListViewAction.Execute, AddressOf updateListViewAction_Execute
    End Sub
    Private Sub updateListViewAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim assignedContact As Object = ViewCurrentObject.AssignedTo
        Dim contactObjectSpace As IObjectSpace = Application.CreateObjectSpace(assignedContact.GetType())
        Dim contactView As View = Application.CreateDetailView(contactObjectSpace, contactObjectSpace.GetObject(assignedContact), True)
        e.ShowViewParameters.CreatedView = contactView
        AddHandler contactObjectSpace.Committed, Async Sub(s, args)
            Dim cancellationTokenSource As New CancellationTokenSource()
            Await (CType(ObjectSpace, XPObjectSpace)).ReloadObjectAsync(assignedContact, cancellationTokenSource.Token)
            If TypeOf View.Editor Is GridListEditor Then
                Dim gridListEditor As GridListEditor = CType(View.Editor, GridListEditor)
                gridListEditor.GridView.LayoutChanged()
            End If
        End Sub
    End Sub
End Class
```

***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]