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
owner: Ekaterina Kiseleva
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
***
