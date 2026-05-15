The following code uses this method in a WinForms-specific [View Controller](xref:112621#view-controllers).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Xpo;
using MainDemo.Module.BusinessObjects;
using System;
using System.Threading;
// ...
public class AsyncAssignedToInfoController : ObjectViewController<ListView, DemoTask> {
    View contactView = null;
    public AsyncAssignedToInfoController() : base() {
        SimpleAction showAssignedToInfoAction = new SimpleAction(this, "Assigned contact's info", "Edit");
        showAssignedToInfoAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject;
        showAssignedToInfoAction.Execute += showAssignedToInfoAction_Execute;
    }
    async private void showAssignedToInfoAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        XPObjectSpace contactObjectSpace = (XPObjectSpace)Application.CreateObjectSpace(typeof(Contact));
        contactView = Application.CreateDetailView(contactObjectSpace, "Contact_DetailView", true);
        e.ShowViewParameters.CreatedView = contactView;
        Contact obj = null;
        if (ViewCurrentObject.AssignedTo != null) {
            obj = (Contact)await contactObjectSpace.GetObjectAsync(ViewCurrentObject.AssignedTo);
            Contact[] contacts = new Contact[] { obj };
            await contactObjectSpace.PreFetchAsync(contacts, new string[] { "Tasks" });
        }
        if (obj == null) {
            obj = contactObjectSpace.CreateObject<Contact>();
            contactObjectSpace.Committed += contactObjectSpace_Committed;
        }
        contactView.CurrentObject = obj;
    }
    private void contactObjectSpace_Committed(object sender, EventArgs e) {
        ViewCurrentObject.AssignedTo = ObjectSpace.GetObject(contactView.CurrentObject) as Contact;
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Xpo
Imports MainDemo.Module.BusinessObjects
Imports System
Imports System.Threading
' ...
Public Class AsyncAssignedToInfoController
    Inherits ObjectViewController(Of ListView, DemoTask)
    Private contactView As View = Nothing
    Public Sub New()
        MyBase.New()
        Dim showAssignedToInfoAction As New SimpleAction(Me, "Assigned contact's info", "Edit")
        showAssignedToInfoAction.SelectionDependencyType = SelectionDependencyType.RequireSingleObject
        AddHandler showAssignedToInfoAction.Execute, AddressOf showAssignedToInfoAction_Execute
    End Sub
    Private Async Sub showAssignedToInfoAction_Execute(ByVal sender As Object, ByVal e As SimpleActionExecuteEventArgs)
        Dim cancellationTokenSource As New CancellationTokenSource()
        Dim contactObjectSpace As XPObjectSpace = CType(Application.CreateObjectSpace(GetType(Contact)), XPObjectSpace)
        contactView = Application.CreateDetailView(contactObjectSpace, "Contact_DetailView", True)
        e.ShowViewParameters.CreatedView = contactView
        Dim obj As Contact = Nothing
        If ViewCurrentObject.AssignedTo IsNot Nothing Then
            obj = CType(Await contactObjectSpace.GetObjectAsync(ViewCurrentObject.AssignedTo), Contact)
            Dim contacts() As Contact = {obj}
            Await contactObjectSpace.PreFetchAsync(contacts, New String() {"Tasks"})
        End If
        If obj Is Nothing Then
            obj = contactObjectSpace.CreateObject(Of Contact)()
            AddHandler contactObjectSpace.Committed, AddressOf contactObjectSpace_Committed
        End If
        contactView.CurrentObject = obj
    End Sub
    Private Sub contactObjectSpace_Committed(ByVal sender As Object, ByVal e As EventArgs)
        ViewCurrentObject.AssignedTo = TryCast(ObjectSpace.GetObject(contactView.CurrentObject), Contact)
    End Sub
End Class
```

***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]