---
uid: "403618"
title: Save Objects to Database
owner: Dmitry Egorov
---
# Save Objects to Database

Common business tasks require additional logic before you store changes in a database. For example, you may need to get objects that are about to be saved and write additional information to them or save objects in a custom way.

## In a Controller

> [!spoiler][Useful API]
>
> {|
> |-
> ! Members !! Description
> |-
> | colspan="2"| **Methods**:
> |-
> | [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.CommitChanges)]
> |-
> | [IObjectSpace.IsObjectToSave](xref:DevExpress.ExpressApp.IObjectSpace.IsObjectToSave(System.Object)) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsObjectToSave(System.Object))]
> |-
> | [IObjectSpace.GetObjectsToSave](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsToSave(System.Boolean)) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectsToSave(System.Boolean))]
> |-
> | [IObjectSpace.RemoveFromModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.RemoveFromModifiedObjects(System.Object)) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.RemoveFromModifiedObjects(System.Object))]
> |-
> | colspan="2"| **Properties**:
> |-
> | [IObjectSpace.IsCommitting](xref:DevExpress.ExpressApp.IObjectSpace.IsCommitting) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsCommitting)]
> |-
> | [IObjectSpace.ModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.ModifiedObjects) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ModifiedObjects)]
> |-
> | colspan="2"| **Events**:
> |-
> | [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.Committing)]
> |-
> | [IObjectSpace.Committed](xref:DevExpress.ExpressApp.IObjectSpace.Committed) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.Committed)]
> |-
> | [IObjectSpace.CustomCommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges)]
> |-
> | [IObjectSpace.ObjectSaving](xref:DevExpress.ExpressApp.IObjectSpace.ObjectSaving) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ObjectSaving)]
> |-
> | [IObjectSpace.ObjectSaved](xref:DevExpress.ExpressApp.IObjectSpace.ObjectSaved) || [!summary-include(DevExpress.ExpressApp.IObjectSpace.ObjectSaved)]
> |}

XAF saves changes in a View in the following situations:

* The **Save**, **Save and New**, or **Save and Close** Action is executed.
* In a popup window, the Accept Action is executed and the [DialogController.SaveOnAccept](xref:DevExpress.ExpressApp.SystemModule.DialogController.SaveOnAccept) property is `true`. 

In XAF WinForms applications, you can control if XAF automatically saves or rolls back changes when you change the current object or close a View. The [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode) property specifies this behavior.

### Persist Changes in Code

To save changes in your code, call the [IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method.

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;

public class MyViewController : ObjectViewController<DetailView, Department> {
    public MyViewController() {
        var action = new SimpleAction(this, "Change Title and Save changes", DevExpress.Persistent.Base.PredefinedCategory.Save);
        action.Execute += Action_Execute;
    }
    private void Action_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Department department = (Department)View.CurrentObject;
        department.Title = "New Title";
        this.ObjectSpace.CommitChanges();
    }
}
```

### Obtain Modified Objects

To write additional information to an object before saving it to a database, do this in the [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing) event handler. The following code illustrates this. An `Employee` business object has the `Notes` property that stores audit information on a number of other objects that were changed in the current transaction.

```csharp{7,10}
using DevExpress.ExpressApp;
using System.Collections;

public class MyViewController : ObjectViewController<DetailView, Employee> {
    protected override void OnActivated() {
        base.OnActivated();
        ObjectSpace.Committing += ObjectSpace_Committing;
    }
    void ObjectSpace_Committing(object sender, System.ComponentModel.CancelEventArgs e) {
        ICollection collection = ObjectSpace.GetObjectsToSave(false);
        Employee owner = (Employee)View.CurrentObject;
        owner.Notes = string.Format("{0};{1} objects changed", owner.Notes, collection.Count);
    }
}
```

### Process Saving Objects

It's also possible to save changes in a custom way in the [IObjectSpace.CustomCommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CustomCommitChanges) event handler. To prevent the default logic to persist objects, handle the [IObjectSpace.Committing](xref:DevExpress.ExpressApp.IObjectSpace.Committing) event and call the [IObjectSpace.RemoveFromModifiedObjects](xref:DevExpress.ExpressApp.IObjectSpace.RemoveFromModifiedObjects(System.Object)) method to remove an object from being committed in the event handler.
[!include[](~/templates/os_committing_committed_customcommitchanges_reloaded.md)]

> [!NOTE]
> We recommend that you handle these events only for root Views. Nested Views use their parent View's Object Space. As a result, the events are handled several times. You can specify the controller scope as described at [](xref:113103). Alternatively, you can check properties like [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot) and [IObjectSpace.Owner](xref:DevExpress.ExpressApp.IObjectSpace.Owner) in event handlers to determine for what View a handler is invoked.

## In a Data Model (in an XPO Business Class)

In XPO business objects, override the `OnSaving` method of a business class to perform additional logic when you save data. A common task is to generate an auto-incremented number or a sequence. Find a sample for how to implement this at [XAF - How to generate a sequential number for a persistent object within a database transaction with Entity Framework Core](https://github.com/DevExpress-Examples/XAF_generate-a-sequential-number-for-a-persistent-object-within-a-database-transaction).

Be aware of the following specifics when you implement custom logic with [Integrated Mode](xref:113436#integrated-mode-xpo-and-ef-core) or [Middle Tier Security](xref:113439):

[!include[XPO-middle_tier_notes](~/templates/XPO-middle_tier_notes.md)]

<!-- TODO: ## In EF Core Business Class -->
