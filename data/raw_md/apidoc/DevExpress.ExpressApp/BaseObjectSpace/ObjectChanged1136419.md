---
uid: DevExpress.ExpressApp.BaseObjectSpace.ObjectChanged
name: ObjectChanged
type: Event
summary: Raised when a persistent object is created, changed or deleted.
syntax:
  content: public event EventHandler<ObjectChangedEventArgs> ObjectChanged
seealso: []
---
This event must be raised by the **BaseObjectSpace** class' descendants.

The **ObjectChanged** event is raised both when an object is changed directly and by means of controls. When the **ObjectChanged** event is raised, the object change has not yet been saved to the database.

[!include[EF_ObjectChanged_Note](~/templates/ef_objectchanged_note111120.md)] Note that the required property should be implemented as described in the [The Importance of Property Change Notifications for Automatic UI Updates](xref:117395) article and decorated with the [](xref:DevExpress.Persistent.Base.ImmediatePostDataAttribute). The example below demonstrates how to get a new value from the **EffectiveDate** property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
//...
public class MyExampleViewController : ObjectViewController<DetailView, DemoObject> {
    private void ObjectSpace_ObjectChanged(object sender, ObjectChangedEventArgs e) {
        if (ViewCurrentObject != null) {
            if (e.PropertyName == "EffectiveDate") {
                ViewCurrentObject.RetroDate = ViewCurrentObject.EffectiveDate;
            }
        }
    }
    protected override void OnActivated() {
        base.OnActivated();
        View.ObjectSpace.ObjectChanged += ObjectSpace_ObjectChanged;
    }
    protected override void OnDeactivated() {
        base.OnDeactivated();
        View.ObjectSpace.ObjectChanged -= ObjectSpace_ObjectChanged;
    }
}
```
***