The following code demonstrates how you can use this method in a [View Controller](xref:112621#view-controllers) to find and show a `Contact` the selected `DemoTask` is assigned to. If this `DemoTask` is not assigned to any `Contact`, XAF displays a Detail View for a new `Contact` object.


# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Data.Filtering;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.Xpo;
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
        Contact assignedTo = (Contact)ViewCurrentObject.AssignedTo;
            if (assignedTo != null) {
                object obj = await contactObjectSpace.FindObjectAsync<Contact>(
                    CriteriaOperator.Parse(string.Format("[Oid] = '{0}'", assignedTo.Oid)), true,
                    cancellationTokenSource.Token);
                contactView.CurrentObject = obj ?? contactObjectSpace.CreateObject(typeof(Contact));
            }
            else {
                contactView.CurrentObject = contactObjectSpace.CreateObject(typeof(Contact));
            }
        if (contactObjectSpace.IsNewObject(contactView.CurrentObject)) {
            contactObjectSpace.Committed += contactObjectSpace_Committed;
        }
    }
    private void contactObjectSpace_Committed(object sender, EventArgs e) {
        ViewCurrentObject.AssignedTo = ObjectSpace.GetObject(contactView.CurrentObject) as Contact;
    }
}
```
# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Data.Filtering
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.Actions
Imports DevExpress.ExpressApp.Xpo
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
        Dim assignedTo As Contact = CType(ViewCurrentObject.AssignedTo, Contact)
        If assignedTo IsNot Nothing Then
            Dim obj As Object = Await contactObjectSpace.FindObjectAsync(Of Contact)( _
                CriteriaOperator.Parse(String.Format("[Oid] = '{0}'", assignedTo.Oid)),
                True, cancellationTokenSource.Token)
            contactView.CurrentObject = If(obj, contactObjectSpace.CreateObject(GetType(Contact)))
        Else
            contactView.CurrentObject = contactObjectSpace.CreateObject(GetType(Contact))
        End If
        If contactObjectSpace.IsNewObject(contactView.CurrentObject) Then
            AddHandler contactObjectSpace.Committed, AddressOf contactObjectSpace_Committed
        End If
    End Sub
    Private Sub contactObjectSpace_Committed(ByVal sender As Object, ByVal e As EventArgs)
        ViewCurrentObject.AssignedTo = TryCast(ObjectSpace.GetObject(contactView.CurrentObject), Contact)
    End Sub
End Class
```

***

[!include[CancellationToken-info](~/templates/CancellationToken-info.md)]