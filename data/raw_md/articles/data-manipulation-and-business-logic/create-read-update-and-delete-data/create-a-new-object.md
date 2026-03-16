---
uid: "403616"
title: Create a New Object
owner: Dmitry Egorov
---
# Create a New Object

## Useful API

You can use following Object Space methods to create a new object:

[IObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) 
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type))]
[IObjectSpace.CreateObject\<ObjectType>](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject``1)
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.CreateObject``1)]
[XafApplication.CreateObject\<T>](xref:DevExpress.ExpressApp.XafApplication.CreateObject``1(DevExpress.ExpressApp.IObjectSpace@))
:   [!summary-include(DevExpress.ExpressApp.XafApplication.CreateObject``1(DevExpress.ExpressApp.IObjectSpace@))]
[IObjectSpace.IsNewObject](xref:DevExpress.ExpressApp.IObjectSpace.IsNewObject(System.Object))
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsNewObject(System.Object))]
[IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges)
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.CommitChanges)]


## In a Controller (the ORM-Independent Technique)

1. Create a new View Controller in a Module project (for example, in _MySolution.Module_).
2. Use the **ViewController.ObjectSpace** property to access an Object Space for data-aware operations.
3. Use the Object Space's methods to create a new object.
4. Call the @DevExpress.ExpressApp.IObjectSpace.CommitChanges method to save changes.


### Example 1

The following Controller contains the **AddTask** Action that creates a new **Task** object:

**File**: _MySolution.Module\Controllers\TaskViewController.cs_.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
// ...
public class TaskViewController : ObjectViewController<ListView, Task> {
    public TaskViewController() {
        SimpleAction addTaskAction = new SimpleAction(this, "AddTask", PredefinedCategory.Edit);
        addTaskAction.Execute += AddTaskAction_Execute;
    }
    private void AddTaskAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        Task task = ObjectSpace.CreateObject<Task>();
        task.Subject = "Demo Task";
        View.CollectionSource.Add(task);
        ObjectSpace.CommitChanges();
        View.Refresh();
    }
}
```
***

### Example 2

The following Controller contains the **AddTask** Action that adds a new **Task** object to the **Employee**'s **Tasks** collection. This Controller activates for the **Employee** Detail View and accesses the nested **Tasks** List View as described in the following topic: [](xref:113161).

**File**: _MySolution.Module\Controllers\EmployeeViewController.cs_.

# [C#](#tab/tabid-csharp)
```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.Actions;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.ExpressApp.Editors;
// ...
public class EmployeeViewController : ObjectViewController<DetailView, Employee> {
    public EmployeeViewController() {
        SimpleAction addTaskAction = new SimpleAction(this, "AddTask", PredefinedCategory.Edit);
        addTaskAction.Execute += AddTaskAction_Execute;
    }
    private void AddTaskAction_Execute(object sender, SimpleActionExecuteEventArgs e) {
        ListPropertyEditor listPropertyEditor = View.FindItem(nameof(Employee.Tasks)) as ListPropertyEditor;
        IObjectSpace os = listPropertyEditor.ListView.ObjectSpace;
        Task task = os.CreateObject<Task>();
        task.Subject = "Demo Task";
        listPropertyEditor.ListView.CollectionSource.Add(task);
        os.CommitChanges();
        listPropertyEditor.ListView.Refresh();
    }
}
```
***

## In an XPO Business Class

In an XPO business class, use the required business class constructor to create a new object and pass the current object's [Session](xref:DevExpress.Xpo.PersistentBase.Session) as the constructor parameter. You can do this in the overridden **AfterConstruction** method.

[!include[<9,12><10,13>](~/templates/createobjectinxpo.md)]

## In a EF Core Business Class

1. EF Core persistent classes implement the @DevExpress.ExpressApp.IObjectSpaceLink interface at runtime.
2. Cast a persistent object to the `IObjectSpaceLink` interface and get the @DevExpress.ExpressApp.IObjectSpaceLink.ObjectSpace  property value.
3. Use the @DevExpress.ExpressApp.IObjectSpaceLink.ObjectSpace methods to create a new object.

[!include[](~/templates/createobjectinefcore.md)]