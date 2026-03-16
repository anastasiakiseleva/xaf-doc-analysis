---
uid: DevExpress.ExpressApp.XafApplication.DetailViewCreating
name: DetailViewCreating
type: Event
summary: Occurs when creating a [Detail View](xref:112611).
syntax:
  content: public event EventHandler<DetailViewCreatingEventArgs> DetailViewCreating
seealso: []
---
Handle this event to provide a custom Detail View instead of a default one. Use the handler's [ViewCreatingEventArgs.ViewID](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID) parameter to get information on the created Detail View. To do this use the application's [XafApplication.FindModelView](xref:DevExpress.ExpressApp.XafApplication.FindModelView(System.String)) method passing the View ID as a parameter. To specify the Detail View's current object use the handler's [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) parameter. Create the Detail View in the Object Space passed as the handler's [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace) parameter.

The following example demonstrates how to handle the `DetailViewCreating` event to select a DetailView model based on properties of a displayed object:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
// using MainDemo.Module.BusinessObjects;

public class EmployeeDetailViewModelController : WindowController {
    public EmployeeDetailViewModelController() {
        TargetWindowType = WindowType.Main;
    }
    protected override void OnActivated() {
        base.OnActivated();
        Application.DetailViewCreating += Application_DetailViewCreating;
    }
    private void Application_DetailViewCreating(object sender, DetailViewCreatingEventArgs e) {
        if (e.ViewID == "Employee_DetailView" && e.Obj is Employee employee && employee.Position?.Title == "Manager") {
            e.ViewID = "Employee_DetailView_Manager";
        }
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        Application.DetailViewCreating -= Application_DetailViewCreating;
    }
}
```
***

[`ObjectViewController`]: xref:DevExpress.ExpressApp.ObjectViewController`2
[`DetailViewCreatingEventArgs`]: xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs
[`ViewID`]: xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID
[`/(Application)\./`]: xref:DevExpress.ExpressApp.Controller.Application

> [!Note]
> * When you open a Detail View from the [Navigation](xref:113198), the [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) argument of the @DevExpress.ExpressApp.XafApplication.DetailViewCreating event is set to *null*;
> * When you open a Detail View from a List View (by double-clicking a record or using the **OpenObject** Action), the [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) argument of the @DevExpress.ExpressApp.XafApplication.DetailViewCreating event is set to the object from the List View's Object Space.
