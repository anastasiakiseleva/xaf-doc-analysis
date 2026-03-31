---
uid: "403619"
title: Delete Objects from the Database
---
# Delete Objects from the Database

## Useful API

[IObjectSpace.Delete](xref:DevExpress.ExpressApp.IObjectSpace.Delete*) method
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.Delete*)]
[IObjectSpace.IsObjectToDelete](xref:DevExpress.ExpressApp.IObjectSpace.IsObjectToDelete(System.Object)) method
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsObjectToDelete(System.Object))]
[IObjectSpace.GetObjectsToDelete](xref:DevExpress.ExpressApp.IObjectSpace.GetObjectsToDelete(System.Boolean)) method
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.GetObjectsToDelete(System.Boolean))]
[IObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.IObjectSpace.CommitChanges) method
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.CommitChanges)]
[IObjectSpace.IsDeleting](xref:DevExpress.ExpressApp.IObjectSpace.IsDeleting) property
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.IsDeleting)]
[IObjectSpace.CustomDeleteObjects](xref:DevExpress.ExpressApp.IObjectSpace.CustomDeleteObjects) event
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.CustomDeleteObjects)]
[IObjectSpace.ObjectDeleting](xref:DevExpress.ExpressApp.IObjectSpace.ObjectDeleting) event
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.ObjectDeleting)]
[IObjectSpace.ObjectDeleted](xref:DevExpress.ExpressApp.IObjectSpace.ObjectDeleted) event
:   [!summary-include(DevExpress.ExpressApp.IObjectSpace.ObjectDeleted)]


## In a Controller

1. Create a new View Controller in a Module project (for example, in _MySolution.Module_).
2. Use the `ViewController.ObjectSpace` property to access an Object Space for data-aware operations.
3. Use the Object Space's methods to delete an object.
4. Call the @DevExpress.ExpressApp.IObjectSpace.CommitChanges method to save changes.

[!include[](~/templates/objectspace_deleteobjects.md)]

### Execute Custom Logic Instead of Deleting Objects

1. Create a new View Controller in a Module project (for example, in _MySolution.Module_).
2. In the overridden `OnActivated` method, subscribe to the @DevExpress.ExpressApp.IObjectSpace.CustomDeleteObjects event.
3. In the event handler, implement custom logic and set the `CustomDeleteObjectsEventArgs.Handled` property to `true` to prevent execution of default logic.

[!include[](~/templates/CustomDeleteObjects-codesnippet.md)]

## In an XPO Business Class

In XPO business class, you can perform additional business logic in the overridden `XPBaseObject.OnDeleting` method. The following code snippet demonstrates this. When you have a one-to-many association between two XPO business classes and delete an object of the one side of the association, the reference property of an object of the many side still contains the deleted object key. You can set this reference property value to `null` as demonstrated below.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.BaseImpl;
// ...
public class Employee : Person {
    // ...
    protected override void OnDeleting() {
        base.OnDeleting();
        foreach (object obj in Session.CollectReferencingObjects(this)) {
            if (Session.GetClassInfo(obj).ClassType == typeof(DemoTask)) {
                ((DemoTask)obj).Notes += 
                string.Format("The assigned employee was removed: {0}.\r\n", FullName);
            }
        }
    }
}
```
***
<!-- TODO: ## In EF Core Business Class -->