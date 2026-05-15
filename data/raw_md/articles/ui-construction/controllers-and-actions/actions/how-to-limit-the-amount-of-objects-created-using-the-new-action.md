---
uid: "112913"
seealso:
- linkId: DevExpress.ExpressApp.BaseObjectSpace.GetObjectsCount(System.Type,DevExpress.Data.Filtering.CriteriaOperator)
title: 'How to: Limit the Amount of Objects Created using the New Action'
---
# How to: Limit the Amount of Objects Created using the New Action

This topic describes how to limit the number of objects that an end-user can create using the **New** [Action](xref:112622). Assume you are using the Task business class from the [Business Class Library](xref:112571). When creating a new Task using the **New** Action, the count of existing Task objects will be checked and an end-user will not be allowed to create additional objects if there are already three objects.

To access the Task [List View](xref:112611) when the **New** Action is about to create a new object, handle the [NewObjectViewController.ObjectCreating](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreating) event of the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController), which contains the **New** Action. To do this, implement a new [View Controller](xref:112621) and override the **OnActivated** method in the following manner.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp.SystemModule;
//...
public class LimitTaskAmountController : ViewController {
	private NewObjectViewController controller;
    protected override void OnActivated() {
        base.OnActivated();
        controller = Frame.GetController<NewObjectViewController>();
        if (controller != null) {
            controller.ObjectCreating += controller_ObjectCreating;
        }
    }
    void controller_ObjectCreating(object sender, ObjectCreatingEventArgs e) {
        if ((e.ObjectType == typeof(Task)) && 
            (e.ObjectSpace.GetObjectsCount(typeof(Task), null) >= 3)) {
                e.Cancel = true;
                throw new UserFriendlyException(
                    "Cannot create a task. Maximum allowed task count exceeded.");
        }
    }
    protected override void OnDeactivated() {
        if (controller != null) {
            controller.ObjectCreating -= controller_ObjectCreating;
        }
        base.OnDeactivated();
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.ExpressApp
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.ExpressApp.SystemModule
'...
Public Class LimitTaskAmountController
    Inherits ViewController
    Private controller As NewObjectViewController
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        controller = Frame.GetController(Of NewObjectViewController)()
        If controller IsNot Nothing Then
            AddHandler controller.ObjectCreating, AddressOf controller_ObjectCreating
        End If
    End Sub
    Private Sub controller_ObjectCreating(ByVal sender As Object, ByVal e As ObjectCreatingEventArgs)
        If (e.ObjectType Is GetType(Task)) AndAlso (e.ObjectSpace.GetObjectsCount(GetType(Task), Nothing) >= 3) Then
                e.Cancel = True
                Throw New UserFriendlyException("Cannot create a task. Maximum allowed task count exceeded.")
        End If
    End Sub
    Protected Overrides Sub OnDeactivated()
        If controller IsNot Nothing Then
            RemoveHandler controller.ObjectCreating, AddressOf controller_ObjectCreating
        End If
        MyBase.OnDeactivated()
    End Sub
End Class
```

***

> [!NOTE]
> You can disable an Action instead of interrupting its execution. See the [How to: Disable an Action When the Current View Has Unsaved Changes](xref:113656) example.
