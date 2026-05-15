---
uid: "112912"
seealso:
- linkId: DevExpress.ExpressApp.Controller.FrameAssigned
- linkId: "113258"
- linkType: HRef
  linkId: "402990"
  altText: Initialize Business Objects with Default Property Values in Entity Framework Core
- linkId: "113711"
title: 'How to: Initialize an Object Created Using the New Action'
---
# How to: Initialize an Object Created Using the New Action

This topic describes how to access an object that is created using the **New** [Action](xref:112622). Assume you are using the Task business class from the [Business Class Library](xref:112571). When creating a new Task using the **New** Action, the **Task.StartDate** property will be set to the current date.

To access an object created using the **New** Action, handle the [NewObjectViewController.ObjectCreated](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreated) event of the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) that contains the **New** Action. To do this, implement a new [View Controller](xref:112621). Override the Controller's **OnActivated** method and subscribe to the **ObjectCreated** event in the following manner:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp.SystemModule;
//...
public class MyController : ViewController {
    private NewObjectViewController controller;
    protected override void  OnActivated() {
        base.OnActivated();
        controller = Frame.GetController<NewObjectViewController>();
        if (controller != null) {
            controller.ObjectCreated += controller_ObjectCreated;
        }
    }
    void controller_ObjectCreated(object sender, ObjectCreatedEventArgs e) {
        if (e.CreatedObject is Task) {
            ((Task)e.CreatedObject).StartDate = DateTime.Now;
        }
    }
    protected override void OnDeactivated() {
        if (controller != null) {
            controller.ObjectCreated -= controller_ObjectCreated;
        }
        base.OnDeactivated();
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Imports DevExpress.Persistent.BaseImpl
Imports DevExpress.ExpressApp.SystemModule
'...
Public Class MyController
    Inherits ViewController
    Private controller As NewObjectViewController
    Protected Overrides Sub OnActivated()
        MyBase.OnActivated()
        controller = Frame.GetController(Of NewObjectViewController)()
        If controller IsNot Nothing Then
            AddHandler controller.ObjectCreated, AddressOf controller_ObjectCreated
        End If
    End Sub
    Private Sub controller_ObjectCreated(ByVal sender As Object, ByVal e As ObjectCreatedEventArgs)
        If TypeOf e.CreatedObject Is Task Then
            CType(e.CreatedObject, Task).StartDate = DateTime.Now
        End If
    End Sub
    Protected Overrides Sub OnDeactivated()
        If controller IsNot Nothing Then
            RemoveHandler controller.ObjectCreated, AddressOf controller_ObjectCreated
        End If
        MyBase.OnDeactivated()
    End Sub
End Class
```

***

In certain scenarios, it can be required to initialize a new object created through the lookup editor's New button, using a value from the parent Detail View. To access the parent object from the **ObjectCreated** event handler, cast the [Controller.Frame](xref:DevExpress.ExpressApp.Controller.Frame) value to the [](xref:DevExpress.ExpressApp.NestedFrame) type, access the [NestedFrame.ViewItem](xref:DevExpress.ExpressApp.NestedFrame.ViewItem) property and then get the master object using the [ViewItem.CurrentObject](xref:DevExpress.ExpressApp.Editors.ViewItem.CurrentObject) property.

# [C#](#tab/tabid-csharp)

```csharp
void controller_ObjectCreated(object sender, ObjectCreatedEventArgs e) {
    NestedFrame nestedFrame = Frame as NestedFrame;
    if (nestedFrame != null) {
        Item createdItem = e.CreatedObject as Item;
        if (createdItem != null) {
            Parent parent = ((NestedFrame)Frame).ViewItem.CurrentObject as Parent;
            if (parent != null) {
                createdItem.Title = parent.DefaultItemTitle;
            }
        }
    }
}
```

# [VB.NET](#tab/tabid-vb)

```vb
Private Sub controller_ObjectCreated(ByVal sender As Object, ByVal e As ObjectCreatedEventArgs)
    Dim nestedFrame As NestedFrame = TryCast(Frame, NestedFrame)
    If nestedFrame IsNot Nothing Then
        Dim createdItem As Item = TryCast(e.CreatedObject, Item)
        If createdItem IsNot Nothing Then
            Dim parent As Parent = TryCast(CType(Frame, NestedFrame).ViewItem.CurrentObject, Parent)
            If parent IsNot Nothing Then
                createdItem.Title = parent.DefaultItemTitle
            End If
        End If
    End If
End Sub
```

***
