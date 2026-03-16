---
uid: DevExpress.ExpressApp.XafApplication.ViewCreating
name: ViewCreating
type: Event
summary: Occurs when creating a [View](xref:112611).
syntax:
  content: public event EventHandler<ViewCreatingEventArgs> ViewCreating
seealso: []
---
Handle this event to provide a custom View instead of a default one. Use the handler's [ViewCreatingEventArgs.View](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.View) parameter to get information on the View being created. To do this, use the application's [XafApplication.FindModelView](xref:DevExpress.ExpressApp.XafApplication.FindModelView(System.String)) method passing the View ID as a parameter.

To specify the Detail View's current object use the handler's [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) parameter. Create the Detail View in the Object Space passed as the handler's [ViewCreatingEventArgs.ObjectSpace](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ObjectSpace) parameter.

To create a List View, use the collection source passed as the handler's [ListViewCreatingEventArgs.CollectionSource](xref:DevExpress.ExpressApp.ListViewCreatingEventArgs.CollectionSource) parameter. To specify whether the List View is root, use the handler's [ViewCreatingEventArgs.IsRoot](xref:DevExpress.ExpressApp.ViewCreatingEventArgs.IsRoot) parameter.

The following example demonstrates how to handle the **ViewCreating** event:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;

namespace MySolution.Module.Controllers {
    public class MyWindowController : WindowController {
        public MyWindowController() {
            TargetWindowType = WindowType.Main;
        }
        protected override void OnActivated() {
            base.OnActivated();
            Application.ViewCreating += Application_ViewCreating;
        }
        void Application_ViewCreating(object sender, ViewCreatingEventArgs e) {
            if (e.ViewID == "Contact_DetailView") {
                var os = Application.CreateObjectSpace(typeof(MyTask));
                var obj = os.CreateObject<MyTask>();
                obj.Subject = "New MyTask";
                var view = Application.CreateDetailView(os, obj);
                e.View = view;
            }
        }
        protected override void OnDeactivated() {
            base.OnDeactivated();
            Application.ViewCreating -= Application_ViewCreating;
        }
    }
}
```
***

[`WindowController`]: xref:DevExpress.ExpressApp.WindowController
[`TargetWindowType`]: xref:DevExpress.ExpressApp.WindowController.TargetWindowType
[`ViewCreatingEventArgs`]: xref:DevExpress.ExpressApp.ViewCreatingEventArgs
[`ViewID`]: xref:DevExpress.ExpressApp.ViewCreatingEventArgs.ViewID
[`/(Application)\./`]: xref:DevExpress.ExpressApp.Controller.Application
[`CreateObjectSpace`]: xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace(System.Type)
[`CreateObject`]: xref:DevExpress.ExpressApp.IObjectSpace.CreateObject``1
[`CreateDetailView`]: xref:DevExpress.ExpressApp.XafApplication.CreateDetailView(DevExpress.ExpressApp.IObjectSpace,System.Object)

> [!Note]
> * When you open a Detail View from the [Navigation](xref:113198), the [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) argument of the @DevExpress.ExpressApp.XafApplication.ViewCreating event is set to *null*;
> * When you open a Detail View from a List View (by double-clicking a record or using the **OpenObject** Action), the [DetailViewCreatingEventArgs.Obj](xref:DevExpress.ExpressApp.DetailViewCreatingEventArgs.Obj) argument of the @DevExpress.ExpressApp.XafApplication.ViewCreating event is set to the object from the List View's Object Space.