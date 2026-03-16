---
uid: "113324"
title: 'How to: Access Objects Selected in the Current View'
seealso: 
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-print-a-report-without-displaying-a-preview
  altText: 'GitHub Example: XAF - How to Print a report without displaying a preview'
---
# How to: Access Objects Selected in the Current View

When working with **XAF** applications, end-users can select objects displayed in a [View](xref:112611). You may often need to access these objects from [Controllers](xref:112621) and [Actions](xref:112622) to perform various business tasks. For example, when implementing an Action, you may need to access a focused object to modify its property values when an Action is executed. This topic explains the basics of manipulating focused and selected objects, and provides sample code snippets.

## Access Currently Selected Objects When an Action is Executed

When an Action is executed, its **Execute** event is triggered. Regardless of the Action type, arguments passed to the event handler contain the [SimpleActionExecuteEventArgs.CurrentObject](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.CurrentObject) and [SimpleActionExecuteEventArgs.SelectedObjects](xref:DevExpress.ExpressApp.Actions.SimpleActionExecuteEventArgs.SelectedObjects) properties. The **CurrentObject** property specifies the current object of the active View. If an active View is a List View, this property specifies the focused object. If the View is a Detail View, the property specifies the object displayed by it. The **SelectedObjects** is a collection of the objects selected in the active View. In the case of a Detail View, this property returns the **CurrentObject** wrapped in a list.

The following code snippet demonstrates an Action intended for a Contact type. When the Action is executed, it adds a new line displaying information (about the moment when salary is transferred) to the **Note** property value of the currently selected objects in a List View, or an object displayed in a Detail View.

# [C#](#tab/tabid-csharp)

```csharp
using System;
using System.Collections;
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.ExpressApp.EF;
//...
public partial class MyNotesController : ViewController {
    public MyNotesController() {
        SimpleAction myAction = new SimpleAction(this, "Salary Info", "Edit");
        myAction.SelectionDependencyType = SelectionDependencyType.RequireMultipleObjects;
        myAction.TargetObjectType = typeof(Contact);
        myAction.Execute += myAction_Execute;
        Actions.Add(myAction);
    }
    void myAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        ArrayList SelectedContacts = new ArrayList();
        if ((e.SelectedObjects.Count > 0) && (e.SelectedObjects[0] is IObjectRecord)) {
            foreach (var selectedObject in e.SelectedObjects) {
                SelectedContacts.Add((Contact)ObjectSpace.GetObject(selectedObject));
            }
        }
        else {
            SelectedContacts = (ArrayList)e.SelectedObjects;
        }
        foreach (Contact selectedContact in SelectedContacts) {
            DateTime now = DateTime.Now;
            selectedContact.Notes += "\r\n[INFO] Your salary is transfered " + 
                now.ToString("M/d/yy") + " at " + now.ToString("hh:mm");
        }
        ObjectSpace.CommitChanges();
        ObjectSpace.Refresh();
    }
}
```
***

> [!NOTE]
> With the code above, each selected **Contact** object is obtained through a separate database request.

A specific View can be displayed when an Action is executed by specifying the [ActionBaseEventArgs.ShowViewParameters](xref:DevExpress.ExpressApp.Actions.ActionBaseEventArgs.ShowViewParameters) property of the **Execute** event handler or by using a [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction). However, regardless of the Action type, the **Execute** event handler arguments always contain focused and selected objects of the View for which the Action was invoked, and not for the View that was displayed as a result of the Action.

## Access Currently Selected Objects with a View Controller
A less common task is accessing focused and selected objects of a View from a Controller. In this instance, you should use the [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject) and [View.SelectedObjects](xref:DevExpress.ExpressApp.View.SelectedObjects) properties of the View object specified by the [ViewController.View](xref:DevExpress.ExpressApp.ViewController.View) property. The properties exposed by the View object have corresponding change notification events - [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged) and [View.SelectionChanged](xref:DevExpress.ExpressApp.View.SelectionChanged). So the best approach to accessing the focused and selected objects from a Controller is to handle these events.

The following code snippet demonstrates a Controller intended for Contact Detail Views. It changes the [DeleteObjectsViewController.DeleteAction](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.DeleteAction)'s [ActionBase.ConfirmationMessage](xref:DevExpress.ExpressApp.Actions.ActionBase.ConfirmationMessage). If you are going to delete one contact, the **FullName** of the **Contact** that is going to be deleted  will be added to the **ConfirmationMessage**. If you want to delete several contacts, the selected Contacts count will be added instead.

# [C#](#tab/tabid-csharp)

```csharp
public class MyConfirmationController : ViewController {
    private string defaultMessage;
    DeleteObjectsViewController deleteObjectsViewController;
    public MyConfirmationController() {
        this.TargetObjectType = typeof(Contact);
    }
    protected override void OnActivated() {
        base.OnActivated();
        deleteObjectsViewController = Frame.GetController<DeleteObjectsViewController>();
        if (deleteObjectsViewController != null) {
            defaultMessage = deleteObjectsViewController.DeleteAction.GetFormattedConfirmationMessage();
            View.SelectionChanged += View_SelectionChanged;
            UpdateConfirmationMessage();                
        }
    }
    void View_SelectionChanged(object sender, System.EventArgs e) {
        UpdateConfirmationMessage();
    }
    private void UpdateConfirmationMessage() {
        if (View.SelectedObjects.Count == 1) {
            deleteObjectsViewController.DeleteAction.ConfirmationMessage =
                String.Format("You are about to delete the '{0}' Contact. Do you want to proceed?",
                ((Contact)View.CurrentObject).FullName);
        }
        else {
            deleteObjectsViewController.DeleteAction.ConfirmationMessage =
                String.Format("You are about to delete {0} Contacts. Do you want to proceed?",
                (View.SelectedObjects.Count));
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        if (deleteObjectsViewController != null) {
            View.SelectionChanged -= View_SelectionChanged;
            deleteObjectsViewController.DeleteAction.ConfirmationMessage = defaultMessage;
            deleteObjectsViewController = null;
        }
    }
}
```
***

> [!NOTE]
> The **View.CurrentObject** and **View.SelectedObjects** properties return [](xref:DevExpress.ExpressApp.IObjectRecord) wrappers instead of original business objects when the View operates in the DataView, ServerView, InstantFeedback, or InstantFeedbackView [data access mode](xref:113683). To get the real object, use the **View.ObjectSpace.GetObject(obj)** method.

## Task-Based Help

- [How to: Create and Show a Detail View of the Selected Object in a Popup Window](xref:118760)
- [How to: Detect a Lookup List View in Code](xref:112908)
