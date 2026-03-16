---
uid: DevExpress.ExpressApp.View.CurrentObjectChanged
name: CurrentObjectChanged
type: Event
summary: Occurs after changing a View's focused object (not an object's property value).
syntax:
  content: public event EventHandler CurrentObjectChanged
seealso:
- linkId: DevExpress.ExpressApp.DetailView.CurrentObject
- linkId: DevExpress.ExpressApp.ListView.CurrentObject
- linkId: DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored
---
This event is raised in methods of the [](xref:DevExpress.ExpressApp.View) class descendants:

* [](xref:DevExpress.ExpressApp.DetailView)
    
   The **CurrentObjectChanged** event is raised after a currently displayed object (the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) property value) is changed. For example, this occurs when you navigate to another object using the [NextObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.NextObjectAction) or [PreviousObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.PreviousObjectAction).

* [](xref:DevExpress.ExpressApp.ListView)
    
    The **CurrentObjectChanged** event is raised when the focused object is changed in a [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor).

> [!IMPORTANT]
> [!include[CurrentObjectChanged_Important](~/templates/currentobjectchanged_important.md)]

The following example demonstrates how to use the **CurrentObjectChanged** event to make a View read-only:

# [C#](#tab/tabid-csharp)

```csharp
public class MyController : ViewController {
    protected override void OnActivated() {
        base.OnActivated();
        View.CurrentObjectChanged += View_CurrentObjectChanged;
        View_CurrentObjectChanged(View, new EventArgs());
    }
    private void View_CurrentObjectChanged(object sender, EventArgs e) {
       if (View.CurrentObject is Task) {
            View.AllowEdit["CurrentUser"] = ((Task)View.CurrentObject).Owner.Id == SecuritySystem.CurrentUserId;
       }
    }
    protected override void OnDeactivated() {           
        View.CurrentObjectChanged -= View_CurrentObjectChanged;
        base.OnDeactivated();
    }
}
```
***