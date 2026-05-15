---
uid: DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.CustomHandleProcessSelectedItem
name: CustomHandleProcessSelectedItem
type: Event
summary: Occurs when an end-user double-clicks an object or presses Enter for a selected object in a WinForms application or clicks an object in a Web application in a List Editor.
syntax:
  content: public event EventHandler<HandledEventArgs> CustomHandleProcessSelectedItem
seealso: []
---

Subscribe to the **CustomHandleProcessSelectedItem** event to change how XAF processes a List Editor's object when a user attempts to open the object.

XAF opens the selected object's [Detail View](xref:112611#detail-view) if the object is in a [List View](xref:112611#list-view). If an end-user selects an object in a Lookup List View, XAF links the object to the current Detail View's object. To cancel this default processing, create the **CustomHandleProcessSelectedItem** event handler and set the **HandledEventArgs.Cancel** parameter to **true**. You can also use the handler to execute an [Action](xref:112622) - for example, to open a View for the selected object.

The **EmployeeLookupListViewController** below changes the default behavior for certain employees in a Lookup List View. If an employee is on leave, the end-user cannot link the employee to the current object, and the employee's Detail View opens. Otherwise, the end-user can link the employee to the master object.


# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.SystemModule;
using System.ComponentModel;
// ...
public class EmployeeLookupListViewController : ViewController {
    private ListViewProcessCurrentObjectController processCurrentObjectController;
    private OpenObjectController openObjectController;

    public EmployeeLookupListViewController() {
        TargetViewId = "Employee_LookupListView";
    }
    protected override void OnActivated() {
        base.OnActivated();
        processCurrentObjectController = Frame.GetController<ListViewProcessCurrentObjectController>();
        openObjectController = Frame.GetController<OpenObjectController>();
        if(processCurrentObjectController != null) {
          processCurrentObjectController.CustomHandleProcessSelectedItem += EmployeeLookupListViewController_CustomHandleProcessSelectedItem;
        }
    }
    private void EmployeeLookupListViewController_CustomHandleProcessSelectedItem(
        object sender, HandledEventArgs e) {
        Employee currentEmployee = (Employee)View.CurrentObject;
        if(currentEmployee.IsOnLeave) {
          e.Handled = true;
          if(openObjectController != null) {
            openObjectController.SetObjectToOpen(View.CurrentObject);
            if(openObjectController.OpenObjectAction.Active && openObjectController.OpenObjectAction.Enabled) {
              openObjectController.OpenObjectAction.DoExecute();
            }
          }
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if(processCurrentObjectController != null) {
          processCurrentObjectController.CustomHandleProcessSelectedItem -= EmployeeLookupListViewController_CustomHandleProcessSelectedItem;
          processCurrentObjectController = null;
        }
        openObjectController = null;
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.ExpressApp.SystemModule
Imports System.ComponentModel
' ...
Public Class EmployeeLookupListViewController
    Inherits ViewController
    
    Private _processCurrentObjectController As ListViewProcessCurrentObjectController
    Private _openObjectController As OpenObjectController
    
    Public Sub New()
        TargetViewId = "Employee_LookupListView"
    End Sub
    
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated
        Me._processCurrentObjectController = Frame.GetController(Of ListViewProcessCurrentObjectController)
        Me._openObjectController = Frame.GetController(Of OpenObjectController)
        If (Not (Me._processCurrentObjectController) Is Nothing) Then
            AddHandler Me._processCurrentObjectController.CustomHandleProcessSelectedItem, AdressOf EmployeeLookupListViewController_CustomHandleProcessSelectedItem
        End If
    End Sub
    
    Private Sub EmployeeLookupListViewController_CustomHandleProcessSelectedItem(ByVal sender As Object, ByVal e As HandledEventArgs)
        Dim currentEmployee As Employee = CType(View.CurrentObject,Employee)
        If currentEmployee.IsOnLeave Then
            e.Handled = true
            If (Not (Me._openObjectController) Is Nothing) Then
                Me._openObjectController.SetObjectToOpen(View.CurrentObject)
                If (Me._openObjectController.OpenObjectAction.Active AndAlso Me._openObjectController.OpenObjectAction.Enabled) Then
                    Me._openObjectController.OpenObjectAction.DoExecute
                End If
            End If
        End If
    End Sub
    Protected Overrides Sub OnDeactivated()
        MyBase.OnDeactivated
        If (Not (Me._processCurrentObjectController) Is Nothing) Then
            RemoveHandler Me._processCurrentObjectController.CustomHandleProcessSelectedItem, AddressOf EmployeeLookupListViewController_CustomHandleProcessSelectedItem
            Me._processCurrentObjectController = Nothing
        End If
        Me._openObjectController = Nothing
    End Sub
End Class
```
***